from django.contrib import admin

from petstagram.pets.models import Pet

# Register your models here.

<<<<<<< HEAD

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
=======
admin.site.register(Pet)


# @admin.register(Pet)
# class PetAdmin(admin.ModelAdmin):
#     pass
>>>>>>> 8e1afc06f53edfc287e72bbbbbf2140374ac116c
