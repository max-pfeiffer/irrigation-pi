import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Schedule, createSchedule } from '../models/scheduler.models';

const BASE_PATH = 'http://localhost:8000/v1/schedule';

@Injectable({
  providedIn: 'root',
})
export class ScheduleService {
  private mockSchedules: Schedule[];
  public constructor(public httpClient: HttpClient) {
    this.mockSchedules = [{ ...createSchedule() }];
  }

  public getSchedule(primaryKey: number): Observable<Schedule> {
    const url = new URL(`${BASE_PATH}/${primaryKey}`);
    return this.httpClient.get<Schedule>(url.toString());
  }

  public getSchedules(): Observable<Schedule[]> {
    const url = new URL(`${BASE_PATH}/`);
    return this.httpClient.get<Schedule[]>(url.toString());
  }

  public createSchedule(schedule: Schedule): Observable<number> {
    const url = new URL(`${BASE_PATH}/`);
    return this.httpClient.post<number>(url.toString(), schedule);
  }

  public updateSchedule(
    primaryKey: number,
    schedule: Schedule
  ): Observable<void> {
    const url = new URL(`${BASE_PATH}/${primaryKey}`);
    return this.httpClient.put<void>(url.toString(), schedule);
  }

  public deleteSchedule(primaryKey: number): Observable<void> {
    const url = new URL(`${BASE_PATH}/${primaryKey}`);
    return this.httpClient.delete<void>(url.toString());
  }
}
