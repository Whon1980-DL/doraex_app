from . import views
from django.urls import path

urlpatterns = [
    path('', views.GadgetList.as_view(), name='home'),
    path('cart/', views.cart, name='cart'),
    path('renting_form/<slug:slug>', views.renting_form, name='renting_form'),
    path('customer_profile/', views.customer_profile, name='customer_profile'),
    path('category/<str:dl>', views.category, name='category'),
    path('<slug:slug>/', views.gadget_view, name='gadget_view'), 
]