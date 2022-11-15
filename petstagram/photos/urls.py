from django.urls import path, include
from petstagram.photos.views import details_photo, edit_photo, add_photo, delete_photo

urlpatterns = (
    path('add/', add_photo, name='add_photo'),
    path('<int:pk>/', details_photo, name='details_photo'),
    path('edit/<int:pk>/', edit_photo, name='edit_photo'),
    path('delete/<int:pk>/', delete_photo, name='delete_photo')
)
