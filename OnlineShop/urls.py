"""OnlineShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from shop.views import *

from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token,verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),

    path('pay/', include('payment.urls')),
    path('cart', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('shop/', include('shop.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('signup/',SignUp, name='signup'),
    path('success/',Success, name='success'),
    path('contact/',Contact, name='contact'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # jwt authontication

    path('api-token-auth/', obtain_jwt_token),

    path('api-token-verify/', verify_jwt_token),

    # # Our Rest API  url.
    path('orderapi/', include('orders.api.urls')),
    path('shopapi/', include('shop.api.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

