from django.db.models import F
from rest_framework import status
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AdvertSerializer
from .models import Advert


class AdvertListAPIView(ListAPIView):
    queryset = Advert.objects.select_related('city', 'category').all()
    serializer_class = AdvertSerializer


class AdvertDetailAPIView(APIView):

    def get(self, request, id_advert, *args, **kwargs):
        Advert.objects.filter(pk=id_advert).update(views=F('views') + 1)
        advert_detail = get_object_or_404(Advert, pk=id_advert)
        advert_serializer = AdvertSerializer(instance=advert_detail)

        return Response(advert_serializer.data, status=status.HTTP_200_OK)


