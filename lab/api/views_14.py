from django.http import JsonResponse
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.views import APIView
@api_view(['GET', 'POST' ])
def company_list(request):
     
    if request.method == 'GET': 
            companies = Company.objects.all()      
            serializer = CompanySerializer(companies, many = True)
            return Response(serializer.data)
    elif request.method == "POST":
        companies = Company.objects.all()
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, id):
    try:
        company = Company.objects.get(id = id)
    except Company.DoesNotExist  as e:
        return Response({'error': str(e)})
    if request.method == "GET":
            serializer = CompanySerializer(company)
            return Response(serializer.data)
    elif request.method == "PUT":
            
            serializer = CompanySerializer(instance=company, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
    elif request.method == "DELETE":
            company.delete()
            return Response({'deleted': True})
    
class VacancyList(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many = True)
        return Response(serializer.data)

class Vacancy_by_Company(APIView):
    def get_object(self, id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)})
    def post(self, request, id):
       
        vacancy = Vacancy(company = self.get_object(id))
        serializer = VacancySerializer(vacancy, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
        return Response(serializer.errors)
    def get(self, request, id):
            vacancies = Vacancy.objects.filter(company = self.get_object(id))
            serializer = VacancySerializer(vacancies, many = True)
            return Response(serializer.data)

class Vacancy_detail(APIView):
    def get_object(self, id):
        try:
            return Vacancy.objects.get(id = id)
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)})
    def get(self, request, id):
         vacancy = self.get_object(id)
         serializer = VacancySerializer(vacancy)
         return Response(serializer.data)
    def put(self, request, id):
            vacancy = self.get_object(id)
            serializer = VacancySerializer(instance = vacancy, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse({'error': serializer.errors})
    def delete(self, request, id):
        vacancy = self.get_object(id)
        vacancy.delete()
        return JsonResponse({'deleted': True})