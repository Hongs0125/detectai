<<<<<<< HEAD
from rest_framework import serializers
from detectFruits.models import detectFruits


class detectserializer(serializers.ModelSerializer):
    class Meta:
        model = detectFruits
=======
from rest_framework import serializers
from detectFruits.models import detectFruits


class detectserializer(serializers.ModelSerializer):
    class Meta:
        model = detectFruits
>>>>>>> e83ef521bec72ef685a6831704f6653aff170d6f
        fields = '__all__'