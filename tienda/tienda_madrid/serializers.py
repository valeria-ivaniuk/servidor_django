from rest_framework import serializers
from .models import Tienda

class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = '__all__'

    def validate_ciudad(self, value):
        if value != 'Madrid':
            raise serializers.ValidationError("La tienda debe estar ubicada en Madrid.")
        return value