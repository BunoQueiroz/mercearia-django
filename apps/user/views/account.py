from django.shortcuts import render, redirect, get_list_or_404
from user.models import Purchase, Account
from django.contrib import messages

def my_account(request):
    if request.user.is_authenticated:
        return my_account_or_404(request)
    return redirect('dashboard')

def render_client_purchase(request, client_purchase):
    if not client_purchase:
        messages.info(request, 'Você ainda não realizou compra(s) conosco')
        return render(request, 'user/my_account.html')
    total = final_value(client_purchase)
    context = {'purchases': client_purchase, 'total': total}
    return render(request, 'user/my_account.html', context)

def my_account_or_404(request):
    account = get_list_or_404(Account, client=request.user)[0]
    client_purchase = Purchase.objects.filter(account=account)
    return render_client_purchase(request, client_purchase)

def final_value(client_purchase):
    result = 0
    for purchase in client_purchase:
        result += purchase.total()
    return result
