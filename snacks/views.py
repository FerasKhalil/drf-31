from rest_framework import generics
from .models import snacks
from .serializers import snacksSerializer

class snacksList(generics.ListCreateAPIView):
    queryset = snacks.objects.all()
    serializer_class = snacksSerializer
    
class snacksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = snacks.objects.all()
    serializer_class = snacksSerializer