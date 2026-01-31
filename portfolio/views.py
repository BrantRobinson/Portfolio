from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import ProjectForm
from .models import Project

# function based view shown in class, but I opted for class based to allow pagination easier
class ProjectListView(ListView):
    model = Project
    paginate_by = 2
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.prefetch_related('skills').order_by('-year', 'title')


class HomeRedirectIfNotLoggedInMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('pages:home')
        return super().dispatch(request, *args, **kwargs)


class ProjectCreateView(HomeRedirectIfNotLoggedInMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'portfolio/project_form.html'
    success_url = reverse_lazy('portfolio:projects')


class ProjectUpdateView(HomeRedirectIfNotLoggedInMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'portfolio/project_form.html'
    success_url = reverse_lazy('portfolio:projects')


class ProjectDeleteView(HomeRedirectIfNotLoggedInMixin, DeleteView):
    model = Project
    template_name = 'portfolio/project_confirm_delete.html'
    success_url = reverse_lazy('portfolio:projects')
