from html5lib import serialize
from rest_framework.viewsets import ModelViewSet
from testapp.api.serializer import BookSerializer
from testapp.models import Book
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


class BookView(ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    authentication_classes=[JSONWebTokenAuthentication,]
    permission_classes=[IsAuthenticated,]