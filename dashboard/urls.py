from django.urls import path
from . import views


urlpatterns = [
    path('',views.loginAdmin,name='admin-login'),
    path('home',views.home,name='admin-home'),
    path('add-user',views.addUser,name='add-user'),
    path('delete-user/<str:pkey>',views.delete,name='delete'),
    path('update-user/<str:pkey>',views.update,name='update'),
    path('logout',views.logout,name='admin-logout'),
]