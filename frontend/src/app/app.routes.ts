import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    redirectTo: 'schedules',
    pathMatch: 'full',
  },
  {
    path: 'schedules',
    loadComponent: () => import('./schedule/pages/list/schedule-list.page').then( m => m.ScheduleListPage)
  },
  {
    path: 'schedules/edit',
    loadComponent: () => import('./schedule/pages/edit/schedule-edit/schedule-edit.page').then( m => m.ScheduleEditPage)
  },
  {
    path: 'schedules/edit/:id',
    loadComponent: () => import('./schedule/pages/edit/schedule-edit/schedule-edit.page').then( m => m.ScheduleEditPage)
  },
];
