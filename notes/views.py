from django.shortcuts import render, redirect
from .models import Note

def index(request):
    if request.method == "POST":
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        nota = Note(title=title, content=content)
        nota.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request, id):
    nota = Note.objects.get(id=id)
    nota.delete()
    return redirect('index')

def update(request, id):
    if request.method == "POST":
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        nota = Note(id=id, title=title, content=content)
        nota.save()
        return redirect('index')
    else:
        nota = Note.objects.get(id=id)
        return render(request, 'notes/edit.html', {'note': nota})