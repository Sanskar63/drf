from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict

# now introducint rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializer import ProductSerializer

def api_home(request, *args, **kwargs):
    # request -> HttpRequest (not python requests)
    print(request.GET) # url query params
    body = request.body #it is byte string of Json data (string of json)
    # to convert it to json 
    data = {}
    try:
        data = json.loads(body) #takes string of JSON data and convert it to python dict
    except:
        pass
    
    # ********Now Echoing GET data i.e. sending back data we r getting (for knowing what things are sent when we are calling an endpoint)*******
    
    # data['headers'] = request.headers # in older versions we had to do request.META  # it will give error read yourself, now to solve that -> the next line
    
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    data['params'] = dict(request.GET)
    # print(data)
    # return JsonResponse({"message":"Hello this your django api response"})
    return JsonResponse(data)


def get_data(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    
    # data['title'] = model_data.title
    # data['content'] = model_data.content
    # data['price'] = model_data.price
    # Here basically i am taking model instance and converting it to python dict and then returning json to client in short ***Serializing****
    
    data = model_to_dict(model_data, fields=['id', 'title', 'content'])
    
    # return JsonResponse({"message": "8==============D"})
    return JsonResponse(data)


# DRF
@api_view(["GET"])
def drf_get_data(request, *args, **kwargs):
    # model_data = Product.objects.all().order_by("?").first()
    instance = Product.objects.all().order_by("?").first()
    data = {}
    # if model_data:
    #     data = model_to_dict(model_data, fields=['id', 'title', 'content']) # Here adding 'sale_price' field don't work thats why serializer is important
    
    if instance:
        data = ProductSerializer(instance).data

    return Response(data)

# *****************POST**********************
@api_view(['POST'])
def post_api(request, *args, **kwargs):
    """
    DRF API View
    """
    print(request.data)
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # instance = form.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)