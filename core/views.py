from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task

from .models import * 
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.



def index(request):
  tasks = Task.objects.all()
  form = TaskForm()



  if request.method == "POST" :
    form = TaskForm(request.POST)
    print("uhiuhi")
    if form.is_valid():
      form.save()
    return redirect('index')
  

  context = {'tasks': tasks, "form" : form}
  return render(request, 'tasks/list.html', context)
 
    


def updateTask(request, pk):
  task = Task.objects.get(id=pk)
  form = TaskForm(instance=task)


  if request.method == "POST":
   
    form = TaskForm(request.POST,instance=task)
  
    if form.is_valid():
      print("Yes")
      form.save()
      return redirect('index')
  context = {'form' : form}

  return render(request, 'tasks/update.html', context)





def deleteTask(request, pk):
  item = Task.objects.get(id=pk)

  context = {'item' : item}
  
  
  return render(request, 'tasks/delete.html', context)
  

def taskListView(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})

def list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})


def deleteTask(request, pk):
    item = get_object_or_404(Task, id=pk)  # Fetch the task by ID

    if request.method == "POST":  # If the form is submitted
        item.delete()
        return redirect('list')  # Redirect to the task list page

    return render(request, 'tasks/delete.html', {'item': item})
