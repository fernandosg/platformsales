from django.db import models

# Create your models here.

class MensajeOperacion(models.Model):
    mensaje=models.TextField()
    estado=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.mensaje+" "+str(self.estado)
