from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login,authenticate,logout
import stripe.error
from . forms import VendorLoginForm,VendorCreationForm,vendor_products ,ProfileForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from . models import *
from  django.db.models import Q
import stripe
from django.conf import settings
from .forms import PaymentForm
from django.views.decorators.csrf import csrf_exempt
from . models import AddressForm
import stripe



def index(request):
    best_selling_products = Product.objects.filter(category='best_selling_products')
    new_arrivals = Product.objects.filter(category='new_arrivals')
    discounted_products = Product.objects.filter(category='discounted')
    Grocery = Product.objects.filter(category = 'grocery')
    Kitchen = Product.objects.filter(category = 'kitchen')
    Mobile = Product.objects.filter(category = 'mobile')
    Camera = Product.objects.filter(category = 'camera')
    Shoes = Product.objects.filter(category = 'shoes')
    Clothes = Product.objects.filter(category = 'clothes')
    Books = Product.objects.filter(category = 'books')
    Furniture = Product.objects.filter(category = 'furniture')
    Beauty = Product.objects.filter(category = 'beauty')
    # Fetch all unique categories except the predefined ones
    predefined_categories = ['best_selling', 'new_arrivals', 'discounted']
    categories = Product.objects.exclude(category__in=predefined_categories).values_list('category', flat=True).distinct()
    
    products_by_category = {category: Product.objects.filter(category=category) for category in categories}

    context = {
        'best_selling_products': best_selling_products,
        'new_arrivals': new_arrivals,
        'discounted_products': discounted_products,
        'products_by_category': products_by_category,
        'Grocery':Grocery,
        'Kitchen':Kitchen,
        'Mobile':Mobile,
        'Camera':Camera,
        'Shoes':Shoes,
        'Clothes':Clothes,
        'Books':Books,
        'Furniture':Furniture,
        'Beauty':Beauty


    }
    return render(request, 'core/index.html', context)



def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def add_vendor(request):
    if request.method == "POST":
        form = VendorCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vendor successfully added')
            return redirect('core:index')  
    else:
        form = VendorCreationForm()
    
    context = {'form': form}
    return render(request, 'core/add_vendor.html', context)


def vendor_login(request):
    form=VendorLoginForm()
    if request.method == 'POST':
        form = VendorLoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            vendor = authenticate(request, username = username, password=password)
            if vendor is not None:
                login(request, vendor)
                messages.success(request,'Vendor successfully logged in')
                return redirect('core:index')
            else:
                messages.error(request,'invalid password or username')

        else:
            messages.error(request,'form is invalid')
    
    context = {
        'form':form
    }
    return render (request, 'core/vendor_login.html',context)

def vendor_logout(request):
    logout(request)
    messages.success(request,'vendor have successfully logged out')
    return redirect('core:index')

def vendor_list(request):
    vendors = Vendor.objects.all()
    context = {'vendors':vendors}
    return render(request, 'core/vendor_list.html',context)




from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import vendor_products
from .models import Vendor

@login_required
def add_products(request):
    if not request.user.is_superuser and not hasattr(request.user, 'vendor'):
        messages.error(request, 'You do not have the permission to add products')
        return redirect('core:index')
    
    if request.method == 'POST':
        form = vendor_products(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)

            if request.user.is_superuser:
                product.vendor = Vendor.objects.first() 
            else:
                product.vendor = request.user.vendor
            
            product.save()
            messages.success(request, 'Product successfully added')  
            messages.info(request, 'You can view the product in your products list.')  

            return redirect('core:add_products')
    else:
        form = vendor_products()

    context = {
        'form': form
    }
    return render(request, 'core/add_products.html', context)





@login_required
def profile_view(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('core:profile')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'core/profile.html', {
        'form': form,
        'profile_picture': profile.profile_picture if profile.profile_picture else None,
        'username': user.username,
        'email': user.email,
        'phone_number': profile.phone_number,
        'created_at': user.date_joined,
    })




@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('core:cart_detail')



@login_required
def cart_detail(request):
    cart = Cart.objects.filter(user=request.user).first()
    cart_items = CartItem.objects.filter(cart=cart) if cart else []
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    context = {'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'core/cart_detail.html', context)


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('core:cart_detail')

@login_required
def update_cart(request,item_id):
    cart_item = get_object_or_404(CartItem,id = item_id)
    if cart_item.quantity>1:
        cart_item.quantity -=1 
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('core:cart_detail')

@login_required
def update_add_cart(request,item_id):
    cart_item = get_object_or_404(CartItem, id = item_id)
    if cart_item.quantity>=1:
        cart_item.quantity+=1
        cart_item.save()
    return redirect('core:cart_detail')

stripe.api_key = settings.STRIPE_SECRET_KEY

def payment_view(request):
    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        amount = 5000  # Amount in cents

        if not token:
            return redirect('core:payment_failed')  # Redirect to failure page if no token

        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description='Example Charge',
                source=token
            )
            return redirect('core:payment_success')  
        except stripe.error.CardError as e:
            print(f"CardError: {e.user_message}")  
            return redirect('core:payment_failed')  
        except Exception as e:
            print(f"Exception: {str(e)}")  
            return redirect('core:payment_failed')  
    else:
        context = {
            'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
        }
        return render(request, 'core/payment.html', context)


@login_required
def payment_success_view(request):
    return render(request, 'core/payment_success.html')

@login_required
def payment_failed_view(request):
    return render(request, 'core/payment_failed.html')

def search(request):
    search_result = request.GET.get('search','')
    products = []
    if search_result:
        products = Product.objects.filter(
            Q(name__icontains = search_result)|
            Q(description__icontains = search_result)|
            Q(price__icontains = search_result)|
            Q(category__icontains = search_result))      
    return render(request, 'core/search_result.html/',context={'products':products})

from django.db.models import Count, Avg
from core.models import CommentAndRating  # Assuming this is your model

@login_required
def comment_rating(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    if request.method == 'POST':
        stars = int(request.POST.get('stars', 0))
        comment_text = request.POST.get('comment_text', '')

        obj, created = CommentAndRating.objects.update_or_create(
            user=user,
            product=product,
            defaults={
                'stars': stars,
                'text': comment_text
            }
        )

        messages.success(request, "Your rating and comment has been saved ")
        return redirect('core:product_detail', product_id=product.id)

    ratings = CommentAndRating.objects.filter(product=product)
    average_rating = ratings.aggregate(avg=Avg('stars'))['avg'] or 0
    total_reviews = ratings.count()

    star_counts = ratings.values('stars').annotate(count=Count('stars')).order_by('-stars')
    star_data = {i: 0 for i in range(1, 6)}
    for item in star_counts:
        star_data[item['stars']] = item['count']

    context = {
        'product': product,
        'average_rating': round(average_rating, 1),
        'total_reviews': total_reviews,
        'star_data': star_data,
        'all_ratings': ratings,  
    }

    return render(request, 'core/product_detail.html', context)

@login_required
def add_address(request):
    if request.method == 'POST':
        form = AddressForm
        if AddressForm.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('core:payment.html')
    else:
        form = AddressForm()
    return render(request, 'core/address.html', {"form":form})

def update_address(request,address_id):
    address = get_object_or_404(Adres, id = address_id, user=request.user)