import { DatePipe } from '@angular/common';
import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  inject,
  signal,
} from '@angular/core';
import {
  FormControl,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import {
  IonButton,
  IonButtons,
  IonContent,
  IonDatetime,
  IonDatetimeButton,
  IonHeader,
  IonItem,
  IonLabel,
  IonList,
  IonMenuButton,
  IonModal,
  IonTitle,
  IonToolbar,
  ToastController,
  ViewDidEnter,
} from '@ionic/angular/standalone';
import { SystemDateTime } from '../../models/system-date-time.models';
import { SystemDateTimeService } from '../../services/system-date-time.service';

@Component({
  selector: 'app-system-date-time',
  templateUrl: './system-date-time.page.html',
  styleUrls: ['./system-date-time.page.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [
    DatePipe,
    ReactiveFormsModule,
    IonHeader,
    IonToolbar,
    IonButtons,
    IonMenuButton,
    IonTitle,
    IonContent,
    IonList,
    IonItem,
    IonLabel,
    IonButton,
    IonDatetime,
    IonDatetimeButton,
    IonModal,
  ],
})
export class SystemDateTimePage implements ViewDidEnter {
  public systemDateTimeService = inject(SystemDateTimeService);
  public cdr = inject(ChangeDetectorRef);
  public toastController = inject(ToastController);

  public currentDateTime = signal<string | null>(null);
  public setDateTimeForm: FormGroup;

  public constructor() {
    this.setDateTimeForm = new FormGroup({
      date_time: new FormControl<string>('', Validators.required),
    });
  }

  public ionViewDidEnter(): void {
    this.loadSystemDateTime();
  }

  public loadSystemDateTime(): void {
    this.systemDateTimeService
      .getSystemDateTime()
      .subscribe((systemDateTime: SystemDateTime) => {
        this.currentDateTime.set(systemDateTime.date_time);
        this.setDateTimeForm.patchValue({
          date_time: this.toLocalIsoString(new Date(systemDateTime.date_time)),
        });
        this.cdr.detectChanges();
      });
  }

  public useDeviceTime(): void {
    this.setDateTimeForm.patchValue({
      date_time: this.toLocalIsoString(new Date()),
    });
    this.cdr.detectChanges();
  }

  public onSubmit(): void {
    if (this.setDateTimeForm.status === 'VALID') {
      const systemDateTime: SystemDateTime = {
        date_time: this.toTimezoneAwareIsoString(
          this.setDateTimeForm.value.date_time,
        ),
      };
      this.systemDateTimeService
        .setSystemDateTime(systemDateTime)
        .subscribe(() => {
          this.loadSystemDateTime();
        });
    } else {
      this.toastController
        .create({
          message: 'Please check your input and try again',
          duration: 3000,
          color: 'danger',
          position: 'bottom',
        })
        .then((toastElement) => toastElement.present())
        .catch(() => {});
    }
  }

  // ion-datetime expects an ISO 8601 string without timezone information,
  // representing the time displayed to the user (local time).
  public toLocalIsoString(date: Date): string {
    const pad = (value: number): string => String(value).padStart(2, '0');
    return (
      `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}` +
      `T${pad(date.getHours())}:${pad(date.getMinutes())}:${pad(date.getSeconds())}`
    );
  }

  // The backend expects a timezone aware ISO 8601 string, so the local
  // timezone offset is appended to the value picked with ion-datetime.
  public toTimezoneAwareIsoString(localIsoString: string): string {
    const date = new Date(localIsoString);
    const pad = (value: number): string => String(value).padStart(2, '0');
    const offsetMinutes = -date.getTimezoneOffset();
    const sign = offsetMinutes < 0 ? '-' : '+';
    const offsetHours = pad(Math.floor(Math.abs(offsetMinutes) / 60));
    const offsetRemainder = pad(Math.abs(offsetMinutes) % 60);
    return `${this.toLocalIsoString(date)}${sign}${offsetHours}:${offsetRemainder}`;
  }
}
