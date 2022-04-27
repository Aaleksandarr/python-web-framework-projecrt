from django.contrib.auth import mixins as auth_mixin
from django.urls import reverse_lazy
from django.views import generic as views
from motherearth.web.models import Event


class CreateEventView(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = Event
    template_name = 'events/event_create.html'
    fields = ('name', 'date', 'description', 'photo', 'location')
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)


class EventDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Event
    template_name = 'events/event_details.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = list(Event.objects.filter(owner_id=self.object.owner_id))

        context.update({

            'is_owner': self.object.owner_id == self.request.user.id,
            'events': events,
        }
        )

        return context


class EditEventView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Event
    template_name = 'events/event_edit.html'
    fields = ('name', 'date', 'description', 'photo', 'location')

    def get_success_url(self):
        return reverse_lazy('event')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = list(Event.objects.filter(owner_id=self.object.owner_id))
        context.update({

            'is_owner': self.object.owner_id == self.request.user.id,
            'events': events,
        }
        )

        return context


class DeleteEventView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = Event
    template_name = 'events/event_delete.html'

    def get_success_url(self):
        return reverse_lazy('events')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = list(Event.objects.filter(owner_id=self.object.owner_id))

        context.update({

            'is_owner': self.object.owner_id == self.request.user.id,
            'events': events,
        }
        )

        return context


class MyEventsView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Event
    template_name = 'events/my_events_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(owner=self.request.user.profile)
