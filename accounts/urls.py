from django.urls import path
from . import views


# urlpatterns below

urlpatterns = [
    #Auth routes
    path("login/", views.login_view, name="login_view"),
    path("logout/", views.logout_view, name="logout_view"),
    path("register/", views.register, name="register"),
    #Other routes
    path("", views.home, name="home"),
    #path("profile/", views.profile_view, name="profile"),
]
