from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
# Create your views here.


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			form.save()
			messages.add_message(request, messages.INFO, f'Account for {username} have been created successfully')
			return redirect('blog:home')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})


def profile_update(request, username):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.add_message(request, messages.INFO, f'Profile for {username} have been updated successfully')
			return redirect('users:profile', username)
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user)

	context = {
	 'u_form': u_form,
	 'p_form': p_form,
	}

	return render(request, 'users/profile.html', context)
