from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .forms import PDFFajloviForm
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.http import HttpResponse
from django_filters import rest_framework as filters

from .models import Simptomi, Nesrece_Simptomi, Pitanja, Nesrece, PostupciPrvePomoci, RezultatiTestiranja, PDFFajlovi, VideoPrimjeri, Odgovori
from .serializers import SimptomiSerializer, Nesrece_SimptomiSerializer, PitanjaSerializer, NesreceSerializer, PostupciPrvePomociSerializer, RezulttiTestiranjaSerializer, UserSerializer, PDFFajloviSerializer, VideoPrimjeriSerializer, OdgovoriSerializer
from .filters import NesreceFilter, PostupciPrvePomociFilter

# 6. Da bi sada mogli primati post, get put ili delete metode moramo u view-u
# dodati anotacije za funkcije koje rade post, get, put ili delete.
# Zbog toga je potrebno instalirati:
# pip install djangorestframework
# 7. I onda u view dodati sljedeće:


@api_view(['POST'])
def test(request):
    return HttpResponse("Test")


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class PitanjaList(generics.ListCreateAPIView):
    queryset = Pitanja.objects.all()
    serializer_class = PitanjaSerializer


class PitanjaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pitanja.objects.all()
    serializer_class = PitanjaSerializer


class OdgovoriList(generics.ListCreateAPIView):
    queryset = Odgovori.objects.all()
    serializer_class = OdgovoriSerializer


class OdgovoriDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Odgovori.objects.all()
    serializer_class = OdgovoriSerializer


class NesreceList(generics.ListCreateAPIView):
    queryset = Nesrece.objects.all()
    serializer_class = NesreceSerializer
    filter_backends = (filters.DjangoFilterBackend,) # ukljucujemo filter opciju samo za ovaj view tj. nismo filtere ukljucili na globalnom nivou jer nam za sad ne trebaju na ostalim pozivima
    filterset_class = NesreceFilter # dodajemo filter parametre

class NesreceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nesrece.objects.all()
    serializer_class = NesreceSerializer


class SimptomiList(generics.ListCreateAPIView):
    queryset = Simptomi.objects.all()
    serializer_class = SimptomiSerializer


class SimptomiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Simptomi.objects.all()
    serializer_class = SimptomiSerializer


class Nesrece_SimptomiList(generics.ListCreateAPIView):
    queryset = Nesrece_Simptomi.objects.all()
    serializer_class = Nesrece_SimptomiSerializer


class Nesrece_SimptomiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nesrece_Simptomi.objects.all()
    serializer_class = Nesrece_SimptomiSerializer


class PostupciPrvePomociList(generics.ListCreateAPIView):
    queryset = PostupciPrvePomoci.objects.all()
    serializer_class = PostupciPrvePomociSerializer
    filter_backends = (filters.DjangoFilterBackend,) # ukljucujemo filter opciju samo za ovaj view tj. nismo filtere ukljucili na globalnom nivou jer nam za sad ne trebaju na ostalim pozivima
    filterset_class = PostupciPrvePomociFilter # dodajemo filter parametre

class PostupciPrvePomociDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostupciPrvePomoci.objects.all()
    serializer_class = PostupciPrvePomociSerializer


class RezultatiTestiranjaList(generics.ListCreateAPIView):
    queryset = RezultatiTestiranja.objects.all()
    serializer_class = RezulttiTestiranjaSerializer


class RezultatiTestiranjaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RezultatiTestiranja.objects.all()
    serializer_class = RezulttiTestiranjaSerializer


class PDFFajloviList(generics.ListCreateAPIView):
    queryset = PDFFajlovi.objects.all()
    serializer_class = PDFFajloviSerializer


class PDFFajloviDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PDFFajlovi.objects.all()
    serializer_class = PDFFajloviSerializer


class PDFFajloviView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = PDFFajlovi.objects.all()
        serializer = PDFFajloviSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = PDFFajloviSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_file(request, file_id):
    file_obj = PDFFajlovi.objects.get(id=file_id)
    response_data = {
        'fileUrl': file_obj.fajl.url
    }
    return JsonResponse(response_data)


class VideoPrimjeriList(generics.ListCreateAPIView):
    queryset = VideoPrimjeri.objects.all()
    serializer_class = VideoPrimjeriSerializer


class VideoPrimjeriDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VideoPrimjeri.objects.all()
    serializer_class = VideoPrimjeriSerializer
