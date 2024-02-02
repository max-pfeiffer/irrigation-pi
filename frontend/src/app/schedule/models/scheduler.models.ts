export enum Repeat {
  EveryDay = 'every_day',
  Weekdays = 'weekdays',
  Weekends = 'weekends',
  Monday = 'monday',
  Tuesday = 'tuesday',
  Wednesday = 'wednesday',
  Thursday = 'thursday',
  Friday = 'friday',
  Saturday = 'saturday',
  Sunday = 'sunday',
}

export enum RelayBoardType {
  WaveshareRpiRelayBoard = 'waveshare_rpi_relay_board',
}

export interface Schedule {
  id?: number;
  start_time: string;
  duration: number;
  repeat: Repeat;
  active: boolean;
  relay_board_type: RelayBoardType;
  relay_position: number;
}

export const createSchedule = (overrides?: Partial<Schedule>): Schedule => {
  return {
    start_time: '12:00',
    duration: 10,
    repeat: Repeat.EveryDay,
    active: false,
    relay_board_type: RelayBoardType.WaveshareRpiRelayBoard,
    relay_position: 1,
    ...overrides,
  };
};
