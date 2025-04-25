# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('books/', views.all_books, name='all_books'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('create/book/', views.create_book, name='create_book'),
    path('delete/book/<int:book_id>/confirm/', views.confirm_delete_book, name='confirm_delete_book'),
    path('create/author/', views.create_author, name='create_author'),
    path('create/genre/', views.create_genre, name='create_genre'),
    path('authors/', views.all_authors, name='all_authors'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('delete/author/<int:author_id>/confirm/', views.confirm_delete_author, name='confirm_delete_author'),
    path('genres/', views.all_genres, name='all_genres'),
    path('genre/<int:genre_id>/', views.genre_books, name='genre_books'),
    path('delete/genre/<int:genre_id>/confirm/', views.confirm_delete_genre, name='confirm_delete_genre'),

    path('search/', views.search_by_genre, name='search_by_genre'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('best_reads/', views.best_reads, name='best_reads'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
 
 
    
   
]
