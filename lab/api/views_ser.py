import json # for json.load
from django.http import JsonResponse
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.http.response import JsonResponse
@csrf_exempt
def company_list(request):
    if request.method == "GET":
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many = True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == "POST":
        request_body = json.loads(request.body)
        serializer = CompanySerializer(data=request_body) # desirealize
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
    return JsonResponse({'error': 'Error'})

@csrf_exempt
def company_detail(request, id):
    try:
        company = Company.objects.get(id = id)
        if request.method == "GET":
            serializer = CompanySerializer(company)
            return JsonResponse(serializer.data)
        elif request.method == "PUT":
            request_body = json.loads(request.body)
            serializer = CompanySerializer(instance=company, data = request_body)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse({'error': serializer.errors})
        elif request.method == "DELETE":
            company.delete()
            return JsonResponse({'deleted': True})
    except Company.DoesNotExist  as e:
        return JsonResponse({'error': str(e)})
@csrf_exempt
def vacancy_list(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many = True)
        return JsonResponse(serializer.data, safe = False)

@csrf_exempt
def vacancy_by_company(request, id):
    company = Company.objects.get(id = id)
    vacancy = Vacancy(company = company)
    if request.method == "POST":
        request_body = json.loads(request.body)
        serializer = VacancySerializer(vacancy, data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})
    elif request.method == "GET":
        vacancies = Vacancy.objects.filter(company = id)
        serializer = VacancySerializer(vacancies, many = True)
        return JsonResponse(serializer.data, safe = False)
@csrf_exempt
def vacancy_detail(request, id):
    vacancy = Vacancy.objects.get(id=id)
    try:
        if request.method == "GET":
            serializer = VacancySerializer(vacancy)
            return JsonResponse(serializer.data)
        elif request.method == "PUT":
            request_body = json.loads(request.body)
            serializer = VacancySerializer(instance = vacancy, data = request_body)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse({'error': serializer.errors})
        elif request.method == "DELETE":
            vacancy.delete()
            return JsonResponse({'deleted': True})
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error':'No such vacancy through serializer :('})






