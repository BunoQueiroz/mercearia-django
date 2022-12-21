from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'core/index.html')
