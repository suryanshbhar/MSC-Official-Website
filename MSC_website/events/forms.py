from django import forms

CHOICES = ['Event-1','Event-2','Event-3']
class Register(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='name')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),label='email')
    roll_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='rollno')
    branch = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='branch')
    year = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='year')
    college = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='college')
    events = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),choices=CHOICES,label='checkbox')