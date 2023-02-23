from django.urls import path
from django.urls import include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('notes/', login_required(views.home), name='notes'),       # for adding a new book
    path('notes/search/', views.search_note, name='search_note'),
    path('notes/<slug:slug>/', login_required(views.get_note_details), name='note_detail'),
    path('notes/<int:pk>/delete/', login_required(views.delete_note), name='delete_single_note'),
    path('notes/<int:pk>/delete/confirm/', login_required(views.confirm_delete_note), name='confirm_delete_note'),
    path('notes/<int:pk>/edit/', login_required(views.edit_note_details), name='note_details_edit'),
    path('notes/<slug:slug>/pdf/', login_required(views.generate_pdf), name='note_as_pdf'),
    path('notes/share/<str:signed_pk>/', views.get_shareable_link, name='share_notes'),
    path('tags/<slug:slug>/', views.get_all_notes_tags, name='get_all_notes_tags'),
    path('', views.home, name='home')
]