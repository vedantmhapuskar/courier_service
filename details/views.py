import email
from email import message
import imp
import string
from typing import Dict
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import forms
from gfg.info import EMAIL_HOST_USER
from .models import packagedetails
from .forms import packageForm
import razorpay
import stripe
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.
def load_form(request):
    form = packageForm
    return render(request , "load_form.html",{'form':form})

def add(request):
    form =packageForm(request.POST)
    form = form.save(commit=False)
    form.user = request.user
    form.save()
    return redirect('/show')

def show(request):
    packages =packagedetails.objects.filter(user=request.user)
    return render(request,"show.html",{'packs':packages})

def summary(request, id):
    packages =packagedetails.objects.get(id=id)
    return render(request,'summary.html',{'packs':packages})

def delete(request, id):
    packages =packagedetails.objects.get(id=id)
    packages.delete()
    return redirect('/show')

def track(request, track_id):
    tracks =packagedetails.objects.get(track_id=track_id)
    return render(request,'track.html',{'tr':tracks})

def payment(request, id):
    packages =packagedetails.objects.get(id=id)
    return render(request,'payment.html',{'packs':packages})

stripe.api_key = 'sk_test_51KhzZmSE7hGgo29p0dJjVxY4S0axdUqkSlr51lFDWr3f0AGRfpdrcJeArpj3iTQEXb2HLDAjszupjwcUADk7KNdB003MHbwEyZ'

def checkout_session(request, id):
    packages =packagedetails.objects.get(id=id)
    pktype = str(packages.track_id)
    price =  int(packages.weight)
    amount = int(price) * 33000
    session = stripe.checkout.Session.create(
        payment_method_types=['card'], 
        line_items=[{
          'price_data': {
            'currency': 'inr',
            'product_data': {
              'name': pktype,
            },
            'unit_amount': amount,
         },
         'quantity': 1,
        }],
            mode='payment',
    success_url='http://127.0.0.1:8000/success',
    cancel_url='http://127.0.0.1:8000/cancel',
    )
    

    
    return redirect(session.url, code=303)

def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')

# share package status via email    

def subscribe(request):
    
    
    if request.method == 'POST':
        sender = request.POST['sender']
        subject = str(sender) + ' has send you order tracking'
        
        email = request.POST['email']
        trackid = request.POST['trackid']
        message = 'Tracking Id :- '+ str(trackid) + ' \nPlease visit http://127.0.0.1:8000/ and enter the tracking id in search field to track the order'
        send_mail(subject, 
            message, EMAIL_HOST_USER, [sender,email,trackid], fail_silently = False)
        return redirect(request.META['HTTP_REFERER'])
    