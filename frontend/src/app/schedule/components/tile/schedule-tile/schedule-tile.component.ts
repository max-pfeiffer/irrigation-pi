import { CommonModule } from '@angular/common';
import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  EventEmitter,
  Input,
  Output,
} from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AlertController, IonicModule, NavController } from '@ionic/angular';
import { finalize } from 'rxjs';
import { Schedule } from '../../../models/scheduler.models';
import { ScheduleService } from '../../../services/schedule.service';
import { trash } from 'ionicons/icons';
import { addIcons } from 'ionicons';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { DisplayStringPipe } from '../../../pipes/display-string.pipe';

@Component({
  selector: 'app-schedule-tile',
  templateUrl: './schedule-tile.component.html',
  styleUrls: ['./schedule-tile.component.scss'],
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [
    IonicModule,
    CommonModule,
    FormsModule,
    RouterLink,
    DisplayStringPipe,
  ],
})
export class ScheduleTileComponent {
  @Input()
  public schedule: Schedule;

  @Output()
  public refreshList = new EventEmitter<void>();

  public constructor(
    public schedulerService: ScheduleService,
    public cdr: ChangeDetectorRef,
    public alertController: AlertController,
    public navController: NavController,
    public route: ActivatedRoute
  ) {
    addIcons({
      trash,
    });
  }

  public toggleActive(): void {
    const payload: Schedule = {
      ...this.schedule,
      active: !this.schedule.active,
    };
    delete payload.id;
    this.schedulerService
      .updateSchedule(this.schedule.id, payload)
      .pipe(
        finalize(() => {
          this.refreshList.emit();
        })
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
            this.schedulerService
              .deleteSchedule(this.schedule.id)
              .pipe(
                finalize(() => {
                  this.refreshList.emit();
                })
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
