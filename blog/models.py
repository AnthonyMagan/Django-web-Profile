from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    #function to return what the default name is S5L47
    def __str__(self):
        return self.title
