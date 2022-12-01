from rest_framework import serializers
from main.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Contact
        # fields = '__all__'
        exclude = ["user"]




