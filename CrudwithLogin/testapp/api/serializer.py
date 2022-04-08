from http.client import IM_USED
import imp
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from testapp.models import Book

class BookSerializer(ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'