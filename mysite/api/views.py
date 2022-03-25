from ast import literal_eval
from pickle import TRUE
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import numpy as np

@api_view(['GET'])
def is_shopify_shop(request):
    url = request.query_params.get('url')
    try:
        html = requests.get(url).text
        if (html.find('var Shopify = Shopify || {}') != -1):
            return Response(True)
        else:
            return Response(False)
    except AssertionError as e:
        print(e)
    except ConnectionError as e:
        print(e)

@api_view(['GET'])
def first_missing_positive(request):
    array = request.query_params.get('array')
    array = literal_eval(array)
    if (1 not in array):
        return Response(1)
    sorted_array = np.sort(array)
    # linearly scan the sorted array:
    i = 0
    while i<len(sorted_array)-1 and (sorted_array[i]<0 or sorted_array[i+1]-sorted_array[i]<=1):
        i+=1
    return Response(sorted_array[i]+1)
