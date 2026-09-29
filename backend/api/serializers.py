from rest_framework import serializers
from .models import *
class Dynamic(serializers.ModelSerializer):
    class Meta: fields='__all__'; read_only_fields=('created_at','updated_at','is_deleted')
for_model={}
def make_serializer(model):
    return type(f'{model.__name__}Serializer',(Dynamic,),{'Meta':type('Meta',(Dynamic.Meta,),{'model':model,'fields':'__all__','read_only_fields':Dynamic.Meta.read_only_fields})})
for m in [Customer,Supplier,Category,Product,Sale,Purchase,Expense,Petrol,Allowance,Salary,Partner,CashTransaction,BankTransaction,GeneralTransaction]: for_model[m]=make_serializer(m)
