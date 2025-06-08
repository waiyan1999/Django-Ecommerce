from django.db import models

# Create your models here.


# =================== Day17 =============

class Category(models.Model):
    category_name = models.CharField()
    
    def __str__(self):
        return self.category_name
    

class Product (models.Model):
    p_category = models.ForeignKey(Category,on_delete= models.CASCADE)
    p_name = models.CharField()
    p_photo = models.ImageField(upload_to='product')
    p_price = models.PositiveIntegerField()
    p_dis_pirce = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.p_name
    
    
class Cart (models.Model):
    
    # cart_qty = models.PositiveIntegerField()
    cart_total_amount = models.PositiveIntegerField()
    cart_created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    
class CartProduct(models.Model):
    cart_category = models.ForeignKey(Cart,on_delete=models.CASCADE)
    cart_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_qty = models.PositiveIntegerField(default=0)
    cart_amount = models.PositiveIntegerField(default=0)
    
    # def __str__(self):
    #     return f'{self.Cart.id}-----{self.cart_product}'


 
    
    
