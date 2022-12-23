from django.shortcuts import render, redirect
from user.models import Purchase, Account
from django.contrib import messages

def my_account(request):
    if request.user.is_authenticated:
        client = request.user
        account = Account.objects.filter(client=client).get()
        client_purchase = Purchase.objects.filter(account=account)
        if account:
            if not client_purchase:
                messages.info(request, 'Você ainda não realizou nenhuma compra conosco')
            context = {'purchases': client_purchase}
            return render(request, 'user/my_account.html', context)
        return redirect('dashboard')
    return redirect('dashboard')
