from django.contrib.auth.models import User, Group
from api.models import *
from rest_framework import serializers

#with HyperlinkedModelSerializer. You can also use primary key and various other relationships, but hyperlinking is good RESTful design.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class  ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nombre', 'apellido','direccion','telefono','email')

class  FacturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Factura
        fields = ('id', 'fecha', 'cliente')

class  DetalleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Detalle
        fields = ('num_detalle', 'factura','producto','cantidad','precio')

class  ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('codigo', 'nombre', 'precio_compra','precio_venta','stock','categoria')

class  CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')
