from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is already taken")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is already taken")
                return redirect('signup')
            else:
                user_reg=User.objects.create_user(username=username, email=email, password=password)
                user_reg.save()
                messages.info(request, "Successfully Created")
                return redirect('signup')
            
        else:
            messages.info(request, "Password doesn't match")
            return redirect('signup')

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request, "Logged in successfully")
            return redirect('/')
        else:
            return redirect('signup')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out")
    return redirect('/')