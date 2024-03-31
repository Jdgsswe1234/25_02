from django.db import models
class Clients(models.Model):
    name= models.CharField("ФИО",max_length=50)
    login+ models.CharField("Логин",max_length=50)