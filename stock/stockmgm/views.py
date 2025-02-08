from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from django.contrib import messages
from .models import Stock, Category
from .forms import StockCreateForm, StockSearchForm, StockUpdateForm

def home(request):
    title = 'Welcome: This is the Home Page'
    context = {
        "title": title,
    }
    return render(request, "stockmgm/home.html", context)

def list_item(request):
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {
        "queryset": queryset,
        "form": form
    }
    
    if request.method == 'POST' and form.is_valid():
        queryset = Stock.objects.filter(
            category__name__icontains=form['category'].value(),
            item_name__icontains=form['item_name'].value()
        )

        if form.cleaned_data.get('export_to_CSV', False):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List_of_stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
            
            for stock in queryset:
                writer.writerow([stock.category.name, stock.item_name, stock.quantity])
            
            return response

    return render(request, 'stockmgm/list_item.html', context)

def add_item(request):
    if request.method == 'POST':
        form = StockCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('list')
    else:
        form = StockCreateForm() 
    context = {'form': form, 'title': 'Add Item'}
    return render(request, 'stockmgm/add_item.html', context)

def update_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated')
            return redirect('list')
    context = {'form': form}
    return render(request, 'stockmgm/add_item.html', context)

def delete_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Deleted Successfully')
        return redirect('list')
    return render(request, 'stockmgm/delete_items.html')
