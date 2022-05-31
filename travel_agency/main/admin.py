from django.contrib import admin

from .models import Contact, City, Gallery, Attractions

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone")
    search_fields = ("full_name", "message")


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(Attractions)
class AttractionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)

