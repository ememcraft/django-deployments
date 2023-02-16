from django.shortcuts import render
from app.models import User
from . import forms


# Create your views here.
def main(request):
	content_text = {'title': 'Hello, You are at the Main Page!',
					'text': 'This is a simple hero unit, a simple jumbotron-style component for calling extra attention to featured content or information.'}
	return render(request, 'main.html', content_text)


def users(request):
	users_list = User.objects.order_by('lastName')
	users_dict = {'users': users_list}
	return render(request, 'users.html', context=users_dict)


def sign_up_form(request):
	form = forms.SignUp()

	if request.method == 'POST':

		form = forms.SignUp(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return main(request)

	return render(request, 'signup.html', {'form': form})
