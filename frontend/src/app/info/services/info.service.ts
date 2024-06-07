import { Injectable } from '@angular/core';
import { Observable, catchError, switchMap, throwError } from 'rxjs';
import { AppConfig } from '../../app.models';
import { BaseApiService } from '../../base/services/base-api.service';
import { RaspberryPiBoardInfo } from '../models/info.models';

const BASE_PATH = '/v1/info';

@Injectable({
  providedIn: 'root',
})
export class InfoService extends BaseApiService {
  public getInfo(): Observable<RaspberryPiBoardInfo> {
    return this.getAppConfig().pipe(
      switchMap((config: AppConfig) => {
        const url = new URL(`${config.api.host}${BASE_PATH}`);
        return this.httpClient.get<RaspberryPiBoardInfo>(url.toString()).pipe(
          catchError((error) => {
            this.showToast(
              `There was an error retrieving the board info!`,
              'danger'
            );
            return throwError(() => error);
          })
        );
      })
    );
  }
}
