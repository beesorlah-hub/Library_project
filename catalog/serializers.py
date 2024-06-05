from rest_framework import serializers
from .models import Author, Publisher, Book, Borrower, Loan


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = ['title','isbn', 'publication_date', 'page_count','author','publisher']

    def create(self, validated_data):
        author_data = validated_data.pop("author")
        publisher_data = validated_data.pop("publisher")

        author, created = Author.objects.get_or_create(**author_data)
        print(f'was author created ----> {created}')
        publisher, created = Publisher.objects.get_or_create(**publisher_data)
        print(f'was publisher created ----> {created}')

        book = Book.objects.create(author=author, publisher=publisher, **validated_data)
        return(book)
    
    def update(self, instance, validated_data):
        author_data = validated_data.pop("author")
        publisher_data = validated_data.pop("publisher")

        author, created = Author.objects.get_or_create(**author_data)
        publisher, created = Publisher.objects.get_or_create(**publisher_data)

        instance.author = author
        instance.publisher = publisher
        instance.title = validated_data.get('title', instance.title)
        instance.publication_date = validated_data.get("publication_date",instance.title)
        instance.save()
        return instance


class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), many=True)
    borrower = serializers.PrimaryKeyRelatedField(queryset=Borrower.objects.all(), many=True)
        
    class Meta:
        model = Loan
        fields = '__all__'


