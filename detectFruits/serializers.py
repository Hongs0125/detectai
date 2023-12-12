from rest_framework import serializers
from detectFruits.models import detectFruits


class detectserializer(serializers.ModelSerializer):
    class Meta:
        model = detectFruits
        fields = '__all__'