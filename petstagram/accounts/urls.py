from django.urls import path, include

from petstagram.accounts import views
from petstagram.accounts.views import UserRegisterView, UserLoginView, UserLogoutView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('register/', UserRegisterView.as_view(), name='register user'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', views.details_user, name='profile details'),
        path('edit/', views.edit_user, name='profile edit'),
        path('delete/', views.delete_user, name='profile delete'),
        ])),
)
