from django.shortcuts import render, HttpResponse
from django.shortcuts import render  
from django.http import HttpResponse  
from EMSapp.functions.functions import handle_uploaded_file  
from EMSapp.forms import CertificateForm  

# Create your views here.

def index(request):  
    if request.method == 'POST':  
        student = CertificateForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = CertificateForm()  
        return render(request,'index.html',{'form':student})  