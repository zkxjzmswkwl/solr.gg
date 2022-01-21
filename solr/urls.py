from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from esports.views import TeamViewSet, PlayerViewSet, GameViewSet
from crm.views import NavbarViewSet, NavbarItemViewSet

admin.site.site_header = "Solaris"

r = routers.DefaultRouter()
r.register(r'teams', TeamViewSet)
r.register(r'players', PlayerViewSet)
r.register(r'games', GameViewSet)
r.register(r'navbars', NavbarViewSet)
r.register(r'navbaritems', NavbarItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(r.urls))
]

urlpatterns += r.urls