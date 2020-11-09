from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request):
    #checking for post request
    if request.method == 'POST':
        #create a new form
        form = UserRegisterForm(request.POST)
        #check the form valid
        if form.is_valid():
            form.save()
            #find all validated form data
            username = form.cleaned_data.get('username')
            messages.success(request, f'Succes.. Please login')
            #return the message to blog
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#add functionality function into function
@login_required
def profile(request):
    if request.method == 'POST':
        #instance=request.user show the current info
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'updated')
            #return the message to blog
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request, 'users/profile.html', context)

