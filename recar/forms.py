from django import forms
from .models import Cars

class Carform(forms.ModelForm):
    
    class Meta():
        model=Cars
       # fields="__all__"
        exclude=['us']


        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'name','id':'ABC',}),
            'price':forms.TextInput(attrs={'class':'form-control','placeholder':'price',}),
            'year':forms.TextInput(attrs={'class':'form-control','placeholder':'year',}),
            'km':forms.TextInput(attrs={'class':'form-control','placeholder':'km',}),
            'ownership':forms.TextInput(attrs={'class':'form-control','placeholder':'ownership',}),
            'transmission':forms.TextInput(attrs={'class':'form-control','placeholder':'transmission',}),
            'company':forms.TextInput(attrs={'class':'form-control','placeholder':'company',}),
            'image':forms.FileInput(attrs={'class':'form-control','placeholder':'image',}),


        }