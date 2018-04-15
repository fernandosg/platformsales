from django.db import models

# Create your models here.

class MensajeOperacion(models.Model):
    mensaje=models.TextField()
    estado=models.BooleanField(default=False)

    def __str__(self):
        return self.mensaje+" "+str(self.estado)
