# Generated by Django 5.1.6 on 2025-02-16 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_loan_payment_delete_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenditure',
            name='category',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='category',
        ),
        migrations.RemoveField(
            model_name='expenditure',
            name='user',
        ),
        migrations.RemoveField(
            model_name='finances',
            name='user',
        ),
        migrations.RemoveField(
            model_name='savings',
            name='user',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Expenditure',
        ),
        migrations.DeleteModel(
            name='Finances',
        ),
        migrations.DeleteModel(
            name='Savings',
        ),
    ]
