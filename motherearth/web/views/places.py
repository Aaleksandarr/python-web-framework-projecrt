from django.contrib.auth import mixins as auth_mixin
from django.urls import reverse_lazy
from django.views import generic as views
from motherearth.web.models import Places


class CreatePlaceView(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = Places
    template_name = 'places/place_create.html'
    fields = ('name', 'categories', 'address', 'description', 'phone_number', 'photo')
    success_url = reverse_lazy('places')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)


class PlaceDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Places
    template_name = 'places/place_details.html'
    context_object_name = 'place'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        places = list(Places.objects.filter(owner_id=self.object.owner_id))

        context.update({

            'is_owner': self.object.owner_id == self.request.user.id,
            'places': places,
        }
        )

        return context


class EditPlaceView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Places
    template_name = 'places/place_edit.html'
    fields = ('name', 'categories', 'address', 'description', 'phone_number')

    def get_success_url(self):
        return reverse_lazy('places')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        places = list(Places.objects.filter(owner_id=self.object.owner_id))
        context.update({

            'is_owner': self.object.owner_id == self.request.user.id,
            'places': places,
        }
        )

        return context


class DeletePlaceView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = Places
    template_name = 'places/place_delete.html'

    def get_success_url(self):
        return reverse_lazy('places')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        places = list(Places.objects.filter(owner_id=self.object.owner_id))

        context.update({

            'is_owner': self.object.owner_id == self.request.user.id,
            'places': places,
        }
        )

        return context


class MyPlacesView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Places
    template_name = 'places/my_places_list.html'
    context_object_name = 'places'

    def get_queryset(self):
        return Places.objects.filter(owner=self.request.user.profile)
