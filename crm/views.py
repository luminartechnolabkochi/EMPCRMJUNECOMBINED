from django.shortcuts import render,redirect
from django.views.generic import View
from crm.forms import EmployeeForm,EmployeesModelForm
from crm.models import Employees
# Create your views here.


class EmployeeCreateView(View):

    def get(self,request,*args, **kwargs):
        form=EmployeesModelForm()
        return render(request,"emp_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
       form=EmployeesModelForm(request.POST)
       if form.is_valid():
           form.save()
        #    Employees.objects.create(**form.cleaned_data)
           print("created")
           return render(request,"emp_add.html",{"form":form})
       else:
            return render(request,"emp_add.html",{"form":form})


class EmployeeListView(View):

    def get(self,request,*args,**kwargs):
        qs=Employees.objects.all()
        return render(request,"emp_list.html",{"data":qs})

           


#url : localhost:8000/employees/{pk}/

class EmployeeDetailView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)
        return render(request,"emp_detail.html",{"data":qs})

#url : localhost:8000/employees/{pk}/remove/


class EmployeeDeleteView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Employees.objects.get(id=id).delete()
        return redirect("emp-all")
    