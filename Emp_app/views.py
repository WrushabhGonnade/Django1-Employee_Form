from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from Emp_app.forms import Employee_Form
from Emp_app.models import Employee_Table


def insert(request):
    if request.method == "POST":
        form = Employee_Form(request.POST)
        if form.is_valid:
            try:
                form.save()
                return redirect("/")
            except:
                pass
    form = Employee_Form()
    return render(request, "home.html", {'form': form})


def show(request):
    data = Employee_Table.objects.all()
    return render(request, 'show.html', {"data": data})


def delete(request, id):
    data = Employee_Table.objects.get(id=id)
    data.delete()
    return redirect('/')


def edit(request, id):
    data = Employee_Table.objects.get(id=id)
    return render(request, "edit.html", {"data": data})


def update(request, id):
    data = Employee_Table.objects.get(id=id)
    form = Employee_Form(request.POST, instance=data)
    form.save()
    return redirect("/")
