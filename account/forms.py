from django import forms
from .models import KYC
from django.forms import ImageField,FileInput
from django.forms.widgets import DateInput


class DateInput(forms.DateInput):
  input_type = 'date'
  input_format = ('%Y-%m-%d')



class KYCForm(forms.ModelForm):
  identity_image = ImageField(widget=FileInput)
  image = ImageField(widget=FileInput)

  class Meta:
    model = KYC
    fields=["full_name", "image", "nationality", "marital_status", "gender", "identity_type","identity_image", "date_of_birth","signature","country", "state","city","house_address","mobile", "city"]
    widgets ={
      "full_name":forms.TextInput(
        attrs={
          "placeholder":"Full Name",
          "class":"form-control bg-light",
          "id":"",
        }
      ),
      "house_address":forms.TextInput(
        attrs={
          "placeholder":"House Adress",
          "class":"form-control",
          "id":"",
        }
      ),
      "mobile":forms.TextInput(
        attrs={
          "placeholder":"Mobile Number",
          "class":"form-control",
          "id":"",
        }
      ),
      "country":forms.TextInput(
        attrs={
          "placeholder":"Country",
          "class":"form-control",
          "id":"",
        }
      ),
      "state":forms.TextInput(
        attrs={
          "placeholder":"State",
          "class":"form-control",
          "id":"",
        }
      ),
      "city":forms.TextInput(
        attrs={
          "placeholder":"City",
          "class":"form-control",
          "id":"",
        }
      ),
      "data_of_birth":forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={
          "class":"form-control",
          "type":"date",
        }
      ),
    }
