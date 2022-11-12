from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Order, Product
 
# Create your views here.
def index(r):
    return JsonResponse({'test':"gustoso"})

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
       
        # ...

        return token

#  signin/Login


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# signup/register
@api_view(['POST'])
def register(request):
    User.objects.create_user(
        username=request.data["username"], password=request.data["password"], email=request.data["email"])
    return JsonResponse({"Register": request.data["username"]})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_members(request):
    return JsonResponse({"welcome": request.data["username"]})

 
# desc ,price,prodName,createdTime, _id
@api_view(['GET','POST','DELETE','PUT'])
def products(request,id=-1):
    if request.method == 'GET':    #method get all
        if int(id) > -1: #get single product
            if int(id)> Product.objects.count(): return JsonResponse({"out of bounds array":"1111"})
            product= Product.objects.get(_id = id)
 
            return JsonResponse({
            "desc":product.desc,
            "price":product.price,
            "weight":product.weight,
            "image" :product.image,
            "amount": product.amount,
            },safe=False)
        else: # return all
            res=[] #create an empty list
            for productObj in Product.objects.all(): #run on every row in the table...
                res.append({"desc":productObj.desc,
                "id":productObj._id,
                "price":productObj.price,
               "amount":productObj.amount,
               "weight":productObj.weight,
                }) #append row by to row to res list
            return JsonResponse(res,safe=False) #return array as json response
    if request.method == 'POST': #method post add new row
        print(request.data['desc'])
        desc =request.data['desc']

        Product.objects.create(desc=request.data['desc'] ,price=request.data['price'],weight=request.data['weight'], image = request.data['image'], amount = request.data['amount'])
        return JsonResponse({'POST':"test"})
    if request.method == 'DELETE': #method delete a row
        temp= Product.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    if request.method == 'PUT': #method update a row
        temp=Product.objects.get(_id = id)
 
        temp.price =request.data['price']
        temp.desc =request.data['desc']
        temp.weight=request.data['weight']
        temp.amount = request.data['amount']
        temp.save()
 
        return JsonResponse({'PUT': id})

