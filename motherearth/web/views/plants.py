from django.contrib.auth import mixins as auth_mixin
from django.urls import reverse_lazy
from django.views import generic as views
from motherearth.web.models import Plants


class CreatePlantView(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = Plants
    template_name = 'plants/plant_create.html'
    fields = ('kind', 'type', 'description', 'photo', 'price')
    success_url = reverse_lazy('market')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)


class MarketPlantsDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Plants
    template_name = 'plants/plant_details.html'
    context_object_name = 'plant'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plants = list(Plants.objects.filter(owner_id=self.object.owner_id))

        context.update({

            'is_owner': self.object.owner_id == self.request.user.id,
            'plants': plants,
        })

        return context


class EditMarketPlantView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Plants
    template_name = 'plants/plant_edit.html'
    fields = ('kind', 'type', 'photo', 'description', 'price')

    def get_success_url(self):
        return reverse_lazy('market')


class DeleteMarketPlantView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = Plants
    template_name = 'plants/plant_delete.html'

    def get_success_url(self):
        return reverse_lazy('market')


class MyPlantsView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Plants
    template_name = 'plants/my_plants_list.html'
    context_object_name = 'plants'

    def get_queryset(self):
        return Plants.objects.filter(owner=self.request.user.profile)