from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import (UserRegisterForm, 
    UserUpdateForm, ProfileUpdateForm, ProfileStudentUpdateForm)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if request.user.email.endswith('@mitaoe.ac.in'):
            # print('here')
            p_s_form = ProfileStudentUpdateForm(request.POST,
                                       instance=request.user.profile_student)
            if p_s_form.is_valid(): p_s_form.save()

        if u_form.is_valid() and p_form.is_valid() :
            u_form.save()
            p_form.save()
            
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        p_s_form = ProfileStudentUpdateForm(instance=request.user.profile_student)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'p_s_form': p_s_form
    }

    return render(request, 'users/profile.html', context)

