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
    
class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    text = models.TextField()  # Changed from 'body' to 'text'
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name}'