from django.shortcuts import render, redirect, render_to_response
from .models import UserProfile, Todo
from .forms importi MyRegistrationForm, UserProfileForm, TodoForm, LoginForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login

class Register_UserView(FormView):
    form_class = MyRegistrationForm

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect(default_redirect(self.request, settings.ACCOUNT_LOGIN_REDIRECT_URL))
        if not self.is_open():
            return self.closed()
        return super(MyRegistrationForm, self).get(*args, **kwargs)

    def post(self, *args, **kwargs):
        if not self.is_open():
            return self.closed()
        return super(MyRegistrationForm, self).post(*args, **kwargs)

    def form_invalid(self, form):
        signals.user_sign_up_attempt.send(
            sender=MyRegistrationForm,
            username=form.data.get("username"),
            email=form.data.get("email"),
            result=form.is_valid()
        )
        return super(MyRegistrationForm, self).form_invalid(form)

    def form_valid(self, form):
        self.created_user = self.create_user(form, commit=False)
        # prevent User post_save signal from creating an Account instance
        # we want to handle that ourself.
        self.created_user._disable_account_creation = True
        self.created_user.save()
        self.use_signup_code(self.created_user)
        email_address = self.create_email_address(form)
        if settings.ACCOUNT_EMAIL_CONFIRMATION_REQUIRED and not email_address.verified:
            self.created_user.is_active = False
            self.created_user.save()
        self.create_account(form)
        self.after_signup(form)
        if settings.ACCOUNT_EMAIL_CONFIRMATION_EMAIL and not email_address.verified:
            self.send_email_confirmation(email_address)
        if settings.ACCOUNT_EMAIL_CONFIRMATION_REQUIRED and not email_address.verified:
            return self.email_confirmation_required_response()
        else:
            show_message = [
                settings.ACCOUNT_EMAIL_CONFIRMATION_EMAIL,
                self.messages.get("email_confirmation_sent"),
                not email_address.verified
            ]
            if all(show_message):
                messages.add_message(
                    self.request,
                    self.messages["email_confirmation_sent"]["level"],
                    self.messages["email_confirmation_sent"]["text"].format(**{
                        "email": form.cleaned_data["email"]
                    })
                )
            # attach form to self to maintain compatibility with login_user
            # API. this should only be relied on by d-u-a and it is not a stable
            # API for site developers.
            self.form = form
            self.login_user()
        return redirect(self.get_success_url())

class LoginView():
    def create_user(self, form, commit=True, **kwargs):
        user = get_user_model()(**kwargs)
        username = form.cleaned_data.get("username")
        if username is None:
            username = self.generate_username(form)
        user.username = username
        user.email = form.cleaned_data["email"].strip()
        password = form.cleaned_data.get("password")
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        if commit:
            user.save()
        return user

    def create_account(self, form):
        return Account.create(request=self.request, user=self.created_user, create_email=False)


class LoginView(TemplateView):
    template_name = 'login.html'

    # Sobreescribir el get_context_data para que haga otras cosas
    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        is_auth = False
        username = None

        if self.request.user.is_authenticated():
            is_auth = True
            username = self.request.user.username

        context.update({'is_auth': is_auth , 'username': username})
        return context

    def post(self, *args, **kwargs):
        if not self.is_open():
            return self.closed()
        return super(LoginView, self).post(*args, **kwargs)

class ProfileUserView(TemplateView):
    form_class = UserProfileForm
    def get_form_class(self):
        if self.form_class:
            return self.form_class
        else:
            if self.model is not None:
                model = self.model
            elif hasattr(self, 'object') and self.object is not None:
                model = self.object.__class__
            else:
                model = self.get_queryset().model

            if self.fields is None:
                warnings.warn("Using ModelFormMixin (base class of %s) without "
                              "the 'fields' attribute is deprecated." % self.__class__.__name__,
                              RemovedInDjango18Warning)
            return model_forms.modelform_factory(model, fields=self.fields)

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

