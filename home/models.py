from django.db import models
class tour(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    place=models.CharField(max_length=100)
    amount=models.IntegerField()
    date=models.DateField()
    contact = models.CharField(max_length=15)  # Updated to CharField to handle phone numbers
    email = models.EmailField()
    food_option = models.CharField(max_length=3, choices=[('Yes', 'Food'), ('No', 'No Food')], default='No')  # Food option field

    def __str__(self):
      return self.name



# Create your models here.
