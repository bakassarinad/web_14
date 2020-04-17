from django.urls import path
from api import views, views_ser, views_14, view_generics
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    # path('companies/', views.company_list),
    # path('companies/<int:id>/', views.company_detail),
    # path('companies/<int:id>/vacancies/', views.vacancy_by_company),
    # path('vacancies/', views.vacancy_list),
    # path('vacancies/<int:id>/', views.vacancy_detail),
    # path('vacancies/top_ten/', views.top_ten),
    # path('vacancy_class/<int:id>/', views.VacancyClass.as_view()),
    # path('companies_ser/', views_ser.company_list),
    # path('companies_ser/<int:id>/', views_ser.company_detail),
    # path('list/', views_ser.vacancy_list),
    # path('companies/<int:id>/list_vacancy/', views_ser.vacancy_by_company),
    # path('vacancy_ser_details/<int:id>/', views_ser.vacancy_detail),


    # # views_14
    # path('companies_14/', views_14.company_list),
    # path('companies_14/<int:id>/', views_14.company_detail),
    # path('vacancies_14/', views_14.VacancyList.as_view()),
    # path('company_14/<int:id>/vacancy/', views_14.Vacancy_by_Company.as_view()),
    # path('vacancy_detail_14/<int:id>/', views_14.Vacancy_detail.as_view()),


    # views_generics
    path('companies_gen/', view_generics.CompanyAPI.as_view()),
    path('companies/<int:pk>/', view_generics.CompanyDetail.as_view()),
    path('vacancyList/', view_generics.VacancyList.as_view()),
    path('vacancy/<int:pk>/', view_generics.VacancyDetail.as_view()),
    path('company/<int:id>/vacancy/', views_14.Vacancy_by_Company.as_view()),
    # superuser login

    path('login/', obtain_jwt_token)
]