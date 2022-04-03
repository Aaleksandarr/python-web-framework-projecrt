from django.contrib.auth import mixins as auth_mixin
from django.urls import reverse_lazy
from django.views import generic as views
from motherearth.web.models import Post


class CreateDashboardPost(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    fields = ('title', 'content', 'photo')
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user.profile
        return super().form_valid(form)


class DashboardPostDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Post
    template_name = 'posts/post_details.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = list(Post.objects.filter(user_id=self.object.user_id))

        context.update({

            'is_owner': self.object.user_id == self.request.user.id,
            'posts': posts,
        })

        return context


class EditDashboardPostView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Post
    template_name = 'posts/post_edit.html'
    fields = ('title', 'content', 'photo')

    def get_success_url(self):
        return reverse_lazy('dashboard')


class DeleteDashboardPostView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')


class MyPostsView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Post
    template_name = 'posts/my_posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user.profile)
