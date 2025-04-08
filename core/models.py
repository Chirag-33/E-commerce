from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

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
    

class CommentAndRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rating_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.PositiveBigIntegerField(null=True, blank=True, validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} rated {self.stars} and commented on {self.product.name}'

    @classmethod
    def get_average_rating(cls,product):
        ratings = cls.objects.filter(product=product,star__isnull = False)
        if ratings.exists():
            return round(sum(r.stars for r in ratings)/ ratings.count(),1)

class Adres(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=10)
    create_at = models.DateTimeField(auto_created=True)

from django import forms

class AddressForm(forms.Form):
    class Meta:
        model = Adres
        fields = ['address','phone_number']