from django.urls import path
from .views import CartView, HomePageView, AboutPageView, ContactPageView, ProductIndexView, ProductShowView,ProductCreateView, EasterEggView,CartRemoveAllView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='products'),
    path('products/create/', ProductCreateView.as_view(), name='create'),
    path('products/<str:id>/', ProductShowView.as_view(), name='product'),
    path('eegg/', EasterEggView.as_view(), name='eegg'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),

]
