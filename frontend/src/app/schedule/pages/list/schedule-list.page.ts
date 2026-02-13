import {
  ChangeDetectionStrategy,
  Component,
  inject,
  signal,
  ViewChild,
} from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {
  IonButton,
  IonButtons,
  IonContent,
  IonHeader,
  IonIcon,
  IonList,
  IonMenuButton,
  IonTitle,
  IonToolbar,
  NavController,
  ViewDidEnter,
} from '@ionic/angular/standalone';
import { addIcons } from 'ionicons';
import { addOutline } from 'ionicons/icons';
import { finalize } from 'rxjs';
import { ScheduleTileComponent } from '../../components/tile/schedule-tile.component';
import { ScheduleResponse } from '../../models/scheduler.models';
import { ScheduleService } from '../../services/schedule.service';

@Component({
  selector: 'app-schedule-list',
  templateUrl: './schedule-list.page.html',
  styleUrls: ['./schedule-list.page.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [
    ScheduleTileComponent,
    IonHeader,
    IonToolbar,
    IonButtons,
    IonMenuButton,
    IonTitle,
    IonButton,
    IonIcon,
    IonContent,
    IonList,
  ],
})
export class ScheduleListPage implements ViewDidEnter {
  public schedulerService = inject(ScheduleService);
  public navController = inject(NavController);
  public route = inject(ActivatedRoute);

  @ViewChild('scheduleList')
  public scheduleList: IonList;
  public schedules = signal<ScheduleResponse[]>([]);

  constructor() {
    addIcons({
      addOutline,
    });
  }

  public ionViewDidEnter(): void {
    this.refreshList();
  }

  public refreshList(): void {
    this.schedulerService
      .getSchedules()
      .pipe(
        finalize(() => this.scheduleList.closeSlidingItems().catch(() => {})),
      )
      .subscribe({
        next: (_schedules: ScheduleResponse[]) => {
          this.schedules.set(_schedules);
        },
      });
  }

  public addSchedule(): void {
    this.navController.navigateForward(['edit'], {
      relativeTo: this.route,
    });
  }
}
