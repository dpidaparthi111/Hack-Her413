# Create your views here.
from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegisterForm, TransactionForm,BookForm
from .models import Transaction,Book,Loan, Payment
import json


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect("home")  # Redirect to home page
    else:
        form = RegisterForm()
    
    return render(request, "registration/register.html", {"form": form})

@login_required(login_url='/accounts/login/')  # Redirects unauthenticated users
def home_view(request):
    return render(request, 'budget/homepage.html')  # Load the home template

def account_view(request):
    return render(request, 'budget/account.html')

def finances_view(request):
    #transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    #return render(request, 'budget/transactions.html', {'transactions': transactions})
    return render(request, 'budget/finances.html')

def books_view(request):
    return render(request, 'budget/books.html')

def student_loans_view(request):
    return render(request, 'budget/student_loans.html')

#transactions page views-
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()  # Save the transaction to the database
            return redirect('transactions')  # Redirect to the transactions list page
    else:
        form = TransactionForm()

    return render(request, 'budget/add_transaction.html', {'form': form})

def transactions_view(request):
    transaction_type = request.GET.get('type')  # Get the type from the query parameters
    if transaction_type:
        transactions = Transaction.objects.filter(type=transaction_type).order_by('-date')
    else:
        transactions = Transaction.objects.all().order_by('-date')
    context = {
        'transactions': transactions,
    }

    return render(request, 'budget/transactions.html', context)

#books page views-
def books(request):
    if request.method == 'POST':
        # Handle form submission
        titles = request.POST.getlist('title')
        costs = request.POST.getlist('cost')

        for title, cost in zip(titles, costs):
            if title and cost:  # Ensure fields are not empty
                Book.objects.create(
                    user=request.user,
                    title=title,
                    cost=cost,
                )

        return redirect('books')
    else:
        # Fetch books for the logged-in user
        books = Book.objects.filter(user=request.user)
        return render(request, 'budget/books.html', {'books': books})

def book_list(request):
    books = Book.objects.all()
    return render(request, "budget/books.html", {"books": books})

def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        cost = request.POST.get("cost")

        # Debugging: Print received data
        print("Received title:", title)
        print("Received cost:", cost)

        if title and cost:
            try:
                book = Book.objects.create(title=title, cost=cost)
                print("Book saved successfully:", book)  # Debugging message
                return redirect("books")  # Redirect to refresh the page
            except Exception as e:
                print("Error saving book:", e)  # Debugging message
                return HttpResponse("Error saving book", status=500)
        
        print("Missing title or cost")
        return HttpResponse("Missing title or cost", status=400)

    return HttpResponse("Invalid request", status=400)

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, user=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, user=request.user)
    if request.method == 'POST':
        book.delete()
        return redirect('books')
    return render(request, 'confirm_delete.html', {'book': book})

#student loans page views-
def student_loans(request):
    loan = Loan.objects.first()  # Get the first loan record
    payments = loan.payments.all() if loan else []

    if loan:
        # Prepare data for the chart
        payment_dates = [payment.date.strftime("%Y-%m-%d") for payment in payments]
        loan_balances = [
            loan.total_amount - sum(p.amount for p in payments[:i+1])
            for i in range(len(payments))
        ]
    else:
        payment_dates = []
        loan_balances = []

    return render(request, "budget/student_loans.html", {
        "loan": loan,
        "payment_dates": json.dumps(payment_dates),
        "loan_balances": json.dumps(loan_balances),
    })


def set_loan_amount(request):
    if request.method == "POST":
        amount = request.POST.get("loan_amount")

        # Ensure a loan entry exists
        loan, created = Loan.objects.get_or_create()
        loan.total_amount = float(amount)  # Convert to float before saving
        loan.save()

    return redirect("student_loans")


def add_payment(request):
    if request.method == "POST":
        amount = request.POST.get("payment_amount")
        date = request.POST.get("payment_date")

        loan = Loan.objects.first()  # Ensure a loan exists before adding payments
        if loan:
            Payment.objects.create(loan=loan, amount=float(amount), date=date)
        else:
            print("No loan exists. Cannot add payment.")  # Debugging message

    return redirect("student_loans")
