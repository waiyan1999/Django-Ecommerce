from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField()
    
    def __str__(self):
        return self.name

class IncomeExpense(models.Model):
    task_name = models.CharField(blank=True, null= True)
    amount = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task_name
