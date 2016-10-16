from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .forms import UserForm, UserProfileForm


# Create your views here.
@login_required
def restricted(request):
	return HttpResponse("Você precisa estar logado para ver isso.")

def index(request):
	template_name = 'account/index.html'

	context = {
		'title' : 'Perfil',
	}

	return render(request, template_name, context)

def register(request):

	template_name = 'account/register.html'
	# A boolean value for telling the template
	# whether the registration was successful.
	# Set to False initially. Code changes value to
	# True when registration succeeds.
	registered = False


	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)

			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()

			registered = True

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	context = {
		'title' : "Registre-se",
		'user_form' : user_form,
		'profile_form' : profile_form,
		'registered' : registered
	}

	return render(request, template_name, context)

def user_login(request):
	template_name = 'account/login.html'

	context = {
		'title' : "Entrar",
	}

	if request.method == 'POST':

		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('account:index'))
			else:
				return HttpResponse("Seu usuário está disativada.")
		else:
			print("Login inválido: {0},{1}".format(username, password))		
			return HttpResponse("Login inválido.")
	
	else:
		return render(request, template_name, context)


@login_required
def user_logout(request):
	logout(request)

	return HttpResponseRedirect(reverse('core:index'))