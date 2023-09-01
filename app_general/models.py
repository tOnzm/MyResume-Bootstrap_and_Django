from django.db import models

# Create your models here.
class Education(models.Model):
    education_name = models.CharField(max_length=100)
    education_years = models.CharField(max_length=100)
    education_address = models.CharField(max_length=100)
    education_lvl = models.CharField(max_length=100)
    education_description = models.TextField()
    education_course = models.CharField(max_length=100, default='default_value')



    def __str__(self):
        return self.education_name 
    
class Experience(models.Model):
    experience_company = models.CharField(max_length=100)
    experience_years = models.CharField(max_length=100)
    experience_address = models.CharField(max_length=100)
    experience_role = models.CharField(max_length=100)
    experience_description = models.TextField()

    def __str__(self):
        return self.experience_company
    

class Skills(models.Model):
    skills = models.CharField(max_length=100)
  

    def __str__(self):
        return self.skills
    
class Languages(models.Model):
    languages = models.CharField(max_length=100)
  

    def __str__(self):
        return self.Languages
    
class MyProject(models.Model):
    myproject_name = models.CharField(max_length=100)
    myproject_description  = models.TextField()
    myproject_image = models.ImageField(upload_to='app_cards/card_images')


    def __str__(self):
        return self.myproject_name