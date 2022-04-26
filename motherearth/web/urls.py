from django.urls import path
from motherearth.web.views.events import CreateEventView, EventDetailsView, EditEventView, DeleteEventView, MyEventsView
from motherearth.web.views.main import HomeView, DashboardView, CommunityView, MarketListView, InternalErrorView, \
    ProductsListView, PlacesListView, EventsListView, ThanksListView
from motherearth.web.views.places import CreatePlaceView, PlaceDetailsView, EditPlaceView, DeletePlaceView, MyPlacesView
from motherearth.web.views.plants import CreatePlantView, MarketPlantsDetailsView, EditMarketPlantView, \
    DeleteMarketPlantView, MyPlantsView
from motherearth.web.views.posts import CreateDashboardPost, EditDashboardPostView, DeleteDashboardPostView, \
    DashboardPostDetailsView, MyPostsView
from motherearth.web.views.products import CreateProductView, EditProductView, DeleteProductView, ProductDetailsView, \
    MyProductView


urlpatterns = (
    path('', HomeView.as_view(), name='index'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('post/create/', CreateDashboardPost.as_view(), name='create post'),
    path('post/edit/<int:pk>/', EditDashboardPostView.as_view(), name='edit post'),
    path('post/delete/<int:pk>/', DeleteDashboardPostView.as_view(), name='delete post'),
    path('post/details/<int:pk>/', DashboardPostDetailsView.as_view(), name='post details'),
    path('post/mine/', MyPostsView.as_view(), name='my posts'),

    path('community/', CommunityView.as_view(), name='community view'),

    path('market/', MarketListView.as_view(), name='market'),
    path('plant/create/', CreatePlantView.as_view(), name='create plant'),
    path('plant/details/<int:pk>/', MarketPlantsDetailsView.as_view(), name='plant details'),
    path('plant/edit/<int:pk>/', EditMarketPlantView.as_view(), name='edit plant'),
    path('plant/delete/<int:pk>/', DeleteMarketPlantView.as_view(), name='delete plant'),
    path('plant/mine/', MyPlantsView.as_view(), name='my plants'),

    path('product/', ProductsListView.as_view(), name='products'),
    path('product/create/', CreateProductView.as_view(), name='create product'),
    path('product/details/<int:pk>/', ProductDetailsView.as_view(), name='product details'),
    path('product/edit/<int:pk>/', EditProductView.as_view(), name='edit product'),
    path('product/delete/<int:pk>/', DeleteProductView.as_view(), name='delete product'),
    path('product/mine/', MyProductView.as_view(), name='my products'),

    path('place/', PlacesListView.as_view(), name='places'),
    path('place/create/', CreatePlaceView.as_view(), name='create place'),
    path('place/details/<int:pk>/', PlaceDetailsView.as_view(), name='place details'),
    path('place/edit/<int:pk>/', EditPlaceView.as_view(), name='edit place'),
    path('place/delete/<int:pk>/', DeletePlaceView.as_view(), name='delete place'),
    path('place/mine/', MyPlacesView.as_view(), name='my places'),

    path('event/', EventsListView.as_view(), name='events'),
    path('event/create/', CreateEventView.as_view(), name='create event'),
    path('event/details/<int:pk>/', EventDetailsView.as_view(), name='event details'),
    path('event/edit/<int:pk>/', EditEventView.as_view(), name='edit event'),
    path('event/delete/<int:pk>/', DeleteEventView.as_view(), name='delete event'),
    path('event/mine/', MyEventsView.as_view(), name='my events'),

    path('thanks/', ThanksListView.as_view(), name='thanks'),

    path('error', InternalErrorView.as_view(), name='error')
)

