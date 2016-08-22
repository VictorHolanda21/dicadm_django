from django.contrib import admin

# Register your models here.

from .models import Word

class WordAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'created_at', 'updated_at']
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ['updated_at', 'created_at']
	search_fields = ['title', 'description']

	class Meta:
		model = Word

admin.site.register(Word, WordAdmin)