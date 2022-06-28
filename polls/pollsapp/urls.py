from django.urls import URLPattern, path
from . import views

URLPattern=[
    path('',views.index, name='index'),
    path ('',views.index, name='vote'),
    path('',views.resultado,name='resultado')

    ]
