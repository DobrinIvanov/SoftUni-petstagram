from django.shortcuts import render

from petstagram.photos.models import Photo


# Create your views here.


# Home page view customization
def index(request):
    all_photos = Photo.objects.all()

    context = {
        "all_photos": all_photos,
    }

    return render(request, template_name='common/home-page.html', context=context)
