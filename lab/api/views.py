import json

from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Company, Vacancy
from django.views import View

# Create your views here.
@csrf_exempt 
def company_list(request):
    if request.method == "GET":
        companies = Company.objects.all()
        json_companies = [c.to_json() for c in companies]
        return JsonResponse(json_companies, safe=False)
    elif request.method == "POST":
        request_body = json.loads(request.body)
        company = Company.objects.create(name=request_body['name'],
                                        description=request_body['description'],
                                        city=request_body['city'],
                                        address=request_body['address']) # autoincrement for id #
        return JsonResponse(company.to_json())
  

@csrf_exempt
def company_detail(request, id):
    try:
        company = Company.objects.get(id = id)
        if request.method == "GET":
            return JsonResponse(company.to_json())
        elif request.method == "PUT":
                request_body = json.loads(request.body)
                company.name = request_body.get('name', company.name)
                company.description = request_body.get('description', company.description)
                company.city = request_body.get('city', company.city)
                company.address = request_body.get('address', company.address)
                company.save()
                return JsonResponse(company.to_json())
        elif request.method == "DELETE":
            company.delete()
            return JsonResponse({'deleted': True})
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 'there is no company :('})

        
@csrf_exempt
def vacancy_by_company(request, id):
    try:
        company = Company.objects.get(id = id)
        if request.method == "GET":
            vacancies = Vacancy.objects.filter(company = id)
            json_vacancies_by_company = [v.to_json() for v in vacancies]
            return JsonResponse(json_vacancies_by_company, safe = False)
        elif request.method == "POST":
            request_body = json.loads(request.body)

            vacancy = Vacancy.objects.create(name=request_body['name'],
                                        description=request_body['description'],
                                        salary=request_body['salary'],
                                        company=company)
                                        
            vacancy.save()
            return JsonResponse(vacancy.to_json())
    except:
        return JsonResponse({'error': 'No vacancies in the company'})

def vacancy_list(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.all()
        json_vacancies = [v.to_json() for v in vacancies]
        return JsonResponse(json_vacancies, safe = False)
    
@csrf_exempt     
def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id = id)
        if request.method == "GET":
           
           return JsonResponse(vacancy.to_json()) 
        elif request.method == "PUT":
            request_body = json.loads(request.body)
            vacancy.name=request_body.get('name', vacancy.name)
            vacancy.description = request_body.get('description', vacancy.description)
            vacancy.salary = request_body.get('salary', vacancy.salary)
            vacancy.save()
            return JsonResponse(vacancy.to_json())
        elif request.method == "DELETE":
            vacancy.delete()
            return JsonResponse({'deleted': True})

       
        
    except:
        return JsonResponse({'error': 'No vacancies with id'})
def top_ten(request):
    if request.method == "GET":
        vacancy_list_ten = Vacancy.objects.all().order_by('salary')[1:10]
        json_vacancy_list_ten = [v.to_json() for v in vacancy_list_ten]
        return JsonResponse(json_vacancy_list_ten, safe = False)
class VacancyClass(View):
    def get(self, request, id):
        vacancy = Vacancy.objects.get(id=id)
        return JsonResponse(vacancy.to_json())
    def put(self, request, id):
            vacancy = Vacancy.objects.get(id = id)
            request_body = json.loads(request.body)
            vacancy.name=request_body.get('name', vacancy.name)
            vacancy.description = request_body.get('description', vacancy.description)
            vacancy.salary = request_body.get('salary', vacancy.salary)
            vacancy.save()
    def delete(self, request, id):
        vacancy = Vacancy.objects.get(id=id)
        vacancy.delete()
        return JsonResponse({'deleted': True})