from modeltranslation.translator import register, TranslationOptions

from .models import City, Gallery, Attractions




@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ['name']


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ['title']


@register(Attractions)
class AttractionsTranslationOptions(TranslationOptions):
    fields = ['title']

