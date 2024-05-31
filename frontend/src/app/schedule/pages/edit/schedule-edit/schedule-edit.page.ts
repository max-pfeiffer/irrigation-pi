import { CommonModule } from '@angular/common';
import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  OnInit,
} from '@angular/core';
import {
  FormControl,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import {
  IonBackButton,
  IonButton,
  IonButtons,
  IonContent,
  IonHeader,
  IonInput,
  IonItem,
  IonItemGroup,
  IonLabel,
  IonList,
  IonTitle,
  IonToggle,
  IonToolbar,
  NavController,
  PickerController,
  ToastController,
} from '@ionic/angular/standalone';
import { Observable, of, switchMap } from 'rxjs';
import {
  Repeat,
  ScheduleCreate,
  ScheduleUpdate,
  createSchedule,
} from '../../../models/scheduler.models';
import { DisplayStringPipe } from '../../../pipes/display-string.pipe';
import { ScheduleService } from '../../../services/schedule.service';

@Component({
  selector: 'app-schedule-edit',
  templateUrl: './schedule-edit.page.html',
  styleUrls: ['./schedule-edit.page.scss'],
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    DisplayStringPipe,
    IonHeader,
    IonToolbar,
    IonButtons,
    IonBackButton,
    IonTitle,
    IonContent,
    IonList,
    IonItemGroup,
    IonItem,
    IonLabel,
    IonButton,
    IonInput,
    IonToggle,
  ],
})
export class ScheduleEditPage implements OnInit {
  public id: number | null = null;
  public addEditForm: FormGroup;
  public repeatOptions: { text: string; value: string }[];
  public hourOptions: { text: string; value: string }[];
  public minuteOptions: { text: string; value: string }[];
  public cancelButton = {
    text: 'Cancel',
    role: 'cancel',
  };
  public repeatValues: Repeat[] = [
    'every_day',
    'weekdays',
    'weekends',
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday',
  ];
  public displayStringPipe: DisplayStringPipe;

  public constructor(
    public activatedRoute: ActivatedRoute,
    public scheduleService: ScheduleService,
    public cdr: ChangeDetectorRef,
    public pickerCtrl: PickerController,
    public toastController: ToastController,
    public navController: NavController
  ) {
    this.displayStringPipe = new DisplayStringPipe();
    this.repeatOptions = this.repeatValues.map((value) => {
      return {
        text: this.displayStringPipe.transform(value),
        value,
      };
    });

    this.hourOptions = [...Array(24)].map((_, index) => {
      const hour = String(index).padStart(2, '0');
      return {
        text: hour,
        value: hour,
      };
    });
    this.minuteOptions = [...Array(60)].map((_, index) => {
      const minute = String(index).padStart(2, '0');
      return {
        text: minute,
        value: minute,
      };
    });

    this.addEditForm = new FormGroup({
      start_time: new FormControl<string>('', [
        Validators.required,
        Validators.pattern('^[0-9]{1,2}:[0-9]{1,2}$'),
      ]),
      duration: new FormControl<number>(1, [
        Validators.min(1),
        Validators.required,
        Validators.pattern('^[0-9]+$'),
      ]),
      repeat: new FormControl<Repeat>('every_day', Validators.required),
      active: new FormControl<boolean>(true, Validators.required),
      relay_position: new FormControl<number>(1, [
        Validators.min(1),
        Validators.pattern('^[0-9]+$'),
      ]),
    });
  }

  public ngOnInit(): void {
    this.id = parseInt(
      this.activatedRoute.snapshot.paramMap.get('id') as string
    );
    of(createSchedule())
      .pipe(
        switchMap((s) =>
          this.id ? this.scheduleService.getSchedule(this.id) : of(s)
        )
      )
      .subscribe((schedule: ScheduleCreate | ScheduleUpdate) => {
        this.addEditForm.patchValue(schedule);
        this.cdr.detectChanges();
      });
  }

  public async openRepeatPicker() {
    const picker = await this.pickerCtrl.create({
      columns: [
        {
          name: 'repeat',
          options: this.repeatOptions,
        },
      ],
      buttons: [
        { ...this.cancelButton },
        {
          text: 'Confirm',
          handler: (data: {
            repeat: { text: string; value: string; columnIndex: number };
          }) => {
            this.addEditForm.patchValue({ repeat: data.repeat.value });
            this.cdr.detectChanges();
          },
        },
      ],
    });
    (await picker.getColumn('repeat')).selectedIndex = this.repeatOptions
      .map(({ value }) => value)
      .findIndex(
        (value) => value === this.addEditForm?.controls?.['repeat']?.value
      );
    await picker.present();
  }

  public async openStartTimePicker() {
    const picker: HTMLIonPickerLegacyElement = await this.pickerCtrl.create({
      columns: [
        {
          name: 'hour',
          options: this.hourOptions,
        },
        {
          name: 'minute',
          options: this.minuteOptions,
        },
      ],
      buttons: [
        { ...this.cancelButton },
        {
          text: 'Confirm',
          handler: (data: {
            hour: { text: string; value: string; columnIndex: number };
            minute: { text: string; value: string; columnIndex: number };
          }) => {
            this.addEditForm.patchValue({
              start_time: `${data.hour.value}:${data.minute.value}`,
            });
            this.cdr.detectChanges();
          },
        },
      ],
    });
    const match = this.addEditForm?.controls?.['start_time']?.value?.match(
      /^([0-9]{1,2}):([0-9]{1,2})/
    );
    if (match) {
      (await picker.getColumn('hour')).selectedIndex = parseInt(match[1]);
      (await picker.getColumn('minute')).selectedIndex = parseInt(match[2]);
    }
    await picker.present();
  }

  public onSubmit(): void {
    // console.log(JSON.stringify(this.addEditForm.value));
    if (this.addEditForm.status === 'VALID') {
      let action: Observable<number | void>;
      if (this.id) {
        action = this.scheduleService.updateSchedule(
          this.id,
          this.addEditForm.value
        );
      } else {
        action = this.scheduleService.createSchedule(this.addEditForm.value);
      }
      action.subscribe(() => {
        this.navController.navigateBack(['schedules']).catch(() => {});
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
}
