import { Injectable } from '@angular/core';
import { Observable, catchError, switchMap, tap, throwError } from 'rxjs';
import { AppConfig } from '../../app.models';
import { BaseApiService } from '../../base/services/base-api.service';
import { Relay, RelayUpdate } from '../models/relay.models';

const BASE_PATH = '/v1/relay';

@Injectable({
  providedIn: 'root',
})
export class RelayService extends BaseApiService {
  public getRelay(position: number): Observable<Relay> {
    return this.getAppConfig().pipe(
      switchMap((config: AppConfig) => {
        const url = new URL(`${config.api.host}${BASE_PATH}/${position}`);
        return this.httpClient.get<Relay>(url.toString()).pipe(
          catchError((error) => {
            this.showToast(
              `There was an error retrieving the relay!`,
              'danger'
            );
            return throwError(() => error);
          })
        );
      })
    );
  }

  public getRelays(): Observable<Relay[]> {
    return this.getAppConfig().pipe(
      switchMap((config: AppConfig) => {
        const url = new URL(`${config.api.host}${BASE_PATH}/`);
        return this.httpClient.get<Relay[]>(url.toString()).pipe(
          catchError((error) => {
            this.showToast(
              `There was an error getting the list of relays!`,
              'danger'
            );
            return throwError(() => error);
          })
        );
      })
    );
  }

  public updateRelay(position: number, relay: RelayUpdate): Observable<void> {
    return this.getAppConfig().pipe(
      switchMap((config: AppConfig) => {
        const url = new URL(`${config.api.host}${BASE_PATH}/${position}`);
        return this.httpClient.put<void>(url.toString(), relay).pipe(
          tap(() => {
            this.showToast(`Relay was updated sucessfully!`, 'success');
          }),
          catchError((error) => {
            this.showToast(`There was an error updating the relay!`, 'danger');
            return throwError(() => error);
          })
        );
      })
    );
  }
}
