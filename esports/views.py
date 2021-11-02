from django.shortcuts import render
from rest_framework import viewsets
from esports.models import Team, Game, Player
from esports.serializers import TeamSerializer, PlayerSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer