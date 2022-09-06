from django.db import models

# Create your models here.

class alertlog(models.Model):

      alertcity = models.CharField(max_length=100, blank=True,null=True)
      temp = models.CharField(max_length=100, blank=True,null=True)
      desc = models.CharField(max_length=100, blank=True,null=True)
      created_at = models.DateTimeField(auto_now_add=True)
     

      class Meta:
         db_table = "alertlog"