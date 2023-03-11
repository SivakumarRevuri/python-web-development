from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esalary = models.FloatField()
    eaddress = models.CharField(max_length=64)


class emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(10)
    job = models.CharField(9)
    mgr = models.IntegerField() 
    hiredate = models.DateField()
    sal = models.FloatField()
    comm = models.FloatField()
    deptno = models.IntegerField()