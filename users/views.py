from django.shortcuts import render
from django.contrib.auth import authenticate , login
from django.http import HttpResponseRedirect
from django.views.generic import View
from .forms import LoginForm
from .models import User

class LoginPageView(View):

    def get(self,request):
        form = LoginForm()
        context = {'form': form}
        return render(request=request,template_name='users/login.html', context=context)

    def post(self,request):
        form = LoginForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            email = form.clean('email')
            password = form.clean('password')
            user = authenticate(request, email, password)
            if not user:
                form.add_error('Error invalid email or password!')
                return render(request,'users/login.html', context)
            login(request, user)
            dashboard_url = reversed('dashboard:home')
            return HttpResponseRedirect(redirect_to=dashboard_url)
        return render(request=request,template_name='users/login.html', context=context)

    


