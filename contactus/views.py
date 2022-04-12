import email
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.mail import send_mail


# Create your views here.
def contact(request):
    
    
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message
        }
        message = '''
        New message: {}
        
        From:{}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '',['courierservicewebsite@gmail.com'])

    return render(request, "contactus.html")