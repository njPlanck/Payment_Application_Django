from account.models import Account
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from payapp.models import Transaction

@login_required
def search_users_account_number(request):
  account = Account.objects.all()
  query = request.POST.get("account_number")
  if query:
    account = account.filter(
      Q(account_number=query)|
      Q(account_id=query)
    ).distinct()

  context = {
    'account':account,
    'query':query,
  }
  return render(request,"transfer/search-account-number.html",context)


def amount_transfer(request,account_number):
  try:
    account = Account.objects.get(account_number=account_number)
  except:
    messages.warning(request,"Account does not exist")
    return redirect("find-account")
  context = {
    'account':account,
  }
  return render(request,"transfer/amount-transfer.html",context)


def amount_trans_process(request,account_number):
  account = Account.objects.get(account_number=account_number)
  sender = request.user
  receiver = account.user
  
  sender_account = request.user.account
  receiver_account = account

  if request.method == "POST":
    amount = request.POST.get("amount-send")    
    description= request.POST.get("description")

    print(amount)
    print(description)

    if sender_account.account_balance > 0 and amount:
      new_transaction = Transaction.objects.create(
        user = request.user,
        amount = amount,
        description = description,
        receiver = receiver,
        sender = sender,
        sender_account = receiver_account,
        status = "processing",
        transaction_type = "transfer"
      )
      new_transaction.save()

      transaction_id = new_transaction.transaction_id

      return redirect("transfer-confirmation",account.account_number,transaction_id)
    
    else:
      messages.warning(request,"insufficient funds")
      return redirect("amount-transfer",account.account_number)
    
  

  else:
    messages.warning(request,"Error Occurred. Try again.")
    return redirect("account")
  


def transfer_confirmation(request,account_number,transaction_id):
  account = Account.objects.get(account_number=account_number)
  transaction = Transaction.objects.get(transaction_id=transaction_id)

  context ={
    'account':account,
    'transaction':transaction
  }

  return render(request,"transfer/transfer-confirmation.html",context)



def tranfer_process(request,account_number,transaction_id):
  account = Account.objects.get(account_number=account_number)
  transaction = Transaction.objects.get(transaction_id=transaction_id)

  sender = request.user
  receiver = account.user

  sender_account = request.user.account
  receiver_account = account

  completed = False

  if request.method == "POST":
    pin_number = request.POST.get("pin-number")


