from django.http import JsonResponse,HttpResponse
from django.core import serializers
from django.forms.models import model_to_dict
from .models import User
import json
def API(request):
  if request.method=='POST':
      temp_name=request.POST['name']
      temp_password=request.POST['password']
      temp_user=User(username=temp_name,password=temp_password)
      temp_user.save()
      result={'status':'success','data':[]}
      users=User.objects.all()
      for user in users:
        user=model_to_dict(user)
        result['data'].append(user)
      # return JsonResponse(result)
      return HttpResponse(json.dumps(result),content_type="application/json")
  else:
      return HttpResponse('Hello world')