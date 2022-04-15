from django.shortcuts import render
from authapp.models import User
from django.contrib.auth.decorators import user_passes_test
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductCatAdminCreateForm, ProdAdminCreateForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from mainapp.models import ProductCategory, Product
from django.contrib import messages
from django.views.generic import ListView, UpdateView, DeleteView, TemplateView, CreateView
from django.utils.decorators import method_decorator
from adminapp.mixins import BaseClassContextMixin, CustomDispatchMixin
from django.urls import reverse_lazy


# @user_passes_test(lambda u: u.is_superuser)
# def index(request):
#     return render(request, 'adminapp/admin.html')


class IndexTemplateView(TemplateView, BaseClassContextMixin, CustomDispatchMixin):
    template_name = 'adminapp/admin.html'
    title = 'Главная страница'
    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # def dispatch(self, request, *args, **kwargs):
    #     super(IndexTemplateView, self).dispatch(request, *args, **kwargs)


class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    title = 'Админка | Пользователи'
    context_object_name = 'users'



# @user_passes_test(lambda u: u.is_superuser)
# def admin_users(request):
#     context = {
#         'title': 'Админка | Пользователи',
#         'users': User.objects.all()
#     }
#     return render(request, 'adminapp/admin-users-read.html', context)


class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    title = 'Админка | Регистрация'
    success_url = reverse_lazy('adminapp:admin_users')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_create(request):
#
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminRegisterForm()
#     context = {
#         'title': 'Админка | Регистрация',
#         'form': form
#     }
#     return render(request, 'adminapp/admin-users-create.html', context)

class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    title = 'Админка | Обновление пользователя'
    success_url = reverse_lazy('adminapp:admin_users')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_update(request, id):
#     user_select = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminProfileForm(instance=user_select)
#
#     context = {
#         'title': 'Админка | Обновление пользователя',
#         'form': form,
#         'user_select': user_select
#     }
#
#     return render(request, 'adminapp/admin-users-update-delete.html', context)


class UserDeleteView(DeleteView, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    title = 'Админка | Обновление пользователя'
    success_url = reverse_lazy('adminapp:admin_users')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_delete(request, id):
#     user = User.objects.get(id=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('adminapp:admin_users'))


class ProductCategoriesListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'adminapp/admin-product-categories-read.html'
    title = 'Geekshop | Категории товаров'
    context_object_name = 'categories'


#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_categories(request):
#     context = {
#         'title': 'Geekshop | Категории товаров',
#         'categories': ProductCategory.objects.all()
#     }
#     return render(request, 'adminapp/admin-product-categories-read.html', context)

class ProductCategoriesCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'adminapp/admin-product-categories-create.html'
    form_class = ProductCatAdminCreateForm
    title = 'Админка | Создание категорий продуктов'
    success_url = reverse_lazy('adminapp:admin_product_categories')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_categories_create(request):
#     if request.method == 'POST':
#         form = ProductCatAdminCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_product_categories'))
#         else:
#             print(form.errors)
#     else:
#         form = ProductCatAdminCreateForm()
#     context = {
#         'title': 'Админка | Создание категорий продуктов',
#         'form': form
#     }
#     return render(request, 'adminapp/admin-product-categories-create.html', context)


class ProductCategoriesUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'adminapp/admin-product-categories-update-delete.html'
    form_class = ProductCatAdminCreateForm
    title = 'Админка | Обновление категорий продуктов'
    success_url = reverse_lazy('adminapp:admin_product_categories')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_categories_update(request, id):
#     product_cat_select = ProductCategory.objects.get(id=id)
#     if request.method == 'POST':
#         form = ProductCatAdminCreateForm(instance=product_cat_select, data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегистрирвались')
#             return HttpResponseRedirect(reverse('adminapp:admin_product_categories'))
#         else:
#             print(form.errors)
#     else:
#         form = ProductCatAdminCreateForm(instance=product_cat_select)
#     context = {
#         'title': 'Админка | Обновление категорий продуктов',
#         'form': form,
#         'product_cat_select': product_cat_select
#     }
#     return render(request, 'adminapp/admin-product-categories-update-delete.html', context)


class ProductCategoriesDeleteView(DeleteView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'adminapp/admin-product-categories-update-delete.html'
    form_class = ProductCatAdminCreateForm
    title = 'Админка | Обновление пользователя'
    success_url = reverse_lazy('adminapp:admin_product_categories')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_categories_delete(request, id):
#     product_cat_select = ProductCategory.objects.get(id=id)
#     product_cat_select.is_active = False
#     product_cat_select.save()
#     return HttpResponseRedirect(reverse('adminapp:admin_product_categories'))


class ProductsListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-read.html'
    title = 'Geekshop | Товары'
    context_object_name = 'products'


# @user_passes_test(lambda u: u.is_superuser)
# def admin_products(request):
#     content = {'title': 'Geekshop | Товары',
#                'products': Product.objects.all()
#                }
#     return render(request, 'adminapp/admin-products-read.html', content)


class ProductsCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-create.html'
    form_class = ProdAdminCreateForm
    title = 'Админка | Создание продукта'
    success_url = reverse_lazy('adminapp:admin_products')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_create(request):
#     if request.method == 'POST':
#         form = ProdAdminCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_products'))
#
#         else:
#             print(form.errors)
#     else:
#         form = ProdAdminCreateForm()
#     content = {'title': 'Администратор | Создание продукта',
#                'form': form}
#     return render(request, 'adminapp/admin-products-create.html', content)


class ProductsUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    form_class = ProdAdminCreateForm
    title = 'Админка | Редактирование товара'
    success_url = reverse_lazy('adminapp:admin_products')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_update(request, id):
#     prod_select = Product.objects.get(id=id)
#     if request.method == 'POST':
#         form = ProdAdminCreateForm(instance=prod_select, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно изменили продукт')
#             return HttpResponseRedirect(reverse('adminapp:admin_products'))
#         else:
#             print(form.errors)
#     else:
#         form = ProdAdminCreateForm(instance=prod_select)
#     content = {'title': 'Администратор | Редактирование товара',
#                'form': form,
#                'prod_select': prod_select}
#     return render(request, 'adminapp/admin-products-update-delete.html', content)


class ProductsDeleteView(DeleteView, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    form_class = ProdAdminCreateForm
    title = 'Админка | Обновление пользователя'
    success_url = reverse_lazy('adminapp:admin_products')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_delete(request, id):
#     Product.objects.get(id=id).delete()
#     return HttpResponseRedirect(reverse('adminapp:admin_products'))