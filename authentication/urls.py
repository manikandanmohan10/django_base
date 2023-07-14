from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('generic/', views.Generic.as_view(), name='generic'),
    path('book/', views.BookAPI.as_view(), name='book'),
    path('deleteUser/', views.DeleteUser.as_view(), name="delete_user"),
    path('userProfile/', views.UserProfileAPI.as_view(), name="user_profile"),
    path('library/', views.LibraryAPI.as_view(), name="library"),
    path('librarySubscription/', views.LibrarySubscriptionAPI.as_view(), name="library_subscription"),

]