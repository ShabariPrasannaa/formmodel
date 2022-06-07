from django.shortcuts import render
from . import forms
# Create your views here.
def empdetailsView(request):
    form = forms.EmployeeInfoForm()
    empInfo = {'form':form}
    return render(request,'formApps/html.html',context=empInfo)
