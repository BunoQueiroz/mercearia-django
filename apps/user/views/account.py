from django.shortcuts import render, redirect
from user.models import Purchase, Account
from django.contrib import messages

def my_account(request):
    if request.user.is_authenticated:
        return my_account_or_404(request)
    return redirect('dashboard')

def get_account_or_404(request):
    client = request.user
    account = Account.objects.filter(client=client)
    if account.exists():
        return account.get()
    return None

def get_purchase_or_404(account):
    client_purchase = Purchase.objects.filter(account=account)
    if not client_purchase:
        return None
    return client_purchase

def render_client_purchase(request, client_purchase):
    if client_purchase is None:
        return message_info_and_redirect(request, 'dashboard', 'Você ainda não realizou compra conosco')
    total = final_value(client_purchase)
    context = {'purchases': client_purchase, 'total': total}
    return render(request, 'user/my_account.html', context)

def my_account_or_404(request):
    account = get_account_or_404(request)
    if account:
        client_purchase = get_purchase_or_404(account)
        return render_client_purchase(request, client_purchase)
    return message_info_and_redirect(request, 'dashboard', 'Você ainda não possui conta')

def message_info_and_redirect(request, to_url, message):
    messages.info(request, message)
    return redirect(to_url)

def final_value(client_purchase):
    result = 0
    for purchase in client_purchase:
        result += purchase.total()
    return result
