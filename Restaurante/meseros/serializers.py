
from rest_framework import serializers
from .models import Mesero

class MeseroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesero
        fields = ['id', 'nombre', 'nacionalidad', 'edad', 'dni']
