from django.shortcuts import render
from django.contrib import messages

from authentication import forms as AFORM
# Create your views here.

def signup_view(request):
	RegisterForm = AFORM.RegisterForm()
	
	if request.method == 'POST':
		RegisterForm = AFORM.RegisterForm(request.POST)
		if RegisterForm.is_valid():
			RegisterForm.save()
			username=RegisterForm.cleaned_data.get('username')
			messages.success(request, f"Account created for {username}")
			return redirect('login')
	context={
		'RegisterForm': RegisterForm,
	}
	return render(request, 'auth/signup.html',context)
	