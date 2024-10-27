from django.urls import path
from . import views
from . import transfer


urlpatterns = [
  path('',views.index,name='index'),

  #search account

  path('find-account/',transfer.search_users_account_number,name='find-account'),
  path('amount-transfer/<account_number>/',transfer.amount_transfer,name='amount-transfer'),
  path('amount-trans-process/<account_number>/',transfer.amount_trans_process,name='amount-trans-process'),
  path('transfer-confirmation/<account_number>/<transaction_id>',transfer.transfer_confirmation,name='transfer-confirmation'),



  #receive mone

  #add a card
]