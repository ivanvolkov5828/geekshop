from django.urls import path
from adminapp.views import IndexTemplateView, UserListView, UserCreateView, UserDeleteView, UserUpdateView, \
    ProductCategoriesListView, ProductCategoriesCreateView, ProductCategoriesUpdateView, \
    ProductCategoriesDeleteView, ProductsListView, ProductsCreateView, ProductsUpdateView, ProductsDeleteView

app_name = 'adminapp'
urlpatterns = [

    # Пользователи
    path('', IndexTemplateView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('user-create/', UserCreateView.as_view(), name='admin_user_create'),
    path('user-update/<int:pk>/', UserUpdateView.as_view(), name='admin_user_update'),
    path('user-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_user_delete'),

    # Категории
    path('product-categories/', ProductCategoriesListView.as_view(), name='admin_product_categories'),
    path('product-categories-create/', ProductCategoriesCreateView.as_view(), name='admin_product_categories_create'),
    path('product-categories-update/<int:pk>/', ProductCategoriesUpdateView.as_view(),
         name='admin_product_categories_update'),
    path('product-categories-delete/<int:pk>/', ProductCategoriesDeleteView.as_view(),
         name='admin_product_categories_delete'),

    # Товары
    path('product/', ProductsListView.as_view(), name='admin_products'),
    path('product-create/', ProductsCreateView.as_view(), name='admin_products_create'),
    path('product-update/<int:pk>/', ProductsUpdateView.as_view(), name='admin_products_update'),
    path('product-delete/<int:pk>/', ProductsDeleteView.as_view(), name='admin_products_delete')
]
