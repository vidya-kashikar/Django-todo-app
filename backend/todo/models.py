
# todo/models.py
      
from django.db import models
# Create your models here.

# add this
class Todo(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)
  due_date = models.DateField(default='2024/02/24')
      
  def __str__(self):
    return self.title