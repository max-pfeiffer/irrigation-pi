import { ComponentFixture, TestBed } from '@angular/core/testing';
import { RelayListPage } from './relay-list.page';

describe('RelayListPage', () => {
  let component: RelayListPage;
  let fixture: ComponentFixture<RelayListPage>;

  beforeEach(async(() => {
    fixture = TestBed.createComponent(RelayListPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
