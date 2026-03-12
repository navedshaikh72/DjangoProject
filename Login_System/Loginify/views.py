from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import UserDetails

def hello_world(request):
    return HttpResponse("Hello, world!")

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if UserDetails.objects.filter(username=username).exists():
            return render(request, 'Loginify/signup.html', 
                         {'error': 'Username already exists'})
        
        if UserDetails.objects.filter(email=email).exists():
            return render(request, 'Loginify/signup.html', 
                         {'error': 'Email already exists'})
        
        UserDetails.objects.create(username=username, email=email, password=password)
        return redirect('login')
    
    return render(request, 'Loginify/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = UserDetails.objects.get(email=email)
            if user.password == password:
                return render(request, 'Loginify/success.html', 
                             {'username': user.username})
            else:
                return render(request, 'Loginify/login.html', 
                             {'error': 'Invalid password'})
        except UserDetails.DoesNotExist:
            return render(request, 'Loginify/login.html', 
                         {'error': 'User not found'})
    
    return render(request, 'Loginify/login.html')

def get_all_users(request):
    users = UserDetails.objects.all()
    user_list = [{'username': u.username, 'email': u.email} for u in users]
    return render(request, 'Loginify/all_users.html', {'users': user_list})

def get_user_by_email(request, email):
    try:
        user = UserDetails.objects.get(email=email)
        return render(request, 'Loginify/user_detail.html', 
                     {'user': {'username': user.username, 'email': user.email}})
    except UserDetails.DoesNotExist:
        return HttpResponse("User not found", status=404)

def update_user(request, username):
    try:
        user = UserDetails.objects.get(username=username)
        if request.method == 'POST':
            user.email = request.POST.get('email', user.email)
            user.password = request.POST.get('password', user.password)
            user.save()
            return render(request, 'Loginify/success.html', 
                         {'username': user.username})
        
        return render(request, 'Loginify/update_user.html', 
                     {'user': user})
    except UserDetails.DoesNotExist:
        return HttpResponse("User not found", status=404)

def delete_user(request, email):
    try:
        user = UserDetails.objects.get(email=email)
        user.delete()
        return HttpResponse("User deleted successfully")
    except UserDetails.DoesNotExist:
        return HttpResponse("User not found", status=404)