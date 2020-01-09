from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup, name="sign-up"),
    path("signin", views.signin, name="sign-in"),
    path("otp-verification", views.phone_verification, name="phone-verification"),
    path("logout", views.signout, name="sign-out"),
    path("forgot-password", views.forgot_password, name="forgot-password"),
    path("reset-password", views.password_reset_otp, name="reset-password"),
    path("set-password", views.set_new_password, name="set-password"),
]