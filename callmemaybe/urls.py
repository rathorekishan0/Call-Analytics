from django.conf.urls import include, url
from . import views

app_name = 'callmemaybe'

urlpatterns = [
	#/game
    url(r'^$',views.UserLoginView.as_view(), name='login'),
    url(r'^index/$',views.index, name='index'),
    url(r'^logout/$',views.logout_view, name='logout'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    ]
