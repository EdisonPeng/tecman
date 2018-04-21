# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Account, Transfer

def account_index(request):
    accounts = Account.objects.all()
    context = {'accounts':accounts,}
    return render(request, 'erp/account_index.html', context)

def account_detail(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    context = {'account': account,}
    return render(request, 'erp/account_detail.html', context)

def transfer(request):
    accounts = Account.objects.all()
    context = {'accounts':accounts,}
    return render(request, 'erp/transfer.html', context)

def execute_transfer(request):
    src_account = get_object_or_404(Account, pk=request.POST['src_account'])
    dst_account = get_object_or_404(Account, pk=request.POST['dst_account'])
    try:
        amount = int(request.POST['amount'])
        if amount == 0:
            raise
    except:
        accounts = Account.objects.all()
        context = {
            'accounts': accounts,
            'error_message': ("%s is not valid." % request.POST['amount'])
        }
        return render(request, 'erp/transfer.html', context)
    if src_account == dst_account:
        accounts = Account.objects.all()
        context = {
            'accounts': accounts,
            'error_message': ("source account is the same with destination account.")
        }
        return render(request, 'erp/transfer.html', context)
    if src_account.balance < amount:
        accounts = Account.objects.all()
        context = {
            'accounts': accounts,
            'error_message': ("balance of source account is not enough.")
        }
        return render(request, 'erp/transfer.html', context)
    src_account.balance -= amount
    src_account.save()
    dst_account.balance += amount
    dst_account.save()
    txfr = Transfer(src_account=src_account, dst_account=dst_account, amount=amount, memo=request.POST['memo'])
    txfr.save()
    return HttpResponseRedirect(reverse('erp:account_index'))
