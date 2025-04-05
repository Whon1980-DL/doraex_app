from . import views
from django.urls import path

urlpatterns = [
    path('', views.GadgetList.as_view(), name='home'),
    path('cart/', views.cart, name='cart'),
    path('cart/edit_renting/<int:renting_id>', views.renting_edit_form, name='renting_edit_form'),
    path('cart/confirm_renting/<int:renting_id>', views.renting_confirm, name='renting_confirm'),
    path('renting_form/<slug:slug>', views.renting_form, name='renting_form'),
    path('customer_profile/', views.customer_profile, name='customer_profile'),
    path('category/<str:dl>', views.category, name='category'),
    path('<slug:slug>/', views.gadget_view, name='gadget_view'), 
]