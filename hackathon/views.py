from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.http import Http404
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect,get_object_or_404,_get_queryset,HttpResponse

from django.contrib.auth import authenticate,login
from django.views.generic import View,CreateView,ListView,DetailView
from django.views import View
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
User=get_user_model()
# from .form import UserRegisterForm
from . import models
from rest_framework.response import Response
# from . import serializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated

@login_required
def dashboard(request):
    user = request.user
    staff_detail = []
    staffs = models.Staff.objects.all()
    for staff in staffs:
        st = dict()
        st['staff_detail'] = staff
        st['total_recordings'] = staff.recordings_set.all().count()
        st['enquiry'] = staff.recordings_set.filter(type=1).count()
        st['complaint'] = staff.recordings_set.filter(type=2).count()
        staff_detail.append(st)
    return render(request, 'hackathon/dashboard.html', {'staff_detail': staff_detail})


