from django.contrib.auth import mixins as auth_mixin
from django.urls import reverse_lazy
from django.views import generic as views
from motherearth.web.models import Thanks


class CreateThanks(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = Thanks
    template_name = 'thanks/thanks_create.html'
    fields = ('title', 'content', 'photo')
    success_url = reverse_lazy('thanks')

    def form_valid(self, form):
        form.instance.user = self.request.user.profile
        return super().form_valid(form)


class ThanksDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Thanks
    template_name = 'thanks/thanks_details.html'
    context_object_name = 'thanks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thanks_list = list(Thanks.objects.filter(user_id=self.object.user_id))

        context.update({

            'is_owner': self.object.user_id == self.request.user.id,
            'thanks_list': thanks_list,
        })

        return context


class EditThanksView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Thanks
    template_name = 'thanks/thanks_edit.html'
    fields = ('title', 'content', 'photo')

    def get_success_url(self):
        return reverse_lazy('thanks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thanks_list = list(Thanks.objects.filter(user_id=self.object.user_id))

        context.update({

            'is_owner': self.object.user_id == self.request.user.id,
            'thanks_list': thanks_list,
        })

        return context


class DeleteThanksView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = Thanks
    template_name = 'thanks/thanks_delete.html'

    def get_success_url(self):
        return reverse_lazy('thanks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thanks_list = list(Thanks.objects.filter(user_id=self.object.user_id))

        context.update({

            'is_owner': self.object.user_id == self.request.user.id,
            'thanks_list': thanks_list,
        })

        return context


class MyThanksView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Thanks
    template_name = 'thanks/my_thanks_list.html'
    context_object_name = 'thanks'

    def get_queryset(self):
        return Thanks.objects.filter(user=self.request.user.profile)
