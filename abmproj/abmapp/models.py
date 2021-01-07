from django.db import models

# Create your models here.

class edificio(models.Model):
    descripcion = models.CharField(max_length=500)
    direccion = models.CharField(max_length=500)
    activo = models.BooleanField(default=True, null=False, blank=False)

class piso(models.Model):
    descripcion = models.CharField(max_length=500)
    edificio = models.ForeignKey(edificio, on_delete=models.DO_NOTHING)
    plano = models.TextField()
    activo = models.BooleanField(default=True, null=False, blank=False)

class area(models.Model):
    descripcion = models.CharField(blank=False, null=False, max_length=500)
    piso = models.ForeignKey(piso, on_delete=models.DO_NOTHING)
    tipoArea = models.IntegerField(blank=False, null=False)
    latitud = models.DecimalField(max_digits=20, decimal_places=2,blank=False, null=False)
    longitud = models.DecimalField(max_digits=20, decimal_places=2,blank=False, null=False)
    radioMayor = models.DecimalField(max_digits=20, decimal_places=2,blank=False, null=False)
    radioMenor = models.DecimalField(max_digits=20, decimal_places=2,blank=False, null=False)
    usuarioAlta = models.CharField(max_length=500)
    usuarioBaja = models.CharField(max_length=500, null=True, blank=True, default=None)
    activo = models.BooleanField(blank=False, null=False, default=True)