from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book, Transaction,Loan,Payment

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['type', 'amount', 'description', 'date']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'cost']

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['total_amount']  # Only setting the loan amount

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'date'] 
       


        