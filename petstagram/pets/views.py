from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from petstagram.pets.forms import PetForm, PetDeleteForm
from petstagram.pets.models import Pet


# Create your views here.


def add_pet(request):
    if request.method == 'GET':
        form = PetForm()
    else:
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk=1)

    context = {
        'form': form,
    }

    return render(request, template_name='pets/pet-add-page.html', context=context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('profile details', pk=1)
    form = PetDeleteForm(initial=pet.__dict__)

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-delete-page.html', context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details_pet', username=username, pet_slug=pet_slug)
    context = {
        'form': form,
    }
    return render(request, 'pets/pet-edit-page.html', context)


def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos,
        # 'photos_count': pet.photos_set.count(),
    }

    return render(request, 'pets/pet-details-page.html', context)
