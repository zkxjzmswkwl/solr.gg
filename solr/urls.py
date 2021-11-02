from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from esports.views import TeamViewSet, PlayerViewSet

r = routers.DefaultRouter()
r.register(r'teams', TeamViewSet)
r.register(r'players', PlayerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(r.urls))
]

urlpatterns += r.urls