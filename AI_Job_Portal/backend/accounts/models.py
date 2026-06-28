from django.db import models


class Register(models.Model):

    full_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Job(models.Model):

    job_title = models.CharField(max_length=100)

    company = models.CharField(max_length=100)

    location = models.CharField(max_length=100)

    salary = models.CharField(max_length=50)

    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} - {self.company}"
    
class ApplyJob(models.Model):

    full_name = models.CharField(max_length=100)

    email = models.EmailField()

    job_title = models.CharField(max_length=100)

    company = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name} - {self.job_title}"

class Recommendation(models.Model):

    full_name = models.CharField(max_length=100)

    email = models.EmailField()

    skills = models.TextField()

    recommended_job = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name} - {self.recommended_job}"