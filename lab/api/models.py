from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField(default='None')
    city = models.CharField(max_length=40)
    address= models.FloatField(default='0')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(default=None)
    salary = models.FloatField(default=None)
    company = models.ForeignKey(Company, on_delete= models.CASCADE)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary
        }