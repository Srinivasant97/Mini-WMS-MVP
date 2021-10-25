from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import order, Inventory
from .serializers import OrderSerializers
from rest_framework.views import APIView
# Create your views here.

dummy = {
    'order_number': 1000,
    'source': 'Item',
    'Lines': {'name': 'A', 'quantity': 5}
}


class Hello(APIView):
    def post(self, request, *args, **kwargs):
        I = Inventory.objects.all()
        Pa = False
        for x in I:
            if x.quantity > 0:
                Pa = True
        if not Pa:
            return HttpResponse(status=500)

        a = OrderSerializers(data=request.data)
        if a.is_valid():
            a.save()
            for i in a.data["Lines"]:
                if i["quantity"] < 1 or i["quantity"] > 5:
                    return HttpResponse(status=400)
                Temp = Inventory.objects.get(name=i["name"])
                Temp.quantity -= i["quantity"]
                Temp.save()
            return Response(a.data)
        return Response(a.errors)


class Report(APIView):
    def get(self, request, *args, **kwargs):
        Ord = order.objects.all()
        H = []
        for i in Ord:
            se = OrderSerializers(i)
            H.append(se.data)

        return Response(H)


class Setup(APIView):
    def post(self, request, *args, **kwargs):
        for i in request.data:
            SKU = Inventory.objects.get(name=i)
            SKU.quantity = request.data[i]
            SKU.save()
        return HttpResponse("SKU Created Successfully")
