import { HttpClient } from '@angular/common/http';
import { Injectable, Injector } from '@angular/core';
import { ToastController } from '@ionic/angular/standalone';
import { environment } from 'frontend/src/environments/environment';
import { Observable, of, tap } from 'rxjs';
import { AppConfig } from '../../app.models';

const BASE_PATH = '/v1/schedule';

@Injectable({
  providedIn: 'root',
})
export class BaseApiService {
  public httpClient: HttpClient;
  public toastController: ToastController;
  public appConfig: AppConfig = null;

  public constructor(public injector: Injector) {
    this.httpClient = injector.get(HttpClient);
    this.toastController = injector.get(ToastController);
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

  public getAppConfig(): Observable<AppConfig> {
    if (this.appConfig) {
      return of(this.appConfig);
    } else {
      return this.httpClient
        .get<AppConfig>(environment.appConfigUrl)
        .pipe(tap((config) => (this.appConfig = config)));
    }
  }
}
