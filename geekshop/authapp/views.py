from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth, messages
from basketapp.models import Basket

# Create your views here.


# авторизация
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username,password=password)

            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        #     else:
        #         print('user not activate')
        #
        # else:
        #     print(form.errors)

    else:
        form = UserLoginForm()

    context = {
        'title': 'Geekshop | Авторизция',
        'form': form
    }
    return render(request, 'authapp/login.html', context)


# регистрация
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('authapp:login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Geekshop | Регистрация',
        'form': form
    }
    return render(request, 'authapp/register.html', context)


# контроллер для личного кабинета
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    user_select = request.user
    context = {
        'title': 'Geekshop | Профайл',
        'form': UserProfileForm(instance=user_select),
        'baskets': Basket.objects.filter(user=user_select)

    }
    return render(request, 'authapp/profile.html', context)


# выйти из аккаунта
def logout(request):
    auth.logout(request)
    return render(request, 'mainapp/index.html')