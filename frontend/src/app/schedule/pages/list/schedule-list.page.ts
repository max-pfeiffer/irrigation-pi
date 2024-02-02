import { CommonModule } from '@angular/common';
import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
} from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { IonicModule, NavController, ViewDidEnter } from '@ionic/angular';
import { addIcons } from 'ionicons';
import { addOutline } from 'ionicons/icons';
import { ScheduleTileComponent } from '../../components/tile/schedule-tile/schedule-tile.component';
import { ScheduleResponse } from '../../models/scheduler.models';
import { ScheduleService } from '../../services/schedule.service';

@Component({
  selector: 'app-schedule-list',
  templateUrl: './schedule-list.page.html',
  styleUrls: ['./schedule-list.page.scss'],
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [IonicModule, CommonModule, ScheduleTileComponent],
})
export class ScheduleListPage implements ViewDidEnter {
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

  public scheduleList: ScheduleResponse[] = [];

  public ionViewDidEnter(): void {
    this.refreshList();
  }

  public refreshList(): void {
    this.schedulerService.getSchedules().subscribe({
      next: (_scheduleList: ScheduleResponse[]) => {
        this.scheduleList = _scheduleList;
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
