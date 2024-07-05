from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def addandshort(request):
    fm=StudentRegistration()
    return render(request,'test_app/addandshort.html',{'form':fm})