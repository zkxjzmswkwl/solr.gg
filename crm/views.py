from django.shortcuts import render
from rest_framework import viewsets
from crm.models import NavbarItem, Navbar
from crm.serializers import NavbarSerializer, NavbarItemSerializer


class NavbarViewSet(viewsets.ModelViewSet):
    queryset = Navbar.objects.all()
    serializer_class = NavbarSerializer


class NavbarItemViewSet(viewsets.ModelViewSet):
    queryset = NavbarItem.objects.all()
    serializer_class = NavbarItemSerializer
