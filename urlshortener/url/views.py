from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from .models import URL
from rest_framework.decorators import api_view
from django.http import JsonResponse
import hashlib
from .serializers import URLSerializer
from rest_framework.response import Response

def redirect_original_url(request, hash):
  try:
    url = URL.objects.get(hash=hash)
    url.visits += 1
    url.save()
    return redirect(url.url)
  except URL.DoesNotExist:
    return HttpResponseNotFound("Short URL not found")
  
@api_view(['POST'])
def create_short_url(request):
  if 'url' in request.data:
    original_url = request.data['url']
    hash_value = hashlib.md5(original_url.encode()).hexdigest()[:10]

    url = URL.objects.create(hash=hash_value, url=original_url)
    
    return JsonResponse({'short_url': f'/url/{hash_value}/'}, status=201)
  return JsonResponse({'error': 'Invalid request data'}, status=400)


@api_view(['GET'])
def get_url_stats(request, hash):
  try:
    url = URL.objects.get(hash=hash)
    serializer = URLSerializer(url)
    return Response(serializer.data)
  except URL.DoesNotExist:
    return Response({'error': 'Short URL not found'}, status=404)
  

def simple_ui(request):
  urls = URL.objects.all()
  return render(request, "index.html", {"urls": urls})