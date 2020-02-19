
from django.urls import path,include
from shop.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('shop', views.CategoryViewSet)
router.register('shop/', views.ProductViewSet)
router.register('users', views.UserViewSet)
router.register('Group', views.GroupViewSet)


urlpatterns = [
    path('',include(router.urls))
]




