from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('add_vendor/', add_vendor, name='add_vendor'),
    path('vendor_login/', vendor_login, name='vendor_login'),
    path('vendor_logout/', vendor_logout, name='vendor_logout'),
    path('vendor_list/', vendor_list, name='vendor_list'),
    path('add_products/', add_products, name='add_products'),
    path('product/<int:product_id>/', comment_rating, name='product_detail'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/remove/<int:item_id>', remove_from_cart,name='remove_from_cart' ),
    path('cart/update/<int:item_id>', update_cart, name='update_cart'),
    path('cart/update_add/<int:item_id>' , update_add_cart, name='update_add_cart'),
    path('profile/', profile_view, name='profile'),
    path('payment/', payment_view, name='payment'),
    path('payment-success/', payment_success_view, name='payment_success'),
    path('payment-failed/', payment_failed_view, name='payment_failed'),
    path('search/', search, name='search')
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
