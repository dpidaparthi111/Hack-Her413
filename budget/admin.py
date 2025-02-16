from django.contrib import admin
from .models import Transaction, Book, Loan, Payment

# Register your models here.


admin.site.register(Transaction)
admin.site.register(Book)
admin.site.register(Loan)
admin.site.register(Payment)