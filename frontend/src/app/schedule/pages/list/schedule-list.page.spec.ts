import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ScheduleListPage } from './schedule-list.page';

describe('SchedulerPage', () => {
  let component: ScheduleListPage;
  let fixture: ComponentFixture<ScheduleListPage>;

  beforeEach(async(() => {
    fixture = TestBed.createComponent(ScheduleListPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
