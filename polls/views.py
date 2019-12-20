from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import json
from .models import BooK
import datetime

def detail(request):
    book_list=BooK.objects.order_by('-pub_date')
    context={'book_list':book_list} 
    return render(request,'polls/detail.html',context)

def addBook(request):
    if request.method == 'POST':
        temp_name = request.POST['name']
        temp_author = request.POST['author']
        temp_pub_house = request.POST['pub_house']

    from django.utils import timezone
    temp_book = BooK(name=temp_name, author=temp_author, pub_house=temp_pub_house, pub_date=timezone.now())
    temp_book.save()

   
    return HttpResponseRedirect(reverse('polls:detail'))
def deleteBook(request,book_id):
    bookId=book_id
    BooK.objects.filter(id=bookId).delete()
    return HttpResponseRedirect(reverse('polls:detail'))

def changeBookinfo(request,book_id):
  if request.method=='POST':
      temp_name=request.POST['name']
      BooK.objects.filter(id=book_id).update(name=temp_name)
      return HttpResponseRedirect(reverse('polls:detail'))