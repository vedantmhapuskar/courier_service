from django.shortcuts import redirect, render
from .models import jobapp

# Create your views here.
def jobapps(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    return render(request, "job.html")


def add_details(request):
    if request.method=="POST":
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('email') and request.POST.get('phonenumber') and request.POST.get('city') and request.POST.get('empstatus') and request.FILES['resume']:
            savepak=jobapp()
            savepak.firstname=request.POST.get('firstname')
            savepak.lastname=request.POST.get('lastname')
            savepak.email=request.POST.get('email')
            savepak.phonenumber=request.POST.get('phonenumber')
            savepak.city=request.POST.get('city')
            savepak.empstatus=request.POST.get('empstatus')
            savepak.resume=request.FILES['resume']
            
            savepak.save(jobapp)
            return render(request,"job.html")

    else:
            return render(request,"job.html")
 