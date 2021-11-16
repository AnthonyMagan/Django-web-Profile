from django.db import models

#S5L39 Create your model
# Create your models here. Blank meaning user does not nesscessary need it
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    #function to return what the default name is S5L47
    def __str__(self):
        return self.title
