from django.contrib import admin
from blog.models import BlogPost, Art, Category

# Register your models here.
#class CategoryAdmin(admin.ModelAdmin):
 #   prepopulated_fields = {'slug': ('label',)}


class ArtAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'created', 'modified')
    search_fields = ('name', 'description')
    list_filter = ( 'created', 'modified')
    prepopulated_fields = {'slug': ('name',)}

class ArtInline(admin.TabularInline):
    model = Art

class BlogPostAdmin(admin.ModelAdmin):
    inlines = [ArtInline]

admin.site.register(BlogPost, BlogPostAdmin)

admin.site.register(Art, ArtAdmin)

#admin.site.register(Category, CategoryAdmin)
