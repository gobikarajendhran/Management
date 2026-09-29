from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
router=DefaultRouter()
for prefix,cls in [('customers',CustomerViewSet),('suppliers',SupplierViewSet),('categories',CategoryViewSet),('products',ProductViewSet),('sales',SaleViewSet),('purchases',PurchaseViewSet),('expenses',ExpenseViewSet),('petrol',PetrolViewSet),('allowance',AllowanceViewSet),('salary',SalaryViewSet),('partners',PartnerViewSet),('cash',CashTransactionViewSet),('bank',BankTransactionViewSet),('transactions',GeneralTransactionViewSet)]: router.register(prefix,cls,basename=prefix)
urlpatterns=[path('auth/token/',obtain_auth_token),path('dashboard/',dashboard)]+router.urls
