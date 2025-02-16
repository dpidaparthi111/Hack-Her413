from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expenditure', 'Expenditure'),
        ('savings', 'Savings'),
    ]

    type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()  # Automatically set the date/time when created

    def __str__(self):
        return f"{self.type.capitalize()}: {self.amount} on {self.date}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     # Check if this is a new book or an update
    #     is_new = self._state.adding
    #     super().save(*args, **kwargs)  # Save the book first

    #     # Log the book cost as a savings transaction only for new books
    #     if is_new:
    #         self.log_to_savings()

    # def log_to_savings(self):
    #     # Import inside method to prevent circular import issues
    #     from .models import Transaction

    #     # Create a savings transaction associated with the same user
    #     Transaction.objects.create(
    #         user=self.user,  # Associate the transaction with the same user
    #         type="savings",
    #         amount=self.cost,
    #         description=f"Saving for {self.title}",
    #         date=timezone.now(),
    #     )


class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)  # Link to the user
    total_amount= models.DecimalField(max_digits=10, decimal_places=2,default=2)

    def __str__(self):
        return f"Loan - ${self.total_amount}"

class Payment(models.Model):
    loan = models.ForeignKey(Loan, related_name="payments", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"Payment - ${self.amount} on {self.date}"

