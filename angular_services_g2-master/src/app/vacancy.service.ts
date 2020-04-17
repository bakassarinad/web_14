// import { Injectable } from '@angular/core';
// import { HttpClient } from '@angular/common/http';
// import { Vacancy } from './models';
// import { Observable } from 'rxjs';

// @Injectable({
//   providedIn: 'root'
// })
// export class VacancyService {

//   constructor(private http: HttpClient) { }

//   BASE_URL = 'http://localhost:8000'

//   getVacancyList(id: number): Observable<Vacancy[]> {
//     return this.http.get<Vacancy[]>(`${this.BASE_URL}/api/company/${id}/vacancy/`);
//   }
// }