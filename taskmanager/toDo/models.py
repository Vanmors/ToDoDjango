from django.db import models


class Tasks(models.Model):
    task = models.TextField("Task")
    creater = models.TextField("Creater")
    status = models.TextField("Status")


