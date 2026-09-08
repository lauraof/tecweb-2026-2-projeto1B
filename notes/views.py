from django.shortcuts import render, redirect
from .models import Note, Tag

def index(request):
    if request.method == "POST":
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        nome = request.POST.get('tag')
        if nome:
            lista_tag = Tag.objects.filter(nome=nome)
            if lista_tag:
                tag = lista_tag[0]
            else:
                tag = Tag(nome=nome)
                tag.save()
            nota = Note(title=title, content=content, tag=tag)
        else:
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
        nome = request.POST.get('tag')
        if nome:
            lista_tag = Tag.objects.filter(nome=nome)
            if lista_tag:
                tag = lista_tag[0]
            else:
                tag = Tag(nome=nome)
                tag.save()
            nota = Note(id=id, title=title, content=content, tag=tag)
        else:
            nota = Note(id=id, title=title, content=content)
        nota.save()
        return redirect('index')
    else:
        nota = Note.objects.get(id=id)
        return render(request, 'notes/edit.html', {'note': nota})

def tags(request):
    tags = Tag.objects.all()
    return render(request, 'notes/tags.html', {'tags': tags})

def tag(request, id):
    tag = Tag.objects.get(id=id)
    notas = Note.objects.filter(tag=tag)
    return render(request, 'notes/tag.html', {'tag': tag.nome, 'notes': notas})