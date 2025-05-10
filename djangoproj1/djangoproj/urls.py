from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', index, name='index'),

    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('catalog/add/', ProductCreateView.as_view(), name='add_product'),
    path('catalog/<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/<int:id>/edit/', ProductUpdateView.as_view(), name='edit_product'),
    path('products/<int:id>/physical-delete/', ProductPhysicalDeleteView.as_view(), name='physical_delete_product'),
    path('products/manage/', ProductManageListView.as_view(), name='product_manage'),
    path('products/<int:id>/delete/', ProductLogicalDeleteView.as_view(), name='logical_delete_product'),
    path('products/<int:id>/restore/', ProductRestoreView.as_view(), name='restore_product'),

    path('categories/', CategoryListView.as_view(),   name='categories'),
    path('categories/add/', CategoryCreateView.as_view(), name='add_category'),
    path('categories/<int:category_id>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:category_id>/edit/', CategoryUpdateView.as_view(), name='edit_category'),
    path('categories/<int:category_id>/delete/', CategoryDeleteView.as_view(), name='delete_category'),

    path('contacts/', contacts, name='contacts'),
    path('profile/', profile, name='profile'),
    path('cart/', cart_view, name='cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', clear_cart, name='clear_cart'),
    path('checkout/', checkout, name='checkout'),
    path('orders/', order_list, name='order_list'),


    path('tags/', TagListView.as_view(),   name='tags'),
    path('tags/add/', TagCreateView.as_view(), name='add_tag'),
    path('tags/<int:tag_id>/', TagDetailView.as_view(), name='tag_detail'),
    path('tags/<int:tag_id>/edit/', TagUpdateView.as_view(), name='edit_tag'),
    path('tags/<int:tag_id>/delete/', TagDeleteView.as_view(), name='delete_tag'),


    path('login/', login_user, name='login_page'),
    path('registration/', registration_user, name='registration_page'),
    path('logout/', logout_user, name='logout_page'),
]