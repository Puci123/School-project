from django.contrib import admin
from .models import Tag, Game, GameList, Review



# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "release_date",)
    prepopulated_fields = {"slug": ("title",)}


class GameListAdmin(admin.ModelAdmin):
    list_display = ("title", "user",)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "game", "created_at")



admin.site.register(Tag, admin.ModelAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(GameList, GameListAdmin)
admin.site.register(Review, ReviewAdmin)