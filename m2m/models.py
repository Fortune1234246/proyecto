from django.db import models

from django.contrib import admin



class Marca(models.Model):

    nombre              = models.CharField(max_length=60)

    anio_fundacion      = models.IntegerField()
    capital             = models.IntegerField()


    def __str__(self):

        return self.nombre

class Cliente(models.Model):

    nombre              = models.CharField(max_length=60)

    edad                = models.IntegerField()
    dpi                 = models.IntegerField()


    def __str__(self):

        return self.nombre


class Carro(models.Model):

    Marca       = models.ForeignKey(Marca, on_delete=models.CASCADE)

    anio        = models.IntegerField()
    linea       = models.IntegerField()
    precio      = models.IntegerField()


    def __str__(self):

        return self.nombre

class Venta(models.Model):

    Cliente       = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    fecha        = models.DateField()

    detalleVenta = models.ManyToManyField(Carro, through='detalleVenta')


    def __str__(self):

        return self.nombre


class detalleVenta (models.Model):

    Carro = models.ForeignKey(Carro, on_delete=models.CASCADE)

    Venta = models.ForeignKey(Venta, on_delete=models.CASCADE)


class detalleVentaInLine(admin.TabularInline):

    model = detalleVenta

#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.

    extra = 1


class CarroAdmin(admin.ModelAdmin):

    inlines = (ActuacionInLine,)


class VentaAdmin (admin.ModelAdmin):

    inlines = (ActuacionInLine,)
