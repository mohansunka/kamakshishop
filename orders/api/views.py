from orders.models import OrderItem,Order,Product
from orders.api.serializers import OrderSerializer,OrderItemSerializer
from rest_framework import viewsets
from orders.pagination import MyPagination

from rest_framework.permissions import IsAuthenticated,IsAdminUser

from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class orderViewSet(viewsets.ModelViewSet):
    queryset =Order.objects.all()
    serializer_class =OrderSerializer
    pagination_class = MyPagination

    permission_classes = (IsAuthenticated,IsAdminUser,)
    authentication_classes = (JSONWebTokenAuthentication,)

class orderitemViewSet(viewsets.ModelViewSet):
    queryset =OrderItem.objects.all()
    serializer_class =OrderItemSerializer
    pagination_class = MyPagination

    permission_classes = (IsAuthenticated,IsAdminUser,)
    authentication_classes = (JSONWebTokenAuthentication,)


