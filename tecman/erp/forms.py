from django import forms
from .models import Transfer, OperatingExpense

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ['src_account', 'dst_account', 'amount', 'memo']

    def clean_amount(self):
        data = self.cleaned_data['amount']
        if data <= 0:
            raise forms.ValidationError("%s is invalid amount." % data)
        return data

    def clean(self):
        cleaned_data = super(TransferForm, self).clean()
        src_account = cleaned_data.get("src_account")
        dst_account = cleaned_data.get("dst_account")
        amount = cleaned_data.get("amount")
        if src_account == dst_account:
            raise forms.ValidationError("Src. account is equal to Dst. account.")
        if src_account.balance < amount:
            raise forms.ValidationError("The balance of Src. account is not enough.")


class CreateOperatingExpenseForm(forms.ModelForm):
    class Meta:
        model = OperatingExpense
        fields = ['item', 'amount', 'account', 'status', 'memo']

    def clean_amount(self):
        data = self.cleaned_data['amount']
        if data <= 0:
            raise forms.ValidationError("%s is invalid amount." % data)
        return data

    def clean(self):
        cleaned_data = super(CreateOperatingExpenseForm, self).clean()
        account = cleaned_data.get("account")
        amount = cleaned_data.get("amount")
        if account.balance < amount:
            raise forms.ValidationError("The balance of account is not enough.")
