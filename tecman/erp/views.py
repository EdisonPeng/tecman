# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Account, Transfer, OperatingExpense
from .forms import TransferForm, CreateOperatingExpenseForm


def account_index(request):
    accounts = Account.objects.all()
    context = {'accounts': accounts, }
    return render(request, 'erp/account_index.html', context)


def account_detail(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    context = {'account': account, }
    return render(request, 'erp/account_detail.html', context)


def transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            src_account = form.cleaned_data['src_account']
            dst_account = form.cleaned_data['dst_account']
            amount = form.cleaned_data['amount']
            memo = form.cleaned_data['memo']

            src_account.balance -= amount
            src_account.save()
            dst_account.balance += amount
            dst_account.save()
            txfr = Transfer(src_account=src_account, dst_account=dst_account,
                            amount=amount, memo=memo)
            txfr.save()
            return HttpResponseRedirect(reverse('erp:account_index'))
    else:
        form = TransferForm()
    context = {'form': form, }
    return render(request, 'erp/transfer.html', context)


def operating_expense_index(request):
    operating_expenses = OperatingExpense.objects.all()
    context = {'operating_expenses': operating_expenses, }
    return render(request, 'erp/operating_expense_index.html', context)


def operating_expense_detail(request, operating_expense_id):
    operating_expense = get_object_or_404(OperatingExpense,
                                          pk=operating_expense_id)
    if request.method == 'POST':
        operating_expense.status = 'Done'
        operating_expense.save()
        return HttpResponseRedirect(reverse('erp:operating_expense_detail',
                                            args=(operating_expense_id)))
    context = {'operating_expense': operating_expense, }
    return render(request, 'erp/operating_expense_detail.html', context)


def create_operating_expense(request):
    if request.method == 'POST':
        form = CreateOperatingExpenseForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data['item']
            amount = form.cleaned_data['amount']
            account = form.cleaned_data['account']
            status = form.cleaned_data['status']
            memo = form.cleaned_data['memo']

            account.balance -= amount
            account.save()
            operating_expense = OperatingExpense(item=item,
                                                 amount=amount,
                                                 account=account,
                                                 status=status,
                                                 memo=memo)
            operating_expense.save()
            return HttpResponseRedirect(
                reverse('erp:operating_expense_index'))
    else:
        form = CreateOperatingExpenseForm()
    context = {'form': form, }
    return render(request, 'erp/create_operating_expense.html', context)
