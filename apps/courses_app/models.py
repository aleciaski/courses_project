from __future__ import unicode_literals

from django.db import models
import re

class Course(models.Model):
	name= models.CharField(max_length= 255)
	desc= models.CharField(max_length= 255)
	created_at= models.DateTimeField(auto_now_add=True)

def __unicode__(self):
        return "id : " + str(self.id) + ", name : " + self.name + ", desc : " + self.desc +  ", created_at : " + str(self.created_at)
    
