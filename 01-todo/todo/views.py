from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoForm

def home(request):
    """Display all TODOs."""
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'home.html', context)

def create_todo(request):
    """Create a new TODO."""
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            messages.success(request, f'TODO "{todo.title}" created successfully!')
            return redirect('home')
    else:
        form = TodoForm()
    return render(request, 'create_todo.html', {'form': form})

def edit_todo(request, pk):
    """Edit an existing TODO."""
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, f'TODO "{todo.title}" updated successfully!')
            return redirect('home')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'edit_todo.html', {'form': form, 'todo': todo})

def delete_todo(request, pk):
    """Delete a TODO."""
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        title = todo.title
        todo.delete()
        messages.success(request, f'TODO "{title}" deleted successfully!')
        return redirect('home')
    return render(request, 'delete_todo.html', {'todo': todo})

def toggle_resolved(request, pk):
    """Toggle TODO resolved status."""
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_resolved = not todo.is_resolved
    todo.save()
    status = 'marked as resolved' if todo.is_resolved else 'marked as unresolved'
    messages.success(request, f'TODO "{todo.title}" {status}!')
    return redirect('home')