from django.contrib import admin
from .models import Blog, Tags

# Register your models here.
# admin.site.register(Profile)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'choices']
    search_fields = ['title', 'body'] 
    prepopulated_fields = {'slug':('title',)} 
    raw_id_fields = ['author'] 
    date_hierarchy = 'publish'
    ordering = ['choices', 'publish']
    show_facets = admin.ShowFacets.ALWAYS

admin.site.register(Tags)