from rest_framework import serializers
from .models import Imagen,Producto

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = ['id','imagen']
        
class ProductoSerializer(serializers.ModelSerializer):
    imagenes = ImagenSerializer(many=True,read_only=True)
    class Meta:
        model = Producto
        fields = ['id','nombre','detalle','fecha_creacion','imagenes']