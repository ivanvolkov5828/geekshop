from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth, messages
from basketapp.models import Basket
from django.contrib.auth.views import LogoutView, FormView, LoginView
from django.views.generic import UpdateView
from adminapp.mixins import BaseClassContextMixin, UserDispatchMixin
from authapp.models import User
# from geekshop import settings
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


# авторизация
# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#
#         if form.is_valid():
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = auth.authenticate(username=username,password=password)
#
#             if user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#         #     else:
#         #         print('user not activate')
#         #
#         # else:
#         #     print(form.errors)
#
#     else:
#         form = UserLoginForm()
#
#     context = {
#         'title': 'Geekshop | Авторизция',
#         'form': form
#     }
#     return render(request, 'authapp/login.html', context)


class LoginGBView(LoginView, BaseClassContextMixin):
    title = 'Geekshop | Авторизация'
    form_class = UserLoginForm
    template_name = 'authapp/login.html'


# регистрация
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегистрировались')
#             return HttpResponseRedirect(reverse('authapp:login'))
#         else:
#             print(form.errors)
#     else:
#         form = UserRegisterForm()
#     context = {
#         'title': 'Geekshop | Регистрация',
#         'form': form
#     }
#     return render(request, 'authapp/register.html', context)


class RegisterView(FormView, BaseClassContextMixin):
    model = User
    title = 'Geekshop | Регистрация'
    form_class = UserRegisterForm
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('authapp:login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save()
            if self.send_verify_link(user):
                messages.set_level(request, messages.SUCCESS)
                messages.error(request, form.errors)
                return HttpResponseRedirect(reverse('authapp:login'))
            else:
                messages.set_level(request, messages.ERROR)
                messages.success(request, 'Вы успешно зарегистрировались')
        else:
            messages.set_level(request, messages.ERROR)
            messages.success(request, 'Вы успешно зарегистрировались')

        return render(request, self.template_name, {'form': form})

    def send_verify_link(self):
        verify_link = reverse('authapp:verify', args=[User.email, User.activation_key])
        subject = f'Для активации учетной записи {User.username} пройдите по ссылки'
        message = f'Для подтверждения учетной записи {User.username} на портале \n {settings.DOMAIN_NAME}{verify_link}'
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [User.email], fail_silently=False)

    def verify(self, email, activate_key):
        try:
            user = User.objects.get(email=email)
            if user and user.activation_key == activate_key and not user.is_activation_key_expires():
                user.activation_key=''
                user.activation_key_expires = None
                user.is_active = True
                user.save()
                auth.login(self, user)
            return render(self, 'authapp/verification.html')

        except Exception as e:
            return HttpResponseRedirect(reverse('index'))

# контроллер для личного кабинета
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#         else:
#             print(form.errors)
#
#     user_select = request.user
#     context = {
#         'title': 'Geekshop | Профайл',
#         'form': UserProfileForm(instance=user_select),
#         'baskets': Basket.objects.filter(user=user_select)
#
#     }
#     return render(request, 'authapp/profile.html', context)


class ProfileFormView(UpdateView, BaseClassContextMixin, UserDispatchMixin):
    # model = User
    template_name = 'authapp/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('authapp:profile')
    title = 'GeekShop | Профайл'

    # def get_context_data(self, **kwargs):
    #     context = super(ProfileFormView, self).get_context_data()
    #     context['baskets'] = Basket.objects.filter(user=self.request.user)
    #     return context

    def form_valid(self, form):
        messages.set_level(self.request, messages.SUCCESS)
        messages.success(self.request, 'Вы успешно сохранили профиль')
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, queryset=None):
        return User.objects.get(id=self.request.user.pk)

# выйти из аккаунта
# def logout(request):
#     auth.logout(request)
#     return render(request, 'mainapp/index.html')


class Logout(LogoutView):
    template_name = 'mainapp/index.html'