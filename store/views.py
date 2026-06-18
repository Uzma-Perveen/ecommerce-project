from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Cart, CartItem, Order, OrderItem
from .forms import RegisterForm

# ── Auth Views ───────────────────────────────────────
def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Account created! Please log in.")
        return redirect('login')
    return render(request, 'store/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('home')
        messages.error(request, "Invalid credentials.")
    return render(request, 'store/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# ── Product Views ────────────────────────────────────
def home(request):
    query    = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query) if query else Product.objects.all()
    return render(request, 'store/home.html', {'products': products, 'query': query})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

# ── Cart Views ───────────────────────────────────────
@login_required
def cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, 'store/cart.html', {'cart': cart})

@login_required
def add_to_cart(request, pk):
    product  = get_object_or_404(Product, pk=pk)
    cart, _  = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, f'"{product.name}" added to cart.')
    return redirect('home')

@login_required
def increase_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.quantity += 1
    item.save()
    return redirect('cart')

@login_required
def decrease_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart')

@login_required
def remove_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('cart')

# ── Order Views ──────────────────────────────────────
@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    items = cart.cartitem_set.all()

    if not items:
        messages.error(request, "Your cart is empty.")
        return redirect('cart')

    if request.method == 'POST':
        # Check stock
        for item in items:
            if item.product.stock < item.quantity:
                messages.error(request, f'Not enough stock for "{item.product.name}".')
                return redirect('cart')

        # Create order
        total = cart.get_total()
        order = Order.objects.create(user=request.user, total=total)

        for item in items:
            OrderItem.objects.create(
                order    = order,
                product  = item.product,
                quantity = item.quantity,
                price    = item.product.price,
            )
            # Reduce stock
            item.product.stock -= item.quantity
            item.product.save()

        # Clear cart
        items.delete()
        return redirect('order_success', pk=order.pk)

    return render(request, 'store/checkout.html', {'cart': cart})

@login_required
def order_success(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'store/order_success.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/order_history.html', {'orders': orders})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'store/order_detail.html', {'order': order})