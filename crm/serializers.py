from crm.models import Navbar, NavbarItem
from rest_framework import serializers


class NavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbar 
        fields = '__all__'


class NavbarItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavbarItem
        fields = '__all__'
