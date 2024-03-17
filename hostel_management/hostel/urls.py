from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login/', views.login, name='login'),
    path('stays/', views.stays, name="stays"),
    path('bookings/', views.bookings, name="bookings"),
    path('signup/', views.signup, name="signup"),
    path('book_room', views.book_room, name='book_room'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
]