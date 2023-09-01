from django import forms
from .models import MyProject

class MyImageForm(forms.ModelForm):
    class Meta:
        model = MyProject
        fields = ['myproject_name','myproject_description', 'myproject_image']
