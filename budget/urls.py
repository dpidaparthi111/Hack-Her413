from django.urls import path
from . import views

urlpatterns = [
    #path('login/',views.register_view,name='register'), #registration page
    path('', views.home_view, name='homepage'), # Default home page

    #navigation bar views-
    path('account/', views.account_view, name='account'),
    path('student_loans/', views.student_loans_view, name='student_loans'),

    #finances page views-
    path('add-transaction/', views.add_transaction, name='add_transaction'),
    path('transactions/', views.transactions_view, name='transactions'),

    #books page views-
    path("books/", views.book_list, name="books"),
    path("add_book/", views.add_book, name="add_book"),
    path('books_table/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books_table/delete/<int:book_id>/', views.delete_book, name='delete_book'),

    #student loans page views-
    path("student_loans/", views.student_loans, name="student_loans"),
    path("set_loan_amount/", views.set_loan_amount, name="set_loan_amount"),
    path("add_payment/", views.add_payment, name="add_payment"),

]
