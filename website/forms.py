from django import forms

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"type":"text","class":"form-control"}))
	password1 = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"type":"password","class":"form-control"}))
	password2 = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"type":"password","class":"form-control"}))
	email = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"type":"text","class":"form-control"}))

class LoginForm(forms.Form):
	username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"type":"text","class":"form-control"}))
	password = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"type":"password","class":"form-control"}))
