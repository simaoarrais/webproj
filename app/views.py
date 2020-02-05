from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import datetime
from app.models import Restaurant, User as UserModel
from app.forms import LoginForm, RegisterForm, RegistRestaurantForm, UserInfoForm

# Create your views here.

def home(request):
    rests = Restaurant.objects.order_by('id')[0:3]
    tparams = {
        'title': 'Home Page',
        'year': datetime.now().year,
        'restaurants': rests
    }
    return render(request, 'index.html', tparams)


def contact(request):
    tparams = {
        'title': 'Contact',
        'message': 'Your contact page.',
        'year': datetime.now().year,
    }
    return render(request, 'contact.html', tparams)

def restaurants(request):
    if request.method == 'POST':
        query = request.POST['query']
        if query:
            rests = Restaurant.objects.filter(name__contains=query)
            return render(request, 'restaurants.html', {'title': 'Restaurants',
                                                    'year': datetime.now().year,
                                                    'restaurants': rests,
                                                    'query': query})

    return render(request, 'restaurants.html', {'title': 'Restaurants',
                                                'year': datetime.now().year,
                                                'restaurants': Restaurant.getById()})

def userinfo(request):
    user = UserModel.objects.get(username=request.user)

    if request.method == 'POST':
        userinfo_form = UserInfoForm(request.POST)
        if userinfo_form.is_valid():
            query = userinfo_form.cleaned_data
            # Guardar Modificações na DB
            user.username = query['username']
            user.password = query['password']
            user.first_name = query['first_name']
            user.last_name = query['last_name']
            user.email = query['email']
            user.save()

            return render(request, 'userinfo.html', {'title': 'Register',
                                                    'message': 'Your application description page.',
                                                    'year': datetime.now().year,
                                                    'form': userinfo_form})

    return render(request, 'userinfo.html', {'title': 'Register',
                                            'message': 'Your application description page.',
                                            'year': datetime.now().year,
                                            'form': UserInfoForm(initial={'username': user.username,
                                                                          'password': user.password,
                                                                          'first_name': user.first_name,
                                                                          'last_name': user.last_name,
                                                                          'email': user.email
                                                                          })
                                             })

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            query = login_form.cleaned_data
        return render(request, 'login.html', {'title': 'Login',
                                            'message': 'Your application description page.',
                                            'year': datetime.now().year,
                                            'form': login_form})
    return render(request, 'login.html', {'title': 'Login',
                                        'message': 'Your application description page.',
                                        'year': datetime.now().year,
                                        'form': LoginForm()})

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            query = register_form.cleaned_data
            #Guardar User na DB
            user = UserModel(username=query['username'], password=query['password'], first_name=query['first_name'], last_name=query['last_name'], email=query['email'])
            user.save()

            #Criação do User
            User.objects.create_user(username=query['username'], password=query['password'], email=query['email'])

            return render(request, 'register.html', {'title': 'Register',
                                                    'message': 'Your application description page.',
                                                    'year': datetime.now().year,
                                                    'form': register_form})

    return render(request, 'register.html', {'title': 'Register',
                                            'message': 'Your application description page.',
                                            'year': datetime.now().year,
                                            'form': RegisterForm()})

def registrestaurant(request):
    if request.method == 'POST':
        registrest_form = RegistRestaurantForm(request.POST)
        if registrest_form.is_valid():
            query = registrest_form.cleaned_data
            restaurant = Restaurant(name=query['name'], city=query['city'], address=query['address'],
                             cuisine=query['cuisine'])
            # Guardar User na DB
            restaurant.save()

            return render(request, 'registrestaurant.html', {'message': 'Your application description page.',
                                                     'year': datetime.now().year,
                                                     'form': registrest_form})

    return render(request, 'registrestaurant.html', {'title': 'Register',
                                             'message': 'Your application description page.',
                                             'year': datetime.now().year,
                                             'form': RegistRestaurantForm()})