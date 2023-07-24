from django.db import models

class Bug(models.Model):
    # 
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=511)
