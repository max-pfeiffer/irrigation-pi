import { HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, map, switchMap, tap, throwError } from 'rxjs';
import { AppConfig } from '../../app.models';
import { BaseApiService } from '../../base/services/base-api.service';
import {
  CreateScheduleRequestBody,
  CreateScheduleResponse,
  ScheduleCreate,
  ScheduleResponse,
  ScheduleUpdate,
} from '../models/scheduler.models';

const BASE_PATH = '/v1/schedule';

@Injectable({
  providedIn: 'root',
})
export class ScheduleService extends BaseApiService {
  public getSchedule(primaryKey: number): Observable<ScheduleResponse> {
    return this.getAppConfig().pipe(
      switchMap((config: AppConfig) => {
        const url = new URL(`${config.api.host}${BASE_PATH}/${primaryKey}`);
        return this.httpClient.get<ScheduleResponse>(url.toString()).pipe(
          map((schedule) => this.stripSeconds(schedule)),
          catchError((error) => {
            this.showToast(
              `There was an error retrieving the schedule!`,
              'danger'
            );
            return throwError(() => error);
          })
        );
      })
    );
  }

  public getSchedules(): Observable<ScheduleResponse[]> {
    return this.getAppConfig().pipe(
      switchMap((config: AppConfig) => {
        const url = new URL(`${config.api.host}${BASE_PATH}/`);
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
      })
    );
  }

  public createSchedule(
    schedule: CreateScheduleRequestBody
  ): Observable<CreateScheduleResponse> {
    return this.getAppConfig().pipe(
      switchMap((config: AppConfig) => {
        const scheduleWithSeconds = this.addSeconds(schedule);
        const url = new URL(`${config.api.host}${BASE_PATH}/`);
        return this.httpClient
          .post<CreateScheduleResponse>(url.toString(), scheduleWithSeconds)
          .pipe(
            tap(() => {
              this.showToast(`Schedule was created sucessfully!`, 'success');
            }),
            catchError((response: HttpErrorResponse) => {
              const msg =
                response.status === 409
                  ? response.error.detail
                  : 'There was an error creating the schedule!';
              this.showToast(msg, 'danger');
              return throwError(() => response);
            })
          );
      })
    );
  }

  public updateSchedule(
    primaryKey: number,
    schedule: ScheduleUpdate
  ): Observable<void> {
    return this.getAppConfig().pipe(
      switchMap((config: AppConfig) => {
        const scheduleWithSeconds = this.addSeconds(schedule);
        const url = new URL(`${config.api.host}${BASE_PATH}/${primaryKey}`);
        return this.httpClient
          .put<void>(url.toString(), scheduleWithSeconds)
          .pipe(
            tap(() => {
              this.showToast(`Schedule was updated sucessfully!`, 'success');
            }),
            catchError((response: HttpErrorResponse) => {
              const msg =
                response.status === 409
                  ? response.error.detail
                  : 'There was an error updating the schedule!';
              this.showToast(msg, 'danger');
              return throwError(() => response);
            })
          );
      })
    );
  }

  public deleteSchedule(primaryKey: number): Observable<void> {
    return this.getAppConfig().pipe(
      switchMap((config: AppConfig) => {
        const url = new URL(`${config.api.host}${BASE_PATH}/${primaryKey}`);
        return this.httpClient.delete<void>(url.toString()).pipe(
          tap(() => {
            this.showToast(`Schedule was deleted sucessfully!`, 'success');
          }),
          catchError((error) => {
            this.showToast(
              `There was an error deleting the schedule!`,
              'danger'
            );
            return throwError(() => error);
          })
        );
      })
    );
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
