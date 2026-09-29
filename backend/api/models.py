from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True); is_deleted=models.BooleanField(default=False)
    class Meta: abstract=True

class Customer(Base):
    name=models.CharField(max_length=150); business_name=models.CharField(max_length=180,blank=True); phone=models.CharField(max_length=40,blank=True); email=models.EmailField(blank=True); address=models.TextField(blank=True); notes=models.TextField(blank=True)
class Supplier(Base):
    name=models.CharField(max_length=150); business_name=models.CharField(max_length=180,blank=True); phone=models.CharField(max_length=40,blank=True); email=models.EmailField(blank=True); address=models.TextField(blank=True); notes=models.TextField(blank=True)
class Category(Base): name=models.CharField(max_length=100,unique=True)
class Product(Base):
    name=models.CharField(max_length=180); code=models.CharField(max_length=80,blank=True); category=models.ForeignKey(Category,null=True,blank=True,on_delete=models.SET_NULL); supplier=models.ForeignKey(Supplier,null=True,blank=True,on_delete=models.SET_NULL); purchase_price=models.DecimalField(max_digits=14,decimal_places=2,default=0); selling_price=models.DecimalField(max_digits=14,decimal_places=2,default=0); opening_stock=models.DecimalField(max_digits=14,decimal_places=3,default=0); stock_added=models.DecimalField(max_digits=14,decimal_places=3,default=0); stock_sold=models.DecimalField(max_digits=14,decimal_places=3,default=0); adjustment=models.DecimalField(max_digits=14,decimal_places=3,default=0); minimum_stock=models.DecimalField(max_digits=14,decimal_places=3,default=0); unit=models.CharField(max_length=30,default='pcs'); notes=models.TextField(blank=True)
    @property
    def current_stock(self): return self.opening_stock+self.stock_added-self.stock_sold+self.adjustment
    @property
    def stock_value(self): return self.current_stock*self.purchase_price
class Sale(Base):
    date=models.DateField(); customer=models.ForeignKey(Customer,null=True,blank=True,on_delete=models.SET_NULL); product=models.ForeignKey(Product,null=True,blank=True,on_delete=models.SET_NULL); quantity=models.DecimalField(max_digits=14,decimal_places=3,default=1); selling_price=models.DecimalField(max_digits=14,decimal_places=2,default=0); amount_received=models.DecimalField(max_digits=14,decimal_places=2,default=0); payment_mode=models.CharField(max_length=40,default='Cash'); reference=models.CharField(max_length=100,blank=True); notes=models.TextField(blank=True)
    @property
    def total_amount(self): return self.quantity*self.selling_price
    @property
    def pending_amount(self): return self.total_amount-self.amount_received
class Purchase(Base):
    date=models.DateField(); supplier=models.ForeignKey(Supplier,null=True,blank=True,on_delete=models.SET_NULL); product=models.ForeignKey(Product,null=True,blank=True,on_delete=models.SET_NULL); quantity=models.DecimalField(max_digits=14,decimal_places=3,default=1); purchase_price=models.DecimalField(max_digits=14,decimal_places=2,default=0); amount_paid=models.DecimalField(max_digits=14,decimal_places=2,default=0); payment_mode=models.CharField(max_length=40,default='Cash'); invoice_number=models.CharField(max_length=100,blank=True); notes=models.TextField(blank=True)
    @property
    def total_amount(self): return self.quantity*self.purchase_price
    @property
    def pending_amount(self): return self.total_amount-self.amount_paid
class Expense(Base):
    date=models.DateField(); category=models.CharField(max_length=80); sub_category=models.CharField(max_length=80,blank=True); description=models.CharField(max_length=255); amount=models.DecimalField(max_digits=14,decimal_places=2); payment_mode=models.CharField(max_length=40,default='Cash'); paid_by=models.CharField(max_length=150,blank=True); classification=models.CharField(max_length=30,default='Business'); notes=models.TextField(blank=True)
class Petrol(Base):
    date=models.DateField(); vehicle=models.CharField(max_length=100); person=models.CharField(max_length=150,blank=True); purpose=models.CharField(max_length=255,blank=True); start_location=models.CharField(max_length=150,blank=True); destination=models.CharField(max_length=150,blank=True); odometer=models.DecimalField(max_digits=14,decimal_places=2,default=0); km=models.DecimalField(max_digits=14,decimal_places=2,default=0); petrol_quantity=models.DecimalField(max_digits=14,decimal_places=2,default=0); petrol_amount=models.DecimalField(max_digits=14,decimal_places=2,default=0); toll=models.DecimalField(max_digits=14,decimal_places=2,default=0); parking=models.DecimalField(max_digits=14,decimal_places=2,default=0); other=models.DecimalField(max_digits=14,decimal_places=2,default=0); paid_by=models.CharField(max_length=150,blank=True); notes=models.TextField(blank=True)
    @property
    def total(self): return self.petrol_amount+self.toll+self.parking+self.other
class Allowance(Base):
    date=models.DateField(); employee=models.CharField(max_length=150); allowance_type=models.CharField(max_length=60); amount=models.DecimalField(max_digits=14,decimal_places=2); purpose=models.CharField(max_length=255,blank=True); payment_mode=models.CharField(max_length=40,default='Cash'); paid_by=models.CharField(max_length=150,blank=True); notes=models.TextField(blank=True)
class Salary(Base):
    employee=models.CharField(max_length=150); salary_month=models.CharField(max_length=20); basic=models.DecimalField(max_digits=14,decimal_places=2); allowance=models.DecimalField(max_digits=14,decimal_places=2,default=0); additions=models.DecimalField(max_digits=14,decimal_places=2,default=0); deductions=models.DecimalField(max_digits=14,decimal_places=2,default=0); payment_date=models.DateField(null=True,blank=True); payment_mode=models.CharField(max_length=40,default='Bank'); status=models.CharField(max_length=30,default='Pending'); notes=models.TextField(blank=True)
    @property
    def net_salary(self): return self.basic+self.allowance+self.additions-self.deductions
class Partner(Base):
    name=models.CharField(max_length=150); phone=models.CharField(max_length=40,blank=True); email=models.EmailField(blank=True); joining_date=models.DateField(null=True,blank=True); share_percent=models.DecimalField(max_digits=6,decimal_places=2,default=0); initial_capital=models.DecimalField(max_digits=14,decimal_places=2,default=0); additional_investment=models.DecimalField(max_digits=14,decimal_places=2,default=0); withdrawals=models.DecimalField(max_digits=14,decimal_places=2,default=0); notes=models.TextField(blank=True)
class CashTransaction(Base):
    date=models.DateField(); transaction_type=models.CharField(max_length=40); description=models.CharField(max_length=255); amount=models.DecimalField(max_digits=14,decimal_places=2); reference=models.CharField(max_length=100,blank=True)
class BankTransaction(CashTransaction): bank_name=models.CharField(max_length=100,blank=True)
class GeneralTransaction(Base):
    date=models.DateField(); transaction_type=models.CharField(max_length=40); category=models.CharField(max_length=100); description=models.CharField(max_length=255); amount=models.DecimalField(max_digits=14,decimal_places=2); payment_mode=models.CharField(max_length=40,default='Cash'); person_company=models.CharField(max_length=150,blank=True); reference=models.CharField(max_length=100,blank=True); notes=models.TextField(blank=True)
class AuditLog(models.Model): user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL); action=models.CharField(max_length=30); model_name=models.CharField(max_length=100); object_id=models.CharField(max_length=80); created_at=models.DateTimeField(auto_now_add=True); details=models.JSONField(default=dict)
