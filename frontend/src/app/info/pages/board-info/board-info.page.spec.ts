import { ComponentFixture, TestBed } from '@angular/core/testing';
import { BoardInfoPage } from './board-info.page';

describe('BoardInfoPage', () => {
  let component: BoardInfoPage;
  let fixture: ComponentFixture<BoardInfoPage>;

  beforeEach(async(() => {
    fixture = TestBed.createComponent(BoardInfoPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
