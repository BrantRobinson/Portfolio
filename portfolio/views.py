from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import ProjectForm
from .models import Project

# function based view shown in class, but I opted for class based to allow pagination easier
class ProjectListView(ListView):
    model = Project
    paginate_by = 4
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.prefetch_related('skills').order_by('-year', 'title')


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'portfolio/project_form.html'
    success_url = reverse_lazy('portfolio:projects')


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'portfolio/project_form.html'
    success_url = reverse_lazy('portfolio:projects')


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'portfolio/project_confirm_delete.html'
    success_url = reverse_lazy('portfolio:projects')
