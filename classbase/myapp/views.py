from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import TemplateView,View,ListView,DetailView
from myapp.models import *
from myapp.form import IncomeExpenseForm, CategoryForm
from django.http import JsonResponse

# Create your views here.

class HomePage(TemplateView):
    template_name = 'index.html'
    
class SecondView(View): # most use for API
    def get(self,request):
        print('GET method is working')
        return render(request, 'index.html')
    
    def post(self,request):
        print('POST method is working')
        return render(request,'index.html')
    
    
    
def incomeExpenseFunction(request):
    ie_obj = IncomeExpense.objects.all()
    form = IncomeExpenseForm()
    
    
    if request.method == 'POST':
        form = IncomeExpenseForm(request.POST)
        
        if form.is_valid():
            print('New Item Save ======================================================')
            print(request.POST)
            form.save()
        else:
            print('Item Saved Error ===================================================')
            print(request.POST)
        
        
    context = {'ie_obj':ie_obj,'form':form}
    return render(request, 'index.html', context)


# def incomeExpenseFunction(request):
#     ie_obj = IncomeExpense.objects.all()
#     form = IncomeExpenseForm()
    
    
    
#     if request.method == 'POST':
#         form = IncomeExpenseForm(request.POST)   
#         if form.is_valid():
#             print('New Item Save ======================================================')
#             print(request.POST)
#             form.save()
#         else:
#             print('Item Saved Error ===================================================')
#             print(request.POST)
            
#     else:
#         if request.GET.get('addNewItem'):
#             context = {'ie_obj':ie_obj,'form':form}
#             return render(request, 'index.html', context)
            
        
#         else:
#             return render (request, 'index.html', {'ie_obj':ie_obj})
        
#     return render (request, 'index.html', {'ie_obj':ie_obj})
           


def ItemDeleteView(request,id):
    item_delete = IncomeExpense.objects.filter(id=id)
    item_delete.delete()
    print('Delet Successful')
    return redirect('incomeexpensefunction')

def ItemUpdateView(request,id):
    item_update = IncomeExpense.objects.get(id=id)
    form = IncomeExpenseForm()
    
    if request.method == 'POST':
        form = IncomeExpenseForm(request.POST, instance= item_update)
        form.save()
        print('Item Successfully Update===================================================')
        return redirect('incomeexpensefunction')

        
    context = {'form':form}
    return  render(request, 'index.html' ,context)


def addCategory(request):
    form1 = CategoryForm()
    context = {'form1':form1}
    
    if request.method == 'POST':
        form1 = CategoryForm(request.POST)
        if form1.is_valid():
            form1.save()
            print(request.POST)
            print('New Category Successfully Saved ========================================')
            return redirect('incomeexpensefunction')
            
        else:
            print(request.POST)
            print("Erro Save Category===================================================")
            
            
    
    return render(request, 'form-show.html', context)


class CategoryAdd(View):
    def get(self,request):  
        form1 = CategoryForm()
        context = {'form1':form1}
        return render(request, 'form-show.html', context)

    def post(self,request):
        form1 = CategoryForm(request.POST)
        if form1.is_valid():
            form1.save()
            print(request.POST)
            print('New Category Successfully Saved ========================================')
            return redirect('incomeexpensefunction')
            
        else:
            print(request.POST)
            print("Erro Save Category===================================================")
            
            


class CategoryList(ListView):
    model = Category
    template_name = 'index.html'
    

class CatDetail(DetailView):
    pass
    

def home(request):
    data_obj = IncomeExpense.objects.all()
    context = {'data_obj':data_obj}
    return render(request, 'home.html', context)

def creteExpense(request):
    
    task_n = request.GET.get('expense')
    am = request.GET.get('amount')
    cat = request.GET.get('cat')
    cat_obj = Category.objects.get(id = int(cat))
    
 
    
    print('===============  Data Received =======================')
    
    print(f'Task Name is  {task_n}')
    print(f'Amount is {am}')
    print(f'Category ID is {cat}')
    print(f'Category ID with Income or Expense  === {cat_obj}')
  
    
    print('======================================================')
    
    IncomeExpense.objects.create(
        task_name = task_n,
        amount = am,
        category = cat_obj
    )
    
    # return HttpResponse('success')
    return JsonResponse({'status':'success'})




def delet_exp(request):
    pid = request.GET.get('pd')
    IncomeExpense.objects.get(id=int(pid)).delete()
    print('=================================')
    print('Delete Success ')
    print('=================================')
    
    return JsonResponse({'status':'delete'})

def edit_exp(request):
    
    EID = request.GET['eid']
    # CAT = request.GET['cat']
    # AMOUNT = request.GET['amount']
    # EXPENSE = request.GET['expense']
    print('hello world ')
  
    print('income')
    pdata = IncomeExpense.objects.get(id=int(EID))
    # cdata = Category.objects.get(id= int(CAT))
    
    print('save')
    # IncomeExpense.objects.create(
    #     category = cdata,
    #     task_name = EXPENSE,
    #     amount = int(AMOUNT),
        
    # )
    
    
    
    
     
    print('last ') 
    # return render(request, 'show.html', context)
    # return redirect('home')
    
    return JsonResponse({'status':'success'})


            
def showView(request):
    form = IncomeExpenseForm()
    context = {'form':form}
    return render(request,'show.html',context)