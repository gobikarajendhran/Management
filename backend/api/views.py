from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Sum
from django.utils import timezone
from .models import *
from .serializers import for_model

class BaseVS(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    def get_queryset(self): return self.queryset.filter(is_deleted=False).order_by('-created_at')
    def perform_destroy(self,instance): instance.is_deleted=True; instance.save(update_fields=['is_deleted','updated_at'])

def vs(model): return type(f'{model.__name__}ViewSet',(BaseVS,),{'queryset':model.objects.all(),'serializer_class':for_model[model]})
CustomerViewSet=vs(Customer); SupplierViewSet=vs(Supplier); CategoryViewSet=vs(Category); ProductViewSet=vs(Product); SaleViewSet=vs(Sale); PurchaseViewSet=vs(Purchase); ExpenseViewSet=vs(Expense); PetrolViewSet=vs(Petrol); AllowanceViewSet=vs(Allowance); SalaryViewSet=vs(Salary); PartnerViewSet=vs(Partner); CashTransactionViewSet=vs(CashTransaction); BankTransactionViewSet=vs(BankTransaction); GeneralTransactionViewSet=vs(GeneralTransaction)
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def dashboard(request):
    today=timezone.localdate(); sales=Sale.objects.filter(is_deleted=False,date=today); expenses=Expense.objects.filter(is_deleted=False,date=today)
    s=sum((x.total_amount for x in sales),0); e=expenses.aggregate(v=Sum('amount'))['v'] or 0
    products=Product.objects.filter(is_deleted=False)
    return Response({'today_sales':s,'today_expenses':e,'today_profit':s-e,'sales_count':sales.count(),'expense_count':expenses.count(),'cash_balance':0,'bank_balance':0,'stock_value':sum((p.stock_value for p in products),0),'low_stock':sum(1 for p in products if p.current_stock<=p.minimum_stock),'receivables':sum((x.pending_amount for x in Sale.objects.filter(is_deleted=False)),0),'payables':sum((x.pending_amount for x in Purchase.objects.filter(is_deleted=False)),0)})
