from django.contrib import admin

# Register your models here.

from .models import Word, Category

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'created_at', 'updated_at']
	prepopulated_fields = {'slug': ('name',)}
	list_filter = ['updated_at', 'created_at']
	search_fields = ['name']

	class Meta:
		model = Category

		verbose_name = "Categoria"
		verbose_name_plural = 'Categorias'

		def __str__(self):
			return self.name


class WordAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'category', 'created_at', 'updated_at']
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ['updated_at', 'created_at', 'category']
	search_fields = ['title', 'description', 'category']

	class Meta:
		model = Word

		verbose_name = "Palavra"
		verbose_name_plural = "Palavras"

		def __str__(self):
			return self.name

admin.site.register(Word, WordAdmin)
admin.site.register(Category, CategoryAdmin)