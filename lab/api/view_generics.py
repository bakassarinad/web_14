from rest_framework import generics
from rest_framework import mixins
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer
class CompanyAPI(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
   # permission_classes = (IsAuthenticated,)
class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
   # lookup_url_kwarg=id
class VacancyList(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
   

class VacancyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    # lookup_url_kwarg=id

class VacancybycompanyAPIView(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    def get_company(self, id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)})
    def get_vacancy(self,id):
        return Vacancy(company = self.get_company(id))
    def get(self,request,id,*args, **kwargs):
        return self.list(self,request,id,*args, **kwargs)
    def post(self,request,id,*args, **kwargs):
        return self.create(self,request,id,*args, **kwargs)
