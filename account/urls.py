from django.urls import path
from . import views


urlpatterns = [
  path('',views.account,name='account'),
  path('kyc-reg/',views.kyc_reg,name="kyc-reg"),
  path('account/',views.account,name="account"),
]