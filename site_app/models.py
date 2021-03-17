from django.db import models

class ignisdata(models.Model):
    event_name=models.CharField(max_length=255)
    data=models.CharField(max_length=255)
    time=models.DateTimeField(auto_now_add=True)
    location=models.CharField(max_length=255)
    image=models.ImageField()
    is_liked=models.BooleanField(default=False)
   
    class Meta:
        db_table="ignisdata"


