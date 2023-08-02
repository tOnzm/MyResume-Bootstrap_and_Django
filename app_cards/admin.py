from django.contrib import admin
from app_cards.models import Cards

# Register your models here.
class CardsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Cards,CardsAdmin)