import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  inject,
  input,
  output,
} from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, RouterLink } from '@angular/router';
import {
  AlertController,
  IonChip,
  IonIcon,
  IonItemOption,
  IonItemOptions,
  IonItemSliding,
  IonLabel,
  NavController,
} from '@ionic/angular/standalone';
import { addIcons } from 'ionicons';
import { trash } from 'ionicons/icons';
import { finalize } from 'rxjs';
import { ScheduleResponse } from '../../models/scheduler.models';
import { DisplayStringPipe } from '../../pipes/display-string.pipe';
import { ScheduleService } from '../../services/schedule.service';

@Component({
  selector: 'app-schedule-tile',
  templateUrl: './schedule-tile.component.html',
  styleUrls: ['./schedule-tile.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [
    FormsModule,
    RouterLink,
    DisplayStringPipe,
    IonItemSliding,
    IonLabel,
    IonChip,
    IonItemOptions,
    IonItemOption,
    IonIcon,
  ],
})
export class ScheduleTileComponent {
  public scheduleService = inject(ScheduleService);
  public cdr = inject(ChangeDetectorRef);
  public alertController = inject(AlertController);
  public navController = inject(NavController);
  public route = inject(ActivatedRoute);

  public schedule = input<ScheduleResponse>();

  public refreshList = output();

  public constructor() {
    addIcons({
      trash,
    });
  }

  public toggleActive(): void {
    let { id, ...payload } = this.schedule();
    payload = { ...payload, active: !this.schedule().active };
    this.scheduleService
      .updateSchedule(id, payload)
      .pipe(
        finalize(() => {
          this.refreshList.emit();
        }),
      )
      .subscribe();
  }

  public async deleteSchedule(): Promise<void> {
    const alert = await this.alertController.create({
      header: 'Are you sure?',
      message: 'Do you really want to delete this schedule?',
      buttons: [
        {
          text: 'Yes',
          role: 'destructive',
          handler: () => {
            this.scheduleService
              .deleteSchedule(this.schedule().id)
              .pipe(
                finalize(() => {
                  this.refreshList.emit();
                }),
              )
              .subscribe();
          },
        },
        {
          text: 'No',
          role: 'cancel',
        },
      ],
    });
    await alert.present();
  }
}
