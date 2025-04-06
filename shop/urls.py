from . import views
from django.urls import path

urlpatterns = [
    path('', views.GadgetList.as_view(), name='home'),
    path('customer_profile_registration/', views.customer_profile_registration, name='customer_profile_registration'),
    path('cart/', views.cart, name='cart'),
    path('cart/edit_renting/<int:renting_id>', views.renting_edit_form, name='renting_edit_form'),
    path('cart/confirm_renting/<int:renting_id>', views.renting_confirm, name='renting_confirm'),
    path('cart/delete_renting/<int:renting_id>', views.renting_delete, name='renting_delete'),
    path('renting_form/<slug:slug>', views.renting_form, name='renting_form'),
    path('customer_profile/', views.customer_profile, name='customer_profile'),
    path('customer_profile/edit_profile/>', views.profile_edit_form, name='profile_edit_form'),
    path('category/<str:dl>', views.category, name='category'),
    path('<slug:slug>/', views.gadget_view, name='gadget_view'),
]