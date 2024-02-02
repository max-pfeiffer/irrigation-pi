import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ToastController } from '@ionic/angular';
import { Observable, catchError, tap, throwError } from 'rxjs';
import {
  CreateScheduleRequestBody,
  CreateScheduleResponse,
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
      catchError((error) => {
        this.showToast(`There was an error retrieving the schedule!`, 'danger');
        return throwError(() => error);
      })
    );
  }

  public getSchedules(): Observable<ScheduleResponse[]> {
    const url = new URL(`${BASE_PATH}/`);
    return this.httpClient.get<ScheduleResponse[]>(url.toString()).pipe(
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
    const url = new URL(`${BASE_PATH}/`);
    return this.httpClient
      .post<CreateScheduleResponse>(url.toString(), schedule)
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
    const url = new URL(`${BASE_PATH}/${primaryKey}`);
    return this.httpClient.put<void>(url.toString(), schedule).pipe(
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
}
