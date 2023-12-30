from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('update.html/<int:id>', views.update_coffee),
    path('add.html', views.add_coffee),
    path('coffees', views.CoffeeCRUD.as_view()),
    path('coffees/<int:id>', views.CoffeeCRUD.as_view())
]