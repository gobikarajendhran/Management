from django.contrib import admin
from .models import *
for m in [Customer,Supplier,Category,Product,Sale,Purchase,Expense,Petrol,Allowance,Salary,Partner,CashTransaction,BankTransaction,GeneralTransaction,AuditLog]: admin.site.register(m)
