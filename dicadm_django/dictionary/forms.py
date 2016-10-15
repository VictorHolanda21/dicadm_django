from django import forms

from .models import Word, Category


class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128, label="Nome", help_text="Por favor, entre com um nome para categoria.")

	class Meta:
		model = Category
		fields = ('name',)	

class WordForm(forms.ModelForm):
	category = forms.Select()
	title = forms.CharField(max_length=128,
			label="Nome:",
			widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': "Por favor, entre com o nome da palavra."})
			)

	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': "Por favor, entre com a descrição da palavra."}),
			label="Descrição:"
			)

	class Meta:
		model = Word

		fields = ('category', 'title', 'description')