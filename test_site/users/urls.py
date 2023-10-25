from django.urls import path
from . import views as users
app_name = "users"
urlpatterns = [
    path("login/", users.login_user, name='login'),
    path("logout/", users.logout_user, name="logout"),
]
