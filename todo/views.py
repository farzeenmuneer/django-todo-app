

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/list.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        notes = request.POST['notes']
        Todo.objects.create(subject=subject, notes=notes)
        return redirect('todo_list')
    return render(request, 'todo/form.html')

def todo_view(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todo/view.html', {'todo': todo})

def todo_edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.subject = request.POST['subject']
        todo.notes = request.POST['notes']
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo/form.html', {'todo': todo})

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todo_list')
