from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import redirect
from django.views import generic as views
from motherearth.web.models import Post, Plants


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


class CommunityView(views.TemplateView):
    template_name = 'main/community_view.html'


class MarketListView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Plants
    template_name = 'main/market.html'
    context_object_name = 'plants'
    ordering = ['-publication_date']


