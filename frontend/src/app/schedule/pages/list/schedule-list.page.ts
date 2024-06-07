import { CommonModule } from '@angular/common';
import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
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
  IonListHeader,
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
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [
    CommonModule,
    ScheduleTileComponent,
    IonHeader,
    IonToolbar,
    IonButtons,
    IonMenuButton,
    IonTitle,
    IonButton,
    IonIcon,
    IonContent,
    IonListHeader,
    IonList,
  ],
})
export class ScheduleListPage implements ViewDidEnter {
  @ViewChild('scheduleList')
  public scheduleList: IonList;
  public schedules: ScheduleResponse[] = [];

  constructor(
    public schedulerService: ScheduleService,
    public cdr: ChangeDetectorRef,
    public navController: NavController,
    public route: ActivatedRoute
  ) {
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
        finalize(() => this.scheduleList.closeSlidingItems().catch(() => {}))
      )
      .subscribe({
        next: (_schedules: ScheduleResponse[]) => {
          this.schedules = _schedules;
          this.cdr.detectChanges();
        },
      });
  }

  public addSchedule(): void {
    this.navController.navigateForward(['edit'], {
      relativeTo: this.route,
    });
  }
}
