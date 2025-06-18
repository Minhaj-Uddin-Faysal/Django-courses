from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('addBook/',views.add_book,name='add_book'),
    path('delete/<int:id>/',views.deleteBook,name='delete_book'),
    path('search/',views.search_book,name='search_book'),
    path('commentpost/<str:title>/',views.commentpost,name='commentpost'),
    path('reviews/<str:title>/',views.reviews,name='reviews'),

]