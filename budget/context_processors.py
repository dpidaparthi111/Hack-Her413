from .models import Transaction, Book

def latest_transactions(request):
    # Fetch the latest expense, income, and savings transactions
    latest_expense = Transaction.objects.filter(type='expenditure').order_by('-date').first()
    latest_income = Transaction.objects.filter(type='income').order_by('-date').first()
    latest_savings = Transaction.objects.filter(type='savings').order_by('-date').first()

    # Fetch the 2 latest books
    latest_books = Book.objects.all().order_by('-id')[:2]  # Get the 2 most recently added books

    # Return the latest values
    return {
        'latest_expense': latest_expense,
        'latest_income': latest_income,
        'latest_savings': latest_savings,
        'latest_books': latest_books,  # Add the latest books to the context
    }