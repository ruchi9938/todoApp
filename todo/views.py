from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import TodoItem

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        TodoItem.objects.create(title=title)
        return redirect('todo_list')
    return render(request, 'todo/todo_create.html')

def todo_update(request, todo_id):
    todo = get_object_or_404(TodoItem, pk=todo_id)
    if request.method == 'POST':
        title = request.POST['title']
        todo.title = title
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo/todo_update.html', {'todo': todo})

def todo_delete(request, todo_id):
    todo = get_object_or_404(TodoItem, pk=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo/todo_delete.html', {'todo': todo})
