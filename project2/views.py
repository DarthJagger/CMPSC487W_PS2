from django.shortcuts import render, redirect
from .models import storeItem
from .forms import AddItem
from django.db.models import Q

# Create your views here.


def home(request):
    search_items = request.GET.get('search')

    if search_items:
        items = storeItem.objects.filter(Q(title__icontains=search_items) |
                                         Q(name__icontains=search_items) |
                                         Q(desc__icontains=search_items))
    else:
        # If not searched, return default posts
        items = storeItem.objects.all()


    return render(request, "home.html", {"storeItem":items})

def update(request, title):
    item = storeItem.objects.get(title=title)
    form = AddItem(instance=item)
    if request.method == 'POST':
        form = AddItem(request.POST, instance=item)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('home')
    else:
        form = AddItem(instance=item)

    return render(request,
                  'update.html',
                  {'form': form})

def delete(request, title):
    item = storeItem.objects.get(title=title)
    form = AddItem(instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    else:
        form = AddItem(instance=item)

    return render(request,
                  'delete.html',
                  {'item': item})


def detail(request, title):
    item = storeItem.objects.get(title=title)
    return render(request,
          'detail.html',
         {'item': item})

def addItem(request):
    if request.method == "POST":
        form = AddItem(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddItem()
    return render(request, "addItem.html", {'form': form})

def home_sort(request):
    search_items = request.GET.get('search')

    if search_items:
        items = storeItem.objects.filter(Q(title__icontains=search_items) |
                                         Q(name__icontains=search_items) |
                                         Q(desc__icontains=search_items))
    else:
        # If not searched, return default posts
        items = storeItem.objects.all().order_by('name')

    return render(request, "home_sort.html", {"storeItem":items})



