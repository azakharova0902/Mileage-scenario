from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register('cars', views.CarsView)
router.register('logs', views.LogsView)

urlpatterns = [
    path('', include(router.urls)),
]

