from django.contrib import admin
from .models import Advert

class AdvertAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_time', 'updated_time', 'auction']
    list_filter = ['auction', 'create_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общие', {
            'fields': ('title', 'description')
        }),
        ('Финансы', {
            'fields': ('price', 'auction')
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Advert, AdvertAdmin)