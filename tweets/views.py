from django.shortcuts import render
from django.http import JsonResponse

from .models import Tweet
# Create your views here.

def home_view(request, *ags,**kwargs):
    return render(request, "pages/home.html", context={}, status=200)

def tweet_detail_view(request,tweet_id, *args,**kwargs):

    '''
    REST API VIEW 
    consume by JavaScript or Swift/JAVA/iOS/Andriod
    return json data
    '''
    data = {
        "id" : tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404
    
    return JsonResponse(data, status=status) #json.dumps content_type = 'application/json'