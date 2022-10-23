from django.shortcuts import render

from petstagram.photos.models import Photo


# Create your views here.


def add_photo(request):
    return render(request, 'photos/photo-add-page.html')


def details_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo_likes = photo.like_set.all()
    photo_comments = photo.comment_set.all()

    context = {
        'photo': photo,
        'photo likes': photo_likes,
        'photo_comments': photo_comments,
    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    return render(request, 'photos/photo-edit-page.html')
