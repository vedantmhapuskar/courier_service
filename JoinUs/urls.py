from django.conf import settings 
from django.urls import path, include
from django.conf.urls.static import static 
from . import views
 
urlpatterns = [ 
    
    path('jobapps/', views.jobapps, name="jobapps"), 
    path('add_details/', views.add_details, name="add_details"), 
]  
if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)