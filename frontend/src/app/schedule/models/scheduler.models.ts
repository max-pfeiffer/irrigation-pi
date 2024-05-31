import type { Components, Paths } from 'frontend/@types/openapi';

export type ScheduleResponse = Components.Schemas.ScheduleResponse;
export type ScheduleUpdate = Components.Schemas.ScheduleUpdate;
export type ScheduleCreate = Components.Schemas.ScheduleCreate;
export type Repeat = Components.Schemas.Repeat;

export type CreateScheduleRequestBody =
  Paths.CreateScheduleV1SchedulePost.RequestBody;
export type CreateScheduleResponse =
  Paths.CreateScheduleV1SchedulePost.Responses.$200;

export const createSchedule = (
  overrides?: Partial<ScheduleCreate>
): ScheduleCreate => {
  return {
    start_time: '12:00',
    duration: 10,
    repeat: 'every_day',
    active: true,
    relay_position: 1,
    ...overrides,
  };
};
