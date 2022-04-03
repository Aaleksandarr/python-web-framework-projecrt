from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from motherearth.auth_app.views import UserLoginView, UserRegisterView, ProfileDetailsView, ChangeUserPasswordView, \
    EditProfileView, UserLogoutView, DeleteUserView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('register/', UserRegisterView.as_view(), name='register'),

    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('profile/delete/<int:pk>/', DeleteUserView.as_view(), name='delete user'),

    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_change_done'),

)
