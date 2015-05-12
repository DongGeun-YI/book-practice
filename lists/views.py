from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from lists.models import Item, List

def home_page(request):

#    if request.method == 'POST':
 #       Item.objects.create(text = request.POST['item_text'])
  #      return redirect('/lists/the-only-list-in-the-world/')
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None
    if request.method == 'POST':
        try:
            item = Item.objects.create(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect('/lists/%d/'%(list_.id,))   # code가 이상함.
        except ValidationError:
            error = "You can't have an empty item"
    return render(request, 'list.html', {'list': list_, 'error': error})


def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST['item_text'], list = list_)
    try:
        item.save()
        item.full_clean()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty item"
        return render(request, 'home.html', {"error": error})
    return redirect(list_)  #('/lists/%d/' % (list_.id,))


