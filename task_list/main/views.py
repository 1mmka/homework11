from django.shortcuts import render,redirect
from main.models import Task

# Create your views here.
def show(request):
    tasks_data = Task.objects.all()
    return render(request,'show.html',{'tasks_data':tasks_data})

def add(request):
    if request.method == "POST":
        rd = request.POST
        new_task = Task.objects.create(
            title=rd['title'],
            body=rd['body']
        )
        new_task.save()
        return redirect('show_page')
    else:
        return render(request,'add.html')

def complete_un(request,id):
    task = Task.objects.get(id=id)
    if task.status == True:
        task.status = False
        task.save()
    else:
        task.status = True
        task.save()
    return redirect('show_page')