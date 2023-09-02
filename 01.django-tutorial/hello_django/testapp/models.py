from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esalary = models.FloatField()
    eaddress = models.CharField(max_length=64)


class emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=30)
    job = models.CharField(max_length=20)
    mgr = models.IntegerField() 
    hiredate = models.DateField()
    sal = models.FloatField()
    comm = models.FloatField()
    deptno = models.IntegerField()

class Director(models.Model):
    director_name = models.CharField(max_length=64)
    def __str__(self) -> str:
        return self.director_name

class Movie(models.Model):
    movie = models.CharField(max_length=100)
    release_year = models.IntegerField()
    director_name = models.ForeignKey(Director, on_delete=models.CASCADE, max_length=64)