from django.db import models

class detectFruits(models.Model) :
    ref_id = models.AutoField(primary_key=True)
    ref_excode = models.CharField(max_length=50)
    ref_exname = models.CharField(max_length=50, default='fruits')
    ref_exdate = models.IntegerField()
    ref_quantity = models.IntegerField(default='1')