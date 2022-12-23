from django.shortcuts import render, redirect
from .models import Game
from .forms import GameForm
from .serializers import GameSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

def index(request):
    games = Game.objects.all()
    return render(request, 'index.html', {'games':games})

def add_game(request):
    form = GameForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return games_list_manage(request)
    return render(request, 'add_game.html', {'form':form})

def games_list_manage(request):
    games = Game.objects.all()
    return render(request, 'manage_games.html', {'games': games})

def delete_game(request, id):
    game = Game.objects.get(id = id)
    game.delete()
    return games_list_manage(request)

def update_game(request, id):
    game = Game.objects.get(id = id)
    form = GameForm(instance=game)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            game.delete()
            form.save()
        return games_list_manage(request)
    return render(request, 'add_game.html', {'form': form})

class GamesList(APIView):
    def get(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)