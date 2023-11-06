from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views as users
app_name = "users"
urlpatterns = [
    path("login/", users.login_user, name='login'),
    path('logout/', users.logout_user, name='logout'),
    path('register/', users.register, name='register'),
    path('register_done/', users.register_done, name='register_done'),
]
