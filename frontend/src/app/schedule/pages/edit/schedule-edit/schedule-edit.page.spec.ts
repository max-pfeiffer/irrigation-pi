import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ScheduleEditPage } from './schedule-edit.page';

describe('ScheduleEditPage', () => {
  let component: ScheduleEditPage;
  let fixture: ComponentFixture<ScheduleEditPage>;

  beforeEach(async(() => {
    fixture = TestBed.createComponent(ScheduleEditPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
