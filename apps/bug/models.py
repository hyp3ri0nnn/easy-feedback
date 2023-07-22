from django.db import models

class Bug(models.Model):
    title = models.fields.CharField(max_length=255)