from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(reqeust, 'Registration successful.')
            return redirect('home')

        messages.error(request, 'Unsuccessful registration.')

    form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, 'registration/register.html', context)
