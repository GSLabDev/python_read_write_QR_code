from django.contrib import admin
from .models import Code


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    # list_filter = ("status",)
    search_fields = ['title', 'content']
    # prepopulated_fields = {'slug': ('title',)}



admin.site.register(Code, PostAdmin)
