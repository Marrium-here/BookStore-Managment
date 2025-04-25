from django import forms
from .models import Author, Genre, Book

# Form for creating and updating authors
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']

# Form for creating and updating genres
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'description']

# Form for creating and updating books
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'description', 'cover_image', 'best_read']


