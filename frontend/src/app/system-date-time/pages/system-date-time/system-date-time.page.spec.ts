import { provideHttpClient } from '@angular/common/http';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { SystemDateTimePage } from './system-date-time.page';

describe('SystemDateTimePage', () => {
  let component: SystemDateTimePage;
  let fixture: ComponentFixture<SystemDateTimePage>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [SystemDateTimePage],
      providers: [provideHttpClient()],
    });
    fixture = TestBed.createComponent(SystemDateTimePage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
