from django.shortcuts import render, redirect

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Todo
from .forms import TodoForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse

@method_decorator(permission_required('app.list_app'))
def listar(request):
    porhacer = Todo.objects.all()
    return render(request, 'app/listar.html', {'porhacer': porhacer})

# Muestra todo el contenido de los campos de la tabla Todo
class TodoList(ListView):
    model = Todo

# Muestra todo el contenido detallado de la tabla Todo

class TodoDetail(DetailView):
    model = Todo
    @method_decorator(permission_required('app.view_app'))
    def dispatch(self, *args, **kwargs):
        return super(TodoDetail, self).dispatch(*args, **kwargs)

class TodoCreate(CreateView):
    model = Todo

    form_class = TodoForm
    @method_decorator(permission_required('app.add_app'))
    def dispatch(self, *args, **kwargs):
        return super(TodoCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return redirect(self.object)

class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm

    @method_decorator(permission_required('app.change_app'))
    def dispatch(self, *args, **kwargs):
        return super(TodoUpdate, self).dispatch(*args, **kwargs)

class TodoDelete(DeleteView):
    model = Todo


    @method_decorator(permission_required('app.delete_app'))

    def dispatch(self, *args, **kwargs):
        return super(TodoDelete, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('app_list')

