from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
path('load_form',views.load_form),
    path('add',views.add),
    path('show',views.show),
    path('summary/<int:id>',views.summary),
    path('payment/<int:id>',views.payment),
    path('success', views.success, name='success'),
    path('cancel', views.cancel, ),
    path('checkout_session/<int:id>',views.checkout_session, name='checkout_session'),
    path('track/<int:track_id>',views.track),
    path('delete/<int:id>',views.delete),
    path('subscribe', views.subscribe, ),

]