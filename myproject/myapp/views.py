from django.shortcuts import render,redirect
from myapp.models import Product,Category,Cart,CartProduct

# login and authentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# # Create your views here.


def baseView(request):
    return render(request, 'base.html')

def indexView(request):
    return render(request, 'index.html')

def productListView(request):
    p_data = Product.objects.all()
    context = {'p_data':p_data}
    return render(request, 'product-list.html', context)

def productDetailView(request,id):
    p_detail_obj = Product.objects.filter(id=id)
    context = {'p_detail_obj':p_detail_obj}
    return render (request, 'product-detail.html',context)

def cartView(request):
    cart_data = CartProduct.objects.all()
    context = {'cart_data':cart_data}
    return render (request,'cart.html',context)

def checkOutView(request):
    return render (request, 'checkout.html')



# def addToCart(request):
#     pid = request.GET.get('product_id')
#     cart_obj = Cart.objects.create(cart_total_amount = 0)
#     p_obj = Product.objects.get(id=pid)
    
    
#     cp_obj = CartProduct.objects.create(
#                                         cart_category=cart_obj ,
#                                         cart_product = p_obj ,
#                                         cart_qty = 1,
#                                         cart_amount=p_obj.p_price)
    
    
#     return redirect ('cart')


# ================ with session ==============================
# def addToCart(request):
#     pid = request.GET.get('product_id')
#     p_obj = Product.objects.get(id=pid)
    
#     inv_no = request.session.get('invoice_no',None)
    
    
#     if inv_no:
#         # alrady have seeeion
#         print('Session Already Have ,Invoice Number  No Created')
#         print(inv_no)
#         cart_obj = Cart.objects.get ( id = inv_no)
#         cp_obj = CartProduct.objects.create(
#                                         cart_category=cart_obj ,
#                                         cart_product = p_obj ,
#                                         cart_qty = 1,
#                                         cart_amount=p_obj.p_price)
        
        
#     else:
#         # does not have session
#         print('Session Does not have , New Session created')
#         cart_obj = Cart.objects.create(cart_total_amount = 0)
#         request.session["invoice_no"] = cart_obj.id
        
#         # print(request.session.get('invoice_no',None))
    
    
    
#         cp_obj = CartProduct.objects.create(
#                                         cart_category=cart_obj ,
#                                         cart_product = p_obj ,
#                                         cart_qty = 1,
#                                         cart_amount=p_obj.p_price)
        
    
    
    
#     return redirect ('cart')



# ================== with session and  check product  and add count ==================
# def addToCart(request):
#     pid = request.GET.get('product_id')
#     p_obj = Product.objects.get(id=pid)
    
#     inv_no = request.session.get('invoice_no',None)
    
    
#     if inv_no:
#         # alrady have seeeion
        
#         print('Session Already Have ,Invoice Number  No Created')
#         print(inv_no)
#         cart_obj = Cart.objects.get ( id = inv_no)
        
#         #if porduct have in invoice number
        
#         # prod_exit = CartProduct.objects.filter(cart_category = cart_obj , cart_product = p_obj)
        
#         product_exist = cart_obj.cartproduct_set.filter(cart_product = p_obj)
        
#         if product_exist.exists():
#             print("=========== Product Already Exist ===============")
            
#             product_itm = product_exist.first()
#             product_itm.cart_qty += 1
#             product_itm.save()
            
          
            
        
#         else:
#             print('=========== Product Does Not Exist =============')
        
#         cp_obj = CartProduct.objects.create(
#                                         cart_category=cart_obj ,
#                                         cart_product = p_obj ,
#                                         cart_qty = 1,
#                                         cart_amount=p_obj.p_price)
        
        
#     else:
#         # does not have session
#         print('Session Does not have , New Session created')
#         cart_obj = Cart.objects.create(cart_total_amount = 0)
#         request.session["invoice_no"] = cart_obj.id
        
#         # print(request.session.get('invoice_no',None))
    
    
    
#         cp_obj = CartProduct.objects.create(
#                                         cart_category=cart_obj ,
#                                         cart_product = p_obj ,
#                                         cart_qty = 1,
#                                         cart_amount=p_obj.p_price)
        
    
    
    
#     return redirect ('cart')



# =======================  AI fix code ==================================

from django.shortcuts import redirect, get_object_or_404
from .models import Product, Cart, CartProduct

def addToCart(request):
    pid = request.GET.get('product_id')
    p_obj = get_object_or_404(Product, id=pid)  # safer than Product.objects.get
    
    inv_no = request.session.get('invoice_no', None)
    
    if inv_no:
        print('Session Already Has Invoice Number:', inv_no)
        cart_obj = Cart.objects.filter(id=inv_no).first()
        
        if not cart_obj:
            print("Cart not found. Creating new one.")
            cart_obj = Cart.objects.create(cart_total_amount=0)
            request.session["invoice_no"] = cart_obj.id

        product_exist = cart_obj.cartproduct_set.filter(cart_product=p_obj)
        
        if product_exist.exists():
            print("=========== Product Already Exist ===============")
            product_itm = product_exist.first()
            product_itm.cart_qty += 1
            product_itm.cart_amount = product_itm.cart_qty * p_obj.p_price
            product_itm.save()
        else:
            print("=========== Product Does Not Exist =============")
            CartProduct.objects.create(
                cart_category=cart_obj,
                cart_product=p_obj,
                cart_qty=1,
                cart_amount=p_obj.p_price
            )

    else:
        print('Session Does not have, New Session created')
        cart_obj = Cart.objects.create(cart_total_amount=0)
        request.session["invoice_no"] = cart_obj.id
        
        CartProduct.objects.create(
            cart_category=cart_obj,
            cart_product=p_obj,
            cart_qty=1,
            cart_amount=p_obj.p_price
        )

    return redirect('cart')



def deleteCartProduct(request,id):
    dcp_obj = CartProduct.objects.filter(id=id)
    dcp_obj.delete()
    print('Delete Successful in Cart')
    
    return redirect ('cart')

def loginView(request):
    
    if request.method == 'POST':
        name = request.POST.get('l-name')
        password = request.POST.get('l-password')
        
        usr_auth = authenticate( username = name , password = password)
        
        if usr_auth:
            login(request,usr_auth)
            print('Successfully Login =============================')
            print(request.POST)
            
            return redirect('index')
            
        else:
            print("Login In Fail========================================")
            print(request.POST)
            
            return redirect('login')
    
    return render(request, 'login.html')


def logoutView(request):
    logout(request)
    return redirect('login')



