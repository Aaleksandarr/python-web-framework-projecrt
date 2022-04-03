from django.urls import path
from motherearth.web.views.main import HomeView, DashboardView, CommunityView, MarketListView
from motherearth.web.views.plants import CreatePlantView, MarketPlantsDetailsView, EditMarketPlantView, \
    DeleteMarketPlantView, MyPlantsView
from motherearth.web.views.posts import CreateDashboardPost, EditDashboardPostView, DeleteDashboardPostView, \
    DashboardPostDetailsView, MyPostsView


urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('post/create/', CreateDashboardPost.as_view(), name='create post'),
    path('post/edit/<int:pk>/', EditDashboardPostView.as_view(), name='edit post'),
    path('post/delete/<int:pk>', DeleteDashboardPostView.as_view(), name='delete post'),
    path('post/details/<int:pk>/', DashboardPostDetailsView.as_view(), name='post details'),
    path('post/mine', MyPostsView.as_view(), name='my posts'),

    path('community/', CommunityView.as_view(), name='community view'),

    path('market/', MarketListView.as_view(), name='market'),
    path('plants/create/', CreatePlantView.as_view(), name='create plant'),
    path('plant/details/<int:pk>/', MarketPlantsDetailsView.as_view(), name='plant details'),
    path('plant/edit/<int:pk>/', EditMarketPlantView.as_view(), name='edit plant'),
    path('plant/delete/<int:pk>/', DeleteMarketPlantView.as_view(), name='delete plant'),
    path('plants/mine', MyPlantsView.as_view(), name='my plants'),
)

