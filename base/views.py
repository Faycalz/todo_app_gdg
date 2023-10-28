from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task
# Create your views here.

def taskList(request):
    tasks = Task.objects.all()
    context = {'tasks' : tasks}
    return render(request , 'base/task_list.html' , context)

def task_detail(request , task_id):
    task = Task.objects.get(id=task_id)
    return render(request , 'base/task_detail.html' , {'task' : task})

def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('title')

        Task.objects.create(
            title=title,
            description=description,
            user=request.user
        )
        return redirect('task')
    return render(request , 'base/task_create.html')

def update_task(request , task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        complete = request.POST.get('complete') == 'on'

        task.title= title
        task.description = description
        task.complete = complete
        task.save()

        return redirect('task')
    return render(request , 'base/task_update.html', {'task':task})
def delete_task(request , task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('task')
    return render(request , 'base/task_delete.html' , {'task':task})