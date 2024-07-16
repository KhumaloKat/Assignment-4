from django.db import models

CATEGORY_CHOICES =(
    ('LS','Lifestyle'),
    ('TC','Technology'),
    ('BS','Business'),
    ('SC','Science'),
    ('PC','Politics'),
    ('CR','Creativity'),

)

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    image =models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.title