from django.db import models

# Create your models here.
class Employee_Table(models.Model):

    FName=models.CharField(max_length=15)
    LName = models.CharField(max_length=15)
    Email=models.EmailField(max_length=30)
    Ph_No=models.CharField(max_length=13)
    EDate=models.DateField()

    def __str__(self):
        return self.FName
    class Meta:
        db_table='Employee_Data'