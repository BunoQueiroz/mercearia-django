from  django.shortcuts import redirect, render

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'core/index.html')
