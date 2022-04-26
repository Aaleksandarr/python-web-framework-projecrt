from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import redirect, render
from django.views import generic as views
from motherearth.web.models import Post, Plants, Type, Kind, Product, Places, Event, Craft, Thanks


class HomeView(views.TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class DashboardView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Post
    template_name = 'main/dashboard.html'
    context_object_name = 'posts'
    ordering = ['-publication_date']
    last_event = Event.objects.last()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_event = Event.objects.last()
        context.update({
            'last_event': last_event,
            })

        return context


class CommunityView(views.TemplateView):
    template_name = 'main/community_view.html'


class MarketListView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Plants
    template_name = 'main/market.html'
    context_object_name = 'plants'
    fields = ('kind', 'type')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        type_list = Type.objects.all()
        kind_list = Kind.objects.all()
        context.update({
            'request': request,
            'type_list': type_list,
            'kind_list': kind_list
        }
        )

        return context

    def get_queryset(self):
        if self.request.GET:
            name = list(self.request.GET.values())[1]
            filter_id = Type.objects.get(name=name).id
            return Plants.objects.filter(type__id=filter_id).order_by('-publication_date')
        else:
            return Plants.objects.all().order_by('-publication_date')


class ProductsListView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Product
    template_name = 'main/products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        craft_list = Craft.objects.all()
        context.update({
            'request': request,
            'craft_list': craft_list,
        }
        )

        return context

    def get_queryset(self):
        if self.request.GET:
            name = list(self.request.GET.values())[1]
            filter_id = Craft.objects.get(name=name).id
            return Product.objects.filter(craft__id=filter_id).order_by('-publication_date')
        else:
            return Product.objects.all().order_by('-publication_date')


class PlacesListView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Places
    template_name = 'main/places.html'
    context_object_name = 'places'
    ordering = ['-publication_date']


class EventsListView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Event
    template_name = 'main/events.html'
    context_object_name = 'events'
    ordering = ['-publication_date']


class ThanksListView(auth_mixin.LoginRequiredMixin, views.ListView):
    template_name = 'main/thanks.html'
    model = Thanks
    context_object_name = 'thanks'
    ordering = ['-publication_date']


class InternalErrorView(views.View):
    def get(self, request):
        return render(request, 'main/internal_error.html')
