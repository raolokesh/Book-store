from django.contrib import admin

from .models import Book,Author

# Register your models here.

class Bookadmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    # prepopulated_fields = { "slug": ("title",)}
    list_filter = ("author","rating")
    list_display = ("title","author","rating")

class Authoradmin(admin.ModelAdmin):
    pass
    






admin.site.register(Book,Bookadmin)
admin.site.register(Author)