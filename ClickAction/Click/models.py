from django.db import models


# Si es Circulo:
## latitud y longitud establecen el centro. RadioMayor es el radio del circulo.
# Si es Ractángulo:
## latitud y longitud establecen el centro. Radio mayor es media longitud de las X. Radio menor es media longitud de las Y.

class Clickleable(models.Model):
    idSite = models.IntegerField(blank=False, null=False, default=1) # es el ID del edificio.
    idArea = models.IntegerField(blank=False, null=False) # es el ID del espacio.
    tipo = models.IntegerField(blank=False, null=False) # selecciona si es rectángulo = 1 o circulo = 2
    latitud = models.DecimalField(max_digits=20, decimal_places=2,blank=False, null=False)
    longitud = models.DecimalField(max_digits=20, decimal_places=2,blank=False, null=False)
    radioMayor = models.DecimalField(max_digits=20, decimal_places=2,blank=False, null=False)
    radioMenor = models.DecimalField(max_digits=20, decimal_places=2,blank=False, null=False)
    activo = models.BooleanField(default=True,blank=False, null=False)

