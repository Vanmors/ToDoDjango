from django.db import models


class Tasks(models.Model):
    task = models.TextField("Task")
    permissions = models.TextField


