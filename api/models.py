from django.db import models

class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.CharField(max_length=50)

class Factura(models.Model):
    fecha = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)

class Producto(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio_compra = models.FloatField()
    precio_venta= models.FloatField()
    stock = models.IntegerField()
    categoria  = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Detalle(models.Model):
    class Meta:
        unique_together = (('num_detalle', 'factura'),)
    num_detalle = models.IntegerField()
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.FloatField()
