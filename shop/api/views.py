
from shop.models import Category,Product
from shop.api.serializers import CategorySerializer,ProductSerializer,UserSerializer,GroupSerializer
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from shop.pagination import MyPagination

from rest_framework.permissions import IsAuthenticated,IsAdminUser

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    pagination_class = MyPagination

    permission_classes = (IsAuthenticated,IsAdminUser,)
    authentication_classes = (JSONWebTokenAuthentication,)




class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = MyPagination

    permission_classes = (IsAuthenticated,IsAdminUser,)
    authentication_classes = (JSONWebTokenAuthentication,)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset =Category.objects.all()
    serializer_class =CategorySerializer
    pagination_class = MyPagination

    permission_classes = (IsAuthenticated,IsAdminUser,)
    authentication_classes = (JSONWebTokenAuthentication,)

class ProductViewSet(viewsets.ModelViewSet):
    queryset =Product.objects.all()
    serializer_class =ProductSerializer
    pagination_class = MyPagination

    permission_classes = (IsAuthenticated,IsAdminUser,)
    authentication_classes = (JSONWebTokenAuthentication,)



