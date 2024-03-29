from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def redirect_to_show(request):
    return redirect('/show')

def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  

def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  

@csrf_exempt
def test(request, id): 
    print('console: \n',  request , ' ' , id, sep='\t'  )
    return JsonResponse({'message': 'Object created successfully', 'id': id})