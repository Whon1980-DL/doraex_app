from . import views
from django.urls import path

urlpatterns = [
    path('', views.GadgetList.as_view(), name='home'),
    path('category/<str:dl>', views.category, name='category')
]