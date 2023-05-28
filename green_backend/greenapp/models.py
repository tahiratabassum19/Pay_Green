from django.db import models


# thise section will manage the database in the backend will create table format database for
#  email and passwords to check existing user

   

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    type_of_user = models.CharField(max_length=50)
    total_income = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.email
