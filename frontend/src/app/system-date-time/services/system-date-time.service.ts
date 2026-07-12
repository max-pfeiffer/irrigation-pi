import { Injectable } from '@angular/core';
import { Observable, catchError, switchMap, tap, throwError } from 'rxjs';
import { AppConfig } from '../../app.models';
import { BaseApiService } from '../../base/services/base-api.service';
import { SystemDateTime } from '../models/system-date-time.models';

const BASE_PATH = '/v1/system-date-time';

@Injectable({
  providedIn: 'root',
})
export class SystemDateTimeService extends BaseApiService {
  public getSystemDateTime(): Observable<SystemDateTime> {
    return this.getAppConfig().pipe(
      switchMap((config: AppConfig) => {
        const url = new URL(`${config.api.host}${BASE_PATH}/`);
        return this.httpClient.get<SystemDateTime>(url.toString()).pipe(
          catchError((error) => {
            this.showToast(
              `There was an error retrieving the system date and time!`,
              'danger'
            );
            return throwError(() => error);
          })
        );
      })
    );
  }

  public setSystemDateTime(
    systemDateTime: SystemDateTime
  ): Observable<void> {
    return this.getAppConfig().pipe(
      switchMap((config: AppConfig) => {
        const url = new URL(`${config.api.host}${BASE_PATH}/`);
        return this.httpClient.put<void>(url.toString(), systemDateTime).pipe(
          tap(() => {
            this.showToast(
              `System date and time was updated sucessfully!`,
              'success'
            );
          }),
          catchError((error) => {
            this.showToast(
              `There was an error setting the system date and time!`,
              'danger'
            );
            return throwError(() => error);
          })
        );
      })
    );
  }
}
