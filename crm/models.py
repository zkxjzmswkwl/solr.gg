from django.db import models


class NavbarItem(models.Model):
    display = models.CharField(max_length=64)
    takes_to = models.CharField(max_length=64)
    icon = models.CharField(max_length=64, default="None")

    def __str__(self):
        return self.display


class Navbar(models.Model):
    items = models.ManyToManyField(NavbarItem)