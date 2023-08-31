from django.db import models

class Applicant(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    education=models.CharField(max_length=100) 
    Experience=models.IntegerField()
    programs=models.CharField(max_length=1000)
    Salary_expected=models.IntegerField()
    info=models.CharField(max_length=100)
 
class Company(models.Model):
    company_name = models.CharField(max_length=10)
    Job_role=models.CharField(max_length=100)
    location = models.CharField(max_length=20)
    Job_type = models.CharField(max_length=20)
 
 
class Job(models.Model):
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=200)
    salary = models.FloatField()
    description = models.TextField(max_length=400)
    experience = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    creation_date = models.DateField()
 
 
class Application(models.Model):
    company = models.CharField(max_length=200)
    job = models.CharField(max_length=100)
    applicant = models.CharField(max_length=100)
    apply_date = models.DateField()
