from crm.models import Navbar, NavbarItem
from rest_framework import serializers


class NavbarItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavbarItem
        fields = '__all__'


class NavbarSerializer(serializers.ModelSerializer):
    items = NavbarItemSerializer(read_only=True, many=True)
    class Meta:
        model = Navbar 
        fields = '__all__'

