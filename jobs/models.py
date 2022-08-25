from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='images/',null=True)
    summary = models.CharField(max_length=200)
    # new_field = models.CharField(max_length=140, default='SOME STRING')