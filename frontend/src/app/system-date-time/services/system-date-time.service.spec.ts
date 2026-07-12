import { provideHttpClient } from '@angular/common/http';
import { TestBed } from '@angular/core/testing';

import { SystemDateTimeService } from './system-date-time.service';

describe('SystemDateTimeService', () => {
  let service: SystemDateTimeService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [provideHttpClient()],
    });
    service = TestBed.inject(SystemDateTimeService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
