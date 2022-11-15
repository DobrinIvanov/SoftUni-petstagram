from django.urls import path

from petstagram.common.views import index, like_functionality, copy_link_to_clipboard, testing_view, add_comment

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:photo_id>/', like_functionality, name='like'),
    path('share/<int:photo_id>/', copy_link_to_clipboard, name='share'),
    path('testing/', testing_view, name='testing'),
    path('comment/<int:photo_id>/', add_comment, name='comment'),
)

