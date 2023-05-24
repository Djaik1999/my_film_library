from django.contrib import admin

from .models import Movie, Genre, CastMember, CastMemberComment


class MovieAdmin(admin.ModelAdmin):
    list_filter = ("title", "year")
    search_fields = ["title", "comments"]
    prepopulated_fields = {"slug": ("title", "year")}


class CastMemberAdmin(admin.ModelAdmin):
    search_fields = ("name", )
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Movie, MovieAdmin)
admin.site.register(CastMember, CastMemberAdmin)
admin.site.register(CastMemberComment)
admin.site.register(Genre)

