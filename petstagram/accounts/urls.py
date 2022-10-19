from django.urls import path, include

from petstagram.accounts import views

urlpatterns = (
    path('login/', views.login_user, name='login user'),
    path('register/', views.register_user, name='register user'),
    path('profile/<int:pk>/', include([
        path('', views.details_user, name='profile details'),
        path('edit/', views.edit_user, name='profile edit'),
        path('delete/', views.delete_user, name='profile delete'),
        ])),
)
