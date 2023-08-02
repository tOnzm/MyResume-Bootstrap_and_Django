from django.db import models

# Create your models here.
class Cards(models.Model):
    card_name = models.CharField(max_length=100)
    card_star = models.IntegerField()
    card_effect = models.TextField()
    card_image = models.ImageField(upload_to='app_cards/card_images')


    def __str__(self):
        return self.card_name 
    
