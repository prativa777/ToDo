from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, template_name='todo_app/todo_list.html', context={'todos':todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        detail = request.POST.get('detail')
        Todo.objects.create(title=title, date=date, detail=detail)
        return redirect('todo_list')
    return render(request, template_name='todo_app/todo_add.html')

def update_todo(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        detail = request.POST.get('detail')
        Todo.objects.filter(id=id).update(title=title, date=date, detail=detail)
        return redirect('todo_list')
    return render(request, template_name='todo_app/todo_update.html', context={'todo':todo})

def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, template_name='todo_app/todo_delete.html', context={'todo':todo})
