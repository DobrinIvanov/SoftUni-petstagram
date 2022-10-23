from django.urls import path

from petstagram.common import views
from petstagram.common.views import index

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:photo_id>', views.like_functionality, name='like'),
    path('testing', views.testing_view, name='testing')
)

