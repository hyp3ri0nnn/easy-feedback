from django.db import models

# Create your models here.

class Thank(models.Model):
    DRAFT = 0
    SENT = 1
    DELIVERED = 2
    READ = 3
    ANSWERED = 4
    PUBLISHED = 5

    STATUS_CHOICES = (
        (0, "Draft"),
        (1, "Sent"),
        (2, "Delivered"),
        (3, "Read"),
        (4, "Answered"),
        (5, "Published"),
    )

    title = models.CharField(max_length=127)
    description = models.CharField(max_length=511)
    publish_permission = models.BooleanField(default=False)
    image = models.ImageField()

    # also can use class based choices 
    # see https://docs.djangoproject.com/en/4.2/ref/models/fields/#enumeration-types
    status = models.IntegerField(default=DRAFT, choices=STATUS_CHOICES)

    ### Think about how this Model will be handled on company side ?
    ### If necessary seperate the Models then relate each other.