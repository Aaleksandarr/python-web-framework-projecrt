from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views
from motherearth.auth_app.forms import CreateProfileForm
from motherearth.auth_app.models import Profile, MotherearthUser
from motherearth.common.view_mixins import RedirectToDashboard
from motherearth.web.models import Post


class UserRegisterView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'auth/profile_create.html'
    success_url = reverse_lazy('login user')


class UserLoginView(auth_views.LoginView):
    template_name = 'auth/login_page.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')


class UserLogoutView(auth_views.LogoutView):
    template_name = 'auth/logout_page.html'


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = 'auth/change_password.html'
    success_url = reverse_lazy('dashboard')


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'main/../../templates/auth/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = list(Post.objects.filter(user_id=self.object.user_id))

        context.update({

            'is_me': self.object.user_id == self.request.user.id,
            'posts': posts,
        })

        return context


class EditProfileView(views.UpdateView):
    model = Profile
    template_name = 'auth/profile_edit.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = list(Post.objects.filter(user_id=self.object.user_id))

        context.update({

            'is_me': self.object.user_id == self.request.user.id,
            'posts': posts,
        })

        return context


class DeleteUserView(views.DeleteView):
    model = MotherearthUser
    template_name = 'auth/user_delete.html'

    def get_success_url(self):
        return reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = list(Post.objects.filter(user_id=self.object.id))

        context.update({

            'is_me': self.object.id == self.request.user.id,
            'posts': posts,
        })

        return context

