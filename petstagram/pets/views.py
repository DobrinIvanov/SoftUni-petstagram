from django.shortcuts import render

from petstagram.pets.models import Pet


# Create your views here.


def add_pet(request):
    return render(request, 'pets/pet-add-page.html')


def delete_pet(request, username, pet_name):
    return render(request, 'pets/pet-delete-page.html')


def edit_pet(request, username, pet_name):
    return render(request, 'pets/pet-edit-page.html')


def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    pet_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'pet_photos': pet_photos,
        'photos_count': pet.photos_set.count(),
    }

    return render(request, 'pets/pet-details-page.html', context)
