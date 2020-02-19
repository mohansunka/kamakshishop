from . import views
from django.urls import path

urlpatterns = [
        path('charge/', views.charge, name='charge'),
# new
        path('', views.HomePageView.as_view(), name='home'),
]
