import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ToastController } from '@ionic/angular/standalone';
import { Observable, catchError, map, tap, throwError } from 'rxjs';
import {
  CreateScheduleRequestBody,
  CreateScheduleResponse,
  ScheduleCreate,
  ScheduleResponse,
  ScheduleUpdate,
} from '../models/scheduler.models';
const BASE_PATH = 'http://localhost:8000/v1/schedule';

@Injectable({
  providedIn: 'root',
})
export class ScheduleService {
  public constructor(
    public httpClient: HttpClient,
    public toastController: ToastController
  ) {}

  public getSchedule(primaryKey: number): Observable<ScheduleResponse> {
    const url = new URL(`${BASE_PATH}/${primaryKey}`);
    return this.httpClient.get<ScheduleResponse>(url.toString()).pipe(
      map((schedule) => this.stripSeconds(schedule)),
      catchError((error) => {
        this.showToast(`There was an error retrieving the schedule!`, 'danger');
        return throwError(() => error);
      })
    );
  }

  public getSchedules(): Observable<ScheduleResponse[]> {
    const url = new URL(`${BASE_PATH}/`);
    return this.httpClient.get<ScheduleResponse[]>(url.toString()).pipe(
      map((schedules) => schedules.map((s) => this.stripSeconds(s))),
      catchError((error) => {
        this.showToast(
          `There was an error getting the list of schedules!`,
          'danger'
        );
        return throwError(() => error);
      })
    );
  }

  public createSchedule(
    schedule: CreateScheduleRequestBody
  ): Observable<CreateScheduleResponse> {
    const scheduleWithSeconds = this.addSeconds(schedule);
    const url = new URL(`${BASE_PATH}/`);
    return this.httpClient
      .post<CreateScheduleResponse>(url.toString(), scheduleWithSeconds)
      .pipe(
        tap(() => {
          this.showToast(`Schedule was created sucessfully!`, 'success');
        }),
        catchError((error) => {
          this.showToast(`There was an error creating the schedule!`, 'danger');
          return throwError(() => error);
        })
      );
  }

  public updateSchedule(
    primaryKey: number,
    schedule: ScheduleUpdate
  ): Observable<void> {
    const scheduleWithSeconds = this.addSeconds(schedule);
    const url = new URL(`${BASE_PATH}/${primaryKey}`);
    return this.httpClient.put<void>(url.toString(), scheduleWithSeconds).pipe(
      tap(() => {
        this.showToast(`Schedule was updated sucessfully!`, 'success');
      }),
      catchError((error) => {
        this.showToast(`There was an error updating the schedule!`, 'danger');
        return throwError(() => error);
      })
    );
  }

  public deleteSchedule(primaryKey: number): Observable<void> {
    const url = new URL(`${BASE_PATH}/${primaryKey}`);
    return this.httpClient.delete<void>(url.toString()).pipe(
      tap(() => {
        this.showToast(`Schedule was deleted sucessfully!`, 'success');
      }),
      catchError((error) => {
        this.showToast(`There was an error deleting the schedule!`, 'danger');
        return throwError(() => error);
      })
    );
  }

  public showToast(message: string, color: string) {
    this.toastController
      .create({
        message,
        color,
        duration: 3000,
        position: 'bottom',
      })
      .then((toastElement) => toastElement.present())
      .catch(() => {});
  }

  public stripSeconds(schedule: ScheduleResponse): ScheduleResponse {
    let match = schedule.start_time.match(/^([0-9]{1,2}):([0-9]{1,2})/);
    return {
      ...schedule,
      start_time: match ? `${match[1]}:${match[2]}` : schedule.start_time,
    };
  }

  public addSeconds(
    schedule: ScheduleCreate | ScheduleUpdate
  ): ScheduleCreate | ScheduleUpdate {
    let match = schedule.start_time.match(/^([0-9]{1,2}):([0-9]{1,2})/);
    return {
      ...schedule,
      start_time: match ? `${match[1]}:${match[2]}:00` : schedule.start_time,
    };
  }
}
