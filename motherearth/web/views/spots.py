from django.contrib.auth import mixins as auth_mixin
from django.urls import reverse_lazy
from django.views import generic as views
from motherearth.web.models import Spots


class CreateSpotView(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = Spots
    template_name = 'spots/spot_create.html'
    fields = ('name', 'categories', 'address', 'description', 'phone_number', 'photo')
    success_url = reverse_lazy('spots')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)


class SpotDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Spots
    template_name = 'spots/spot_details.html'
    context_object_name = 'spot'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        spots = list(Spots.objects.filter(owner_id=self.object.owner_id))

        context.update({

            'is_owner': self.object.owner_id == self.request.user.id,
            'spots': spots,
        }
        )

        return context


class EditSpotView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Spots
    template_name = 'spots/spot_edit.html'
    fields = ('name', 'categories', 'address', 'description', 'phone_number')

    def get_success_url(self):
        return reverse_lazy('spots')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        spots = list(Spots.objects.filter(owner_id=self.object.owner_id))
        context.update({

            'is_owner': self.object.owner_id == self.request.user.id,
            'spots': spots,
        }
        )

        return context


class DeleteSpotView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = Spots
    template_name = 'spots/spot_delete.html'

    def get_success_url(self):
        return reverse_lazy('spots')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        spots = list(Spots.objects.filter(owner_id=self.object.owner_id))

        context.update({

            'is_owner': self.object.owner_id == self.request.user.id,
            'spots': spots,
        }
        )

        return context


class MySpotsView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Spots
    template_name = 'spots/my_spots_list.html'
    context_object_name = 'spots'

    def get_queryset(self):
        return Spots.objects.filter(owner=self.request.user.profile)
