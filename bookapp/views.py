from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import views as auth_views
from . models import Book  , Genre , Author
from . forms import BookForm , GenreForm , AuthorForm

# Home page view with links to login/signup
def home(request):
    genres = Genre.objects.all()
    return render(request, 'authentication/home.html' , {'genres': genres})

# Signup view (for creating a new user)
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful signup
            return redirect('home')  # Redirect to all books page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})

# Login view (for existing users)
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to all books page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'authentication/login.html')

# Custom logout view
def logout_view(request):
    logout(request)  # This logs out the user
    return redirect('home')  # Redirect to the home page after logging out


# View to list all books (only accessible to logged-in users)
@login_required
def all_books(request):
    # This is where you would fetch the books from the database and pass them to the template
    books = Book.objects.all()  # Retrieve all books
    return render(request, 'books/all_books.html', {'books': books})



# View for details of a specific book
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

# View for creating a new book (only accessible to logged-in users)
@login_required
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to all books page
    else:
        form = BookForm()
    return render(request, 'books/create_book.html', {'form': form})

# View for creating a new author (only accessible to logged-in users)
@login_required
def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to authors list after creation
    else:
        form = AuthorForm()
    return render(request, 'authors/create_author.html', {'form': form})

# View for creating a new genre (only accessible to logged-in users)
@login_required
def create_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to genres list after creation
    else:
        form = GenreForm()
    return render(request, 'genre/create_genre.html', {'form': form})

# View for details of a specific author
def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = Book.objects.filter(author=author)  # Books written by this author
    return render(request, 'authors/author_detail.html', {'author': author, 'books': books})

# View to list all genres
def all_genres(request):
    genres = Genre.objects.all()  # Fetch all genres
    return render(request, 'genre/all_genres.html', {'genres': genres})

def all_authors(request):
    authors = Author.objects.all()  # Fetch all genres
    return render(request, 'authors/all_authors.html', {'authors': authors})

# View to display books by a specific genre
def genre_books(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    books = Book.objects.filter(genre=genre)  # Fetch books by the specific genre
    return render(request, 'genre/genre_books.html', {'genre': genre, 'books': books})

def search_by_genre(request):
    genre_name = request.GET.get('genre_name', '')  # Get genre name from the query string
    books = []  # Start with an empty list of books
    
    # If genre_name is provided, filter the books by genre
    if genre_name:
        genre = Genre.objects.filter(name__icontains=genre_name).first()  # Case-insensitive search for genre
        if genre:
            books = Book.objects.filter(genre=genre)  # Filter books by the found genre

    return render(request, 'genre/search_by_genre.html', {'books': books, 'genre_name': genre_name})
def dashboard(request):
    # Fetch all books, authors, and genres
    books = Book.objects.all()
    authors = Author.objects.all()
    genres = Genre.objects.all()

    context = {
        'books': books,
        'authors': authors,
        'genres': genres,
    }
    return render(request, 'dashboard/dashboard.html', context)

def confirm_delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('dashboard')
    return render(request, 'dashboard/confirm_delete.html', {'item': book, 'type': 'book'})

def confirm_delete_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == 'POST':
        author.delete()
        return redirect('dashboard')
    return render(request, 'dashboard/confirm_delete.html', {'item': author, 'type': 'author'})

def confirm_delete_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    if request.method == 'POST':
        genre.delete()
        return redirect('dashboard')
    return render(request, 'dashboard/confirm_delete.html', {'item': genre, 'type': 'genre'})

def best_reads(request):
    best_reads = Book.objects.filter(best_read=True)  # Query for Best Reads
    return render(request, 'books/best_reads.html', {'best_reads': best_reads})

def about(request):
    return render(request, 'reachout/about.html')

def contact(request):
    return render(request, 'reachout/contact.html')