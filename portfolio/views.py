from django.shortcuts import render

from .models import Project


def projects(request):
    items = Project.objects.prefetch_related('skills')
    return render(request, 'portfolio/projects.html', {'projects': items})
