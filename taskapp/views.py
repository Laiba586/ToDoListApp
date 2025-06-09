from django.shortcuts import render,HttpResponse,redirect
from taskapp.models import Task
# Create your views here.
def index(request):
       if request.method == 'GET':
           tasks = Task.objects.all()
           return render(request,'taskapp/index.html',{'tasks':tasks})
def add_task(request):
       if request.method == 'POST':
           title = request.POST.get('title')
           Task.objects.create(title=title)
           return redirect('index')
       tasks= Task.objects.all()
       return render(request,'taskapp/addtask.html',{'tasks':tasks})     
def delete_task(request,task_id):
     task = Task.objects.get(id=task_id)
     task.delete()
     return redirect('index')
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        task.title = title
        task.save()
        return redirect('index')

    return render(request, 'taskapp/edit.html', {'task': task})
       
