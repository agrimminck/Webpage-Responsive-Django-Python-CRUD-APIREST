"""PaginaVideojuegos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.urls import path
from General import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add-game', views.add_game, name = 'add_game'),
    path('manage-games', views.games_list_manage, name='manage_games'),
    path('delete-game/<int:id>', views.delete_game, name='delete_game'),
    path('update-game/<int:id>', views.update_game, name='update_game'),
    path('games/', views.GamesList.as_view(), name='games_api'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
