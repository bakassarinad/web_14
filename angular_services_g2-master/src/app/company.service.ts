import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { NEWS_LIST } from './newsList';
import { HttpClient } from '@angular/common/http';
import { Company, LoginResponse, Vacancy } from './models';

@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  BASE_URL = 'http://localhost:8000'
  constructor(private http: HttpClient) {}
  getCompanyList(): Observable<Company[]> {
    return this.http.get<Company[]>(`${this.BASE_URL}/api/companies_gen/`)
   // return of(this.news);
  }
  getCompany(id): Observable<Company> {
    return this.http.get<Company>(`${this.BASE_URL}/api/companies/${id}/`);
  }

  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.BASE_URL}/api/login/`, {
      username,
      password
    })
  }
  deleteCompany(id): Observable<any> {
    return this.http.delete(`${this.BASE_URL}/api/companies/${id}/`);
  }

  getVacancyList(id): Observable<Vacancy> {
    return this.http.get<Vacancy>(`${this.BASE_URL}/api/company/${id}/vacancy`);
  }
  // getNewsPageById(id): Observable<any> {
  //   const neededNewsPage = this.news.find(newsPage => newsPage.id === id);
  //   return of(neededNewsPage);
  // }

}
