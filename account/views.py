from django.shortcuts import render, redirect
from .models import KYC, Account
from .forms import KYCForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

#@login_required
def account(request):
  if request.user.is_authenticated:
    user = request.user

    try:
      kyc = KYC.objects.get(user=user)
    except:
      messages.warning(request,"You need to submit your kyc")
      return redirect("kyc-reg")
  
    account = Account.objects.get(user=user)
  else:
    messages.warning(request,"You need to login to access this page")
    return redirect('userauths:sign-in')
  context = {
    "account":account,
    "kyc":kyc,
  }
  return render(request,'account/account.html',context)

#@login_required
def kyc_reg(request):
  if request.user.is_authenticated:  
     user = request.user
     account = Account.objects.get(user=user)

     try:
       kyc = KYC.objects.get(user=user)

     except:
      kyc = None

     if request.method == "POST":
       form = KYCForm(request.POST, request.FILES, instance=kyc)
       if form.is_valid():
        new_form = form.save(commit=False)
        new_form.user = user
        new_form.account = account
        new_form.save()
        messages.success(request,"KYC submitted successfully. Being reviewed now.")
        return redirect("index")
     else:
       form = KYCForm(instance=kyc)
  else:
    messages.warning(request,"You need to login to access this page")
    return redirect('userauths:sign-in')

  context = {
    "form":form,
    "account":account,
    "kyc":kyc,
  }

  return render(request,"account/kyc-form.html",context)

 
