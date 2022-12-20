from django.shortcuts import render, redirect

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'user/profile.html')
    return redirect('home')

def update_profile(request):
    return render(request, 'user/profile.html')
