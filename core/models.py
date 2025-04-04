from django.db import models
from django.contrib.auth.models import User

class Vendor(User):
    USER_TYPE_CHOICES = (
        ('Vendor', 'Vendor'),
        ('Customer', 'Customer'),
    )

    phone_number = models.CharField(max_length=10)
    address = models.TextField(blank=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='Customer')

    def __str__(self):
        return self.username

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('electronic', 'Electronic'),
        ('kitchen', 'Kitchen'),
        ('fashion', 'Fashion'),
        ('grocery', 'Grocery'),
        ('mobile','Mobile'),
        ('camera', 'Camera'),
        ('clothes', 'Clothes'),
        ('shoes', 'Shoes'),
        ('books', 'Books'),
        ('furniture','Furniture'),
        ('beauty', 'Beauty'),
        ('best_selling_products', 'Best_selling_products'),
        ('new_arrivals', 'New_arrivals')
        # add more categories as needed
    ]
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=300, default="https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES,default='unknown')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,)  # renamed to lowercase
    def __str__(self):
        return self.name

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'commented by {self.user.username} on {self.product.name}'

class Ratings(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.stars} starts by {self.user.username} on {self.product.name}'




    def __str__(self):
        return f'{self.quantity} x {self.product.name} in {self.cart.user.username}'




class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"{self.user.username}'s cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



class ItemStatu (models.Model):
    product_status = [
        ('payment_conformation', 'Payment_conformation'),
        ('packed', 'Packed'),
        ('intransit', 'Intransit'),
        ('delivered', 'Delivered'),
    ]
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    status = models.CharField(max_length=100,  choices=product_status, default='')


class UserProfile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    phone_number = models.CharField(max_length=10 , blank=True)
    