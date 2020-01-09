from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.contrib import messages
import random
from twilio.rest import Client
from .models import SignupOtp, User


# Function for sending OTP to User for account verification

def send_otp(first_name, otp, phone):
    # Your Account SID from twilio.com/console
    account_sid = "ACc6ab1f8b3e6129e436379bde7de47862"
    # Your Auth Token from twilio.com/console
    auth_token = "acf9ff16b50a76b9c574e006e7262645"

    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            to="+91"+phone,
            from_="+15132530921",
            body="Hello "+first_name+"! Your account activation OTP is: "+otp)
        return True
    except:
        return False


def send_reset_otp(first_name, otp, phone):
    # Your Account SID from twilio.com/console
    account_sid = "ACc6ab1f8b3e6129e436379bde7de47862"
    # Your Auth Token from twilio.com/console
    auth_token = "acf9ff16b50a76b9c574e006e7262645"

    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            to="+91"+phone,
            from_="+15132530921",
            body="Hello "+first_name+"! Your account password reset OTP is: "+otp)
        return True
    except:
        return False


# index page
def index(request):
    return render(request, 'index.html', {})


# view to signup
def signup(request):
    if request.method == "POST":
        try:
            user_exists = User.objects.get(phone=request.POST.get('phone'))
            if user_exists:
                messages.error(request, "Sorry, User with this phone is already exists.")
                return redirect('sign-up')
        except:
            signup_form = SignUpForm(data=request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                otp = ''.join(random.choice('0123456789') for _ in range(6)) # generate OTP of 6 digits
                SignupOtp.objects.create(user=user, otp=otp) # creating random OTP
                is_otp_send = send_otp(request.POST.get('first_name'), otp, request.POST.get('phone'))
                return render(request, 'otp_verification.html', {"user_id":user.pk})
    return render(request, 'signup.html', {})


# signing user module
def signin(request):
    if request.method == "POST":
        try:
            is_user_active = User.objects.get(phone=request.POST.get('phone'))
        except:
            messages.error(request, "Sorry, wrong credentials!")
            return redirect('sign-in')
        if is_user_active.is_active:
            user = authenticate(request, username=request.POST.get('phone'), password=request.POST.get('password'))
            if user:
                login(request, user)
                return render(request, 'index.html', {})
            else:
                messages.success(request, "Sorry wrong credentials :)")
                return render(request, 'login.html', {})
        else:
            messages.success(request, "Sorry, your account is not verified :)")
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})


@login_required(login_url="sign-in")
def signout(request):
    logout(request)
    return redirect('index')


# Verify Otp sent to user mobile
def phone_verification(request):
    user_id = request.POST.get('user_id')
    otp = request.POST.get('otp')
    user = User.objects.get(id=user_id)
    saved_otp = SignupOtp.objects.filter(user=user_id).order_by('-created')[0]
    print(saved_otp)
    if saved_otp.attempt == 3:
        messages.error(request, "Sorry, You have exceeds 3 attempt.")
        return render(request, 'signup.html', {})
    saved_otp.attempt = saved_otp.attempt+1
    saved_otp.save()

    if str(saved_otp.otp) == str(otp):
        user.is_active = True # set user active
        user.save()
        SignupOtp.objects.get(user=user_id).delete()
        login(request, user) # starting session for the user
        messages.success(request, "Account Activated Successfully :)")
        return render(request, 'index.html', {"user_id": user.pk})
    messages.error(request, "Sorry, Wrong OTP :(")
    return render(request, 'otp_verification.html', {"user_id": user.pk})


# forgot password module
def forgot_password(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        try:
            user = User.objects.get(phone=phone)
            otp = ''.join(random.choice('0123456789') for _ in range(6))  # generate OTP of 6 digits
            SignupOtp.objects.create(user=user, otp=otp)  # creating random OTP
            is_otp_send = send_reset_otp(user.first_name, otp, request.POST.get('phone'))
            return render(request, 'pass_reset_otp.html', {"user_id":user.pk})
        except:
            messages.error(request, "Sorry, no user exists with such phone. Have you registered already?")
            return render(request, 'login.html', {})

    return render(request, 'reset_password.html', {})


# function to verify password reset OTP
def password_reset_otp(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        otp = request.POST.get('otp')
        user = User.objects.get(id=user_id)
        saved_otp = SignupOtp.objects.filter(user=user_id).order_by('-created')[0]
        if saved_otp.attempt >= 3:
            messages.error(request, "Sorry, You have exceeds 3 attempt. Signup with correct details.")
            return render(request, 'signup.html', {})
        saved_otp.attempt = saved_otp.attempt + 1
        saved_otp.save()

        if str(saved_otp.otp) == str(otp):
            SignupOtp.objects.filter(user=user_id).order_by('-created')[0].delete()
            return render(request, 'new_password.html', {"user_id": user.pk})
        else:
            messages.error(request, "Sorry, wrong OTP. Try again!")
            return render(request, 'pass_reset_otp.html', {"user_id": user.pk})
    return redirect('/')


# change password after OTP verification
def set_new_password(request):
    try:
        user = User.objects.get(id=request.POST.get('user_id'))
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 == pass2:
            user.set_password(pass1)
            user.save()
            messages.success(request, "New password has been set. Login Now. ")
            return redirect('sign-in')
    except:
        messages.error(request, "Seems invalid user")
        return redirect('sign-in')
