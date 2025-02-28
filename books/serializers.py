from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields =['id','name', 'birthday', 'biography']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model= Book
        fields = ['id', 'title', 'pub_date', 'synopsis', 'author']