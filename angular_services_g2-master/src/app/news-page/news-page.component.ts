import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CompanyService } from '../company.service';
import {Vacancy, Company} from '../models'
//import { VacancyService } from '../vacancy.service';

@Component({
  selector: 'app-news-page',
  templateUrl: './news-page.component.html',
  styleUrls: ['./news-page.component.css']
})
export class NewsPageComponent implements OnInit {
   vacancies: Vacancy;
    company: Company;
  constructor(private companyService: CompanyService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getCompany();
     this.getVacancyList();
  }

  getCompany() {
    const id = +this.route.snapshot.paramMap.get('id');

    this.companyService.getCompany(id).subscribe(company => this.company = company);
  }
  getVacancyList(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.companyService.getVacancyList(id)
      .subscribe(vacancies => this.vacancies = vacancies );
  }

  // changeTitle() {
  //   const id = +this.route.snapshot.paramMap.get('id');

  //   this.newsService.changeNewsPageTitleById(id, 'Hello Imma new titel');
  // }
}
