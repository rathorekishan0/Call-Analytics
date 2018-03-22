from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm
from hackathon.models import Staff, Recordings
from django.views.generic import View
from django.views import generic
from django.views.generic import DetailView


# Create your views here.

class UserLoginView(View):
	form_class = UserLoginForm
	template_name = 'callmemaybe/page-login.html'	

	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():
			
			#cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			#returns user objects if credential are correct
			user = authenticate(username=username,password=password)

			if user is not None:

				if user .is_active:
					login(request, user)
					print(request.user.is_authenticated())
					return redirect('callmemaybe:index')


		return render(request,self.template_name,{'form':form})

def index(request):
	user = request.user
	staff = Staff.objects.get(user=user)
	calls = Recordings.objects.filter(staff=staff)[0:5]
	template = loader.get_template('callmemaybe/app-profile.html')
	return render(request,'callmemaybe/app-profile.html',{'staff' : staff,'calls':calls})

def logout_view(request):
    logout(request)
    return redirect('callmemaybe:login')

class DetailView(DetailView):
	model = Recordings
	template_name = 'callmemaybe/detail.html'

	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		rec = Recordings.objects.filter().exclude(score=None).order_by('timestamp')
		context['rec'] = rec
		return context