
from django.urls import path,include
from orders.api import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('orders', views.orderViewSet)
router.register('orders/', views.orderitemViewSet)

urlpatterns = [
    path('',include(router.urls))
]