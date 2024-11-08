from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    detalle = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class Imagen(models.Model):
    producto = models.ForeignKey(Producto, related_name='imagenes',on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/')
    
    def __str__(self):
        return f'Imagen de {self.producto.nombre}'
