<<<<<<< HEAD
from django.db import models

class detectFruits(models.Model) :
    ref_id = models.AutoField(primary_key=True)
    ref_excode = models.CharField(max_length=50)
    ref_exname = models.CharField(max_length=50, default='fruits')
    ref_exdate = models.IntegerField()
=======
from django.db import models

class detectFruits(models.Model) :
    ref_id = models.AutoField(primary_key=True)
    ref_excode = models.CharField(max_length=50)
    ref_exname = models.CharField(max_length=50, default='fruits')
    ref_exdate = models.IntegerField()
>>>>>>> e83ef521bec72ef685a6831704f6653aff170d6f
    ref_quantity = models.IntegerField(default='1')