from django.shortcuts import render,redirect

from django.http import HttpResponse

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from myApp.models import *


def homePage(req):

    return render(req,'index.html')

def registerPage(req):

    if req.method == 'POST':
        user_name = req.POST.get('username')
        firstName = req.POST.get('firstName')
        lastName = req.POST.get('lastName')
        email = req.POST.get('email')
        userType = req.POST.get('userType')
        password = req.POST.get('password')
        confirmPassword = req.POST.get('confirmPassword')

        if all([user_name, firstName, lastName, email, userType, password, confirmPassword]):
            
            if not User_Model.objects.filter(username = user_name).exists():
                if password == confirmPassword:
                    user = User_Model.objects.create_user(
                        username = user_name,
                        first_name = firstName,
                        last_name = lastName,
                        email = email, 
                        user_type = userType,
                        password = confirmPassword
                    )
                    messages.success(req, 'Registration Successful!')
                    return redirect('loginPage')

                else:
                    messages.warning(req, 'Password not match!')
                    return redirect('registerPage')  

            else:
                messages.warning(req, 'This username already exists!')
                return redirect('registerPage')  

        else:
            messages.warning(req,'All fields are required!')
            return redirect('registerPage')  


    return render(req, 'register.html')

def loginPage(req):

    if req.method == 'POST':
        
        user_name = req.POST.get('username')
        password = req.POST.get('password')

        if all([user_name, password]):
            user = authenticate(username = user_name, password = password)

            if user is not None:
                login(req, user)
                return redirect('homePage')

            else:
                messages.warning(req, 'Username or Password is not Correct!') 
                return redirect('loginPage')

        else:
            messages.warning(req, 'All fields are required!')
            return redirect('loginPage')

    return render(req, 'login.html')