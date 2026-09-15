from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import AnonymousUser
from .models import Product, Cart, Order ,Review, Wishlist,Suggestion
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
# Create your views here.


def home(request):
    query = request.GET.get("q")

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(brand__icontains=query)
        )
    else:
        products = Product.objects.all()

    return render(request, "store/home.html", {
        "products": products,
        "query": query,
    })

    return render(request, "store/home.html", context)
    
def product_detail(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    reviews = Review.objects.filter(product=product).order_by("-created_at")

    average_rating = 0

    if reviews.exists():
        average_rating = sum(
            review.rating for review in reviews
        ) / reviews.count()

    context = {
        "product": product,
        "reviews": reviews,
        "average_rating": round(average_rating, 1),
    }

    return render(
        request,
        "store/product_detail.html",
        context,
    )
    
    

@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
    )

    if created:

        messages.success(request, "Product added to cart!")

    else:

        cart_item.quantity += 1
        cart_item.save()

        messages.success(request, "Cart quantity updated!")

    return redirect("product_detail", product_id=product.id)

@login_required
def cart(request):

    

    cart_items = Cart.objects.filter(user=request.user)

    grand_total = sum(item.total_price() for item in cart_items)

    context = {
        "cart_items": cart_items,
        "grand_total": grand_total,
    }

    return render(request, "store/cart.html", context)

@login_required(login_url="login")
def checkout(request):

    cart_items = Cart.objects.filter(user=request.user)

    grand_total = sum(item.total_price() for item in cart_items)

    if request.method == "POST":

        customer_name = request.POST.get("name")
        customer_email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")
        payment_method = request.POST.get("payment_method")
        
        print(request.POST)
        print(payment_method)

        Order.objects.create(
            user=request.user,
            customer_name=customer_name,
            customer_email=customer_email,
            phone=phone,
            address=address,
            city=city,
            state=state,
            pincode=pincode,
            payment_method=payment_method,
            total_price=grand_total,
)
        

        cart_items.delete()

        return render(request, "store/order_success.html")

    context = {
        "cart_items": cart_items,
        "grand_total": grand_total,
    }

    return render(request, "store/checkout.html", context)


@login_required
def my_orders(request):

    orders = Order.objects.filter(user=request.user).order_by("-created_at")

    return render(request, "store/my_orders.html", {
        "orders": orders
    })


def remove_from_cart(request, cart_id):

    if not request.user.is_authenticated:
        return redirect("login")

    cart_item = get_object_or_404(
        Cart,
        id=cart_id,
        user=request.user
    )

    cart_item.delete()

    return redirect("cart")
def increase_quantity(request, cart_id):

    cart_item = get_object_or_404(
        Cart,
        id=cart_id,
        user=request.user
    )

    cart_item.quantity += 1
    cart_item.save()

    return redirect("cart")


def decrease_quantity(request, cart_id):

    cart_item = get_object_or_404(
        Cart,
        id=cart_id,
        user=request.user
    )

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect("cart")

def place_order(request):

    Cart.objects.all().delete()

    return render(request, "store/order_success.html")

@login_required
def add_review(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":

        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        Review.objects.create(
            product=product,
            user=request.user,
            rating=rating,
            comment=comment,
        )

    return redirect("product_detail", product_id=product.id)

@login_required
def add_to_wishlist(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    wishlist_item, created = Wishlist.objects.get_or_create(
    user=request.user,
    product=product
)

    if created:
        messages.success(request, "Added to wishlist!")
    else:
        messages.info(request, "Already in your wishlist!")

    return redirect("product_detail", product_id=product.id)

@login_required
def wishlist(request):

    wishlist_items = Wishlist.objects.filter(
        user=request.user
    ).select_related("product")

    return render(
        request,
        "store/wishlist.html",
        {
            "wishlist_items": wishlist_items
        }
    )
@login_required
def remove_from_wishlist(request, wishlist_id):

    item = get_object_or_404(
        Wishlist,
        id=wishlist_id,
        user=request.user
    )

    item.delete()

    return redirect("wishlist")

def about(request):
    return render(request, "store/about.html")

def contact(request):
    return render(request, "store/contact.html")


def suggestions(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Suggestion.objects.create(
            name=name,
            email=email,
            message=message
        )

        messages.success(
            request,
            "Thank you! Your suggestion has been submitted successfully."
        )

        return redirect("suggestions")

    return render(request, "store/suggestions.html")