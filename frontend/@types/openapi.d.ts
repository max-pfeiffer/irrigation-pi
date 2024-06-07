import type {
  OpenAPIClient,
  Parameters,
  UnknownParamsObject,
  OperationResponse,
  AxiosRequestConfig,
} from 'openapi-client-axios';

declare namespace Components {
    namespace Schemas {
        /**
         * HTTPValidationError
         */
        export interface HTTPValidationError {
            /**
             * Detail
             */
            detail?: /* ValidationError */ ValidationError[];
        }
        /**
         * RaspberryPiBoardInfo
         * Raspberry Pi board information.
         */
        export interface RaspberryPiBoardInfo {
            /**
             * Revision
             * Raspberry Pi revision
             */
            revision: string;
            /**
             * Model
             * Raspberry Pi model
             */
            model: string;
            /**
             * Pcb Revision
             * Printed Circuit Board (PCB) revision
             */
            pcb_revision: string;
            /**
             * Released
             * Release date
             */
            released: string;
            /**
             * Soc
             * System On a Chip (SoC)
             */
            soc: string;
            /**
             * Manufacturer
             * Manufacturer
             */
            manufacturer: string;
            /**
             * Memory
             * Memory (SDRAM)
             */
            memory: number;
            /**
             * Storage
             * Storage type
             */
            storage: string;
            /**
             * Usb
             * Number of USB ports
             */
            usb: number;
            /**
             * Usb3
             * Number of USB3 ports
             */
            usb3: number;
            /**
             * Ethernet
             * Number of ethernet ports
             */
            ethernet: number;
            /**
             * Eth Speed
             * Ethernet speed
             */
            eth_speed: number;
            /**
             * Wifi
             * Wifi available
             */
            wifi: boolean;
            /**
             * Bluetooth
             * Bluetooth available
             */
            bluetooth: boolean;
            /**
             * Csi
             * Number of Camera Serial Interfaces (CSI)
             */
            csi: number;
            /**
             * Dsi
             * Number of Display Serial Interfaces (DSI)
             */
            dsi: number;
        }
        /**
         * Relay
         * Response schema for Relay object.
         */
        export interface Relay {
            /**
             * Position
             * Relay position on the board
             */
            position: number;
            /**
             * On
             * Indicates if relay is switched on
             */
            on: boolean;
        }
        /**
         * RelayUpdate
         * Update schema for Relay object.
         */
        export interface RelayUpdate {
            /**
             * On
             * Indicates if relay is switched on
             */
            on: boolean;
        }
        /**
         * Repeat
         * Enumeration for repeat values.
         */
        export type Repeat = "every_day" | "weekdays" | "weekends" | "monday" | "tuesday" | "wednesday" | "thursday" | "friday" | "saturday" | "sunday";
        /**
         * ScheduleCreate
         * Creation schema for schedule.
         */
        export interface ScheduleCreate {
            /**
             * Start Time
             * Start time of the schedule
             */
            start_time: string; // time
            /**
             * Duration
             * Duration in minutes
             */
            duration: number;
            /**
             * Repeat
             * Specifies how the schedule is repeated
             */
            repeat: "every_day" | "weekdays" | "weekends" | "monday" | "tuesday" | "wednesday" | "thursday" | "friday" | "saturday" | "sunday";
            /**
             * Active
             * Whether the schedule is active
             */
            active?: boolean;
            /**
             * Relay Position
             * Position of the relay
             */
            relay_position: number;
        }
        /**
         * ScheduleResponse
         * Response schema for schedule.
         */
        export interface ScheduleResponse {
            /**
             * Id
             * Primary key
             */
            id: number;
            /**
             * Start Time
             * Start time of the schedule
             */
            start_time: string; // time
            /**
             * Duration
             * Duration in minutes
             */
            duration: number;
            /**
             * Repeat
             * Specifies how the schedule is repeated
             */
            repeat: "every_day" | "weekdays" | "weekends" | "monday" | "tuesday" | "wednesday" | "thursday" | "friday" | "saturday" | "sunday";
            /**
             * Active
             * Whether the schedule is active
             */
            active: boolean;
            /**
             * Relay Position
             * Position of the relay
             */
            relay_position: number;
        }
        /**
         * ScheduleUpdate
         * Update schema for schedule.
         */
        export interface ScheduleUpdate {
            /**
             * Start Time
             * Start time of the schedule
             */
            start_time?: /**
             * Start Time
             * Start time of the schedule
             */
            string /* time */ | null;
            /**
             * Duration
             * Duration in minutes
             */
            duration?: /**
             * Duration
             * Duration in minutes
             */
            number | null;
            /**
             * Specifies how the schedule is repeated
             */
            repeat?: /* Specifies how the schedule is repeated */ /**
             * Repeat
             * Enumeration for repeat values.
             */
            Repeat | null;
            /**
             * Active
             * Whether the schedule is active
             */
            active?: /**
             * Active
             * Whether the schedule is active
             */
            boolean | null;
            /**
             * Relay Position
             * Position of the relay
             */
            relay_position?: /**
             * Relay Position
             * Position of the relay
             */
            number | null;
        }
        /**
         * ValidationError
         */
        export interface ValidationError {
            /**
             * Location
             */
            loc: (string | number)[];
            /**
             * Message
             */
            msg: string;
            /**
             * Error Type
             */
            type: string;
        }
    }
}
declare namespace Paths {
    namespace CreateScheduleV1SchedulePost {
        export type RequestBody = /**
         * ScheduleCreate
         * Creation schema for schedule.
         */
        Components.Schemas.ScheduleCreate;
        namespace Responses {
            /**
             * Response Create Schedule V1 Schedule  Post
             */
            export type $200 = number;
            export interface $409 {
            }
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace DeleteScheduleV1SchedulePrimaryKeyDelete {
        namespace Parameters {
            /**
             * Primary Key
             */
            export type PrimaryKey = number;
        }
        export interface PathParameters {
            primary_key: /* Primary Key */ Parameters.PrimaryKey;
        }
        namespace Responses {
            export type $200 = any;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace GetBoardInfoV1InfoGet {
        namespace Responses {
            export type $200 = /**
             * RaspberryPiBoardInfo
             * Raspberry Pi board information.
             */
            Components.Schemas.RaspberryPiBoardInfo;
        }
    }
    namespace GetRelayV1RelayPositionGet {
        namespace Parameters {
            /**
             * Position
             */
            export type Position = number;
        }
        export interface PathParameters {
            position: /* Position */ Parameters.Position;
        }
        namespace Responses {
            export type $200 = /**
             * Relay
             * Response schema for Relay object.
             */
            Components.Schemas.Relay;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace GetRelaysV1RelayGet {
        namespace Responses {
            /**
             * Response Get Relays V1 Relay  Get
             */
            export type $200 = /**
             * Relay
             * Response schema for Relay object.
             */
            Components.Schemas.Relay[];
        }
    }
    namespace GetScheduleV1SchedulePrimaryKeyGet {
        namespace Parameters {
            /**
             * Primary Key
             */
            export type PrimaryKey = number;
        }
        export interface PathParameters {
            primary_key: /* Primary Key */ Parameters.PrimaryKey;
        }
        namespace Responses {
            export type $200 = /**
             * ScheduleResponse
             * Response schema for schedule.
             */
            Components.Schemas.ScheduleResponse;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace GetSchedulesV1ScheduleGet {
        namespace Responses {
            /**
             * Response Get Schedules V1 Schedule  Get
             */
            export type $200 = /**
             * ScheduleResponse
             * Response schema for schedule.
             */
            Components.Schemas.ScheduleResponse[];
        }
    }
    namespace UpdateRelayV1RelayPositionPut {
        namespace Parameters {
            /**
             * Position
             */
            export type Position = number;
        }
        export interface PathParameters {
            position: /* Position */ Parameters.Position;
        }
        export type RequestBody = /**
         * RelayUpdate
         * Update schema for Relay object.
         */
        Components.Schemas.RelayUpdate;
        namespace Responses {
            export type $200 = any;
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
    namespace UpdateScheduleV1SchedulePrimaryKeyPut {
        namespace Parameters {
            /**
             * Primary Key
             */
            export type PrimaryKey = number;
        }
        export interface PathParameters {
            primary_key: /* Primary Key */ Parameters.PrimaryKey;
        }
        export type RequestBody = /**
         * ScheduleUpdate
         * Update schema for schedule.
         */
        Components.Schemas.ScheduleUpdate;
        namespace Responses {
            export type $200 = any;
            export interface $409 {
            }
            export type $422 = /* HTTPValidationError */ Components.Schemas.HTTPValidationError;
        }
    }
}

export interface OperationMethods {
  /**
   * get_schedule_v1_schedule__primary_key__get - Get Schedule
   * 
   * Get Schedule.
   */
  'get_schedule_v1_schedule__primary_key__get'(
    parameters?: Parameters<Paths.GetScheduleV1SchedulePrimaryKeyGet.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.GetScheduleV1SchedulePrimaryKeyGet.Responses.$200>
  /**
   * update_schedule_v1_schedule__primary_key__put - Update Schedule
   * 
   * Update Schedule.
   */
  'update_schedule_v1_schedule__primary_key__put'(
    parameters?: Parameters<Paths.UpdateScheduleV1SchedulePrimaryKeyPut.PathParameters> | null,
    data?: Paths.UpdateScheduleV1SchedulePrimaryKeyPut.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.UpdateScheduleV1SchedulePrimaryKeyPut.Responses.$200>
  /**
   * delete_schedule_v1_schedule__primary_key__delete - Delete Schedule
   * 
   * Delete Schedule.
   */
  'delete_schedule_v1_schedule__primary_key__delete'(
    parameters?: Parameters<Paths.DeleteScheduleV1SchedulePrimaryKeyDelete.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.DeleteScheduleV1SchedulePrimaryKeyDelete.Responses.$200>
  /**
   * get_schedules_v1_schedule__get - Get Schedules
   * 
   * Get Schedules.
   */
  'get_schedules_v1_schedule__get'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.GetSchedulesV1ScheduleGet.Responses.$200>
  /**
   * create_schedule_v1_schedule__post - Create Schedule
   * 
   * Create Schedule.
   */
  'create_schedule_v1_schedule__post'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: Paths.CreateScheduleV1SchedulePost.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.CreateScheduleV1SchedulePost.Responses.$200>
  /**
   * get_relays_v1_relay__get - Get Relays
   * 
   * Get all relays.
   * 
   * :return:
   */
  'get_relays_v1_relay__get'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.GetRelaysV1RelayGet.Responses.$200>
  /**
   * get_relay_v1_relay__position__get - Get Relay
   * 
   * Get relay by position.
   * 
   * :param position:
   * :return:
   */
  'get_relay_v1_relay__position__get'(
    parameters?: Parameters<Paths.GetRelayV1RelayPositionGet.PathParameters> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.GetRelayV1RelayPositionGet.Responses.$200>
  /**
   * update_relay_v1_relay__position__put - Update Relay
   * 
   * Update relay by position.
   * 
   * :param position:
   * :param relay:
   * :return:
   */
  'update_relay_v1_relay__position__put'(
    parameters?: Parameters<Paths.UpdateRelayV1RelayPositionPut.PathParameters> | null,
    data?: Paths.UpdateRelayV1RelayPositionPut.RequestBody,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.UpdateRelayV1RelayPositionPut.Responses.$200>
  /**
   * get_board_info_v1_info__get - Get Board Info
   * 
   * Get Raspberry Pi board information.
   * 
   * :return:
   */
  'get_board_info_v1_info__get'(
    parameters?: Parameters<UnknownParamsObject> | null,
    data?: any,
    config?: AxiosRequestConfig  
  ): OperationResponse<Paths.GetBoardInfoV1InfoGet.Responses.$200>
}

export interface PathsDictionary {
  ['/v1/schedule/{primary_key}']: {
    /**
     * get_schedule_v1_schedule__primary_key__get - Get Schedule
     * 
     * Get Schedule.
     */
    'get'(
      parameters?: Parameters<Paths.GetScheduleV1SchedulePrimaryKeyGet.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.GetScheduleV1SchedulePrimaryKeyGet.Responses.$200>
    /**
     * update_schedule_v1_schedule__primary_key__put - Update Schedule
     * 
     * Update Schedule.
     */
    'put'(
      parameters?: Parameters<Paths.UpdateScheduleV1SchedulePrimaryKeyPut.PathParameters> | null,
      data?: Paths.UpdateScheduleV1SchedulePrimaryKeyPut.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.UpdateScheduleV1SchedulePrimaryKeyPut.Responses.$200>
    /**
     * delete_schedule_v1_schedule__primary_key__delete - Delete Schedule
     * 
     * Delete Schedule.
     */
    'delete'(
      parameters?: Parameters<Paths.DeleteScheduleV1SchedulePrimaryKeyDelete.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.DeleteScheduleV1SchedulePrimaryKeyDelete.Responses.$200>
  }
  ['/v1/schedule/']: {
    /**
     * get_schedules_v1_schedule__get - Get Schedules
     * 
     * Get Schedules.
     */
    'get'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.GetSchedulesV1ScheduleGet.Responses.$200>
    /**
     * create_schedule_v1_schedule__post - Create Schedule
     * 
     * Create Schedule.
     */
    'post'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: Paths.CreateScheduleV1SchedulePost.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.CreateScheduleV1SchedulePost.Responses.$200>
  }
  ['/v1/relay/']: {
    /**
     * get_relays_v1_relay__get - Get Relays
     * 
     * Get all relays.
     * 
     * :return:
     */
    'get'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.GetRelaysV1RelayGet.Responses.$200>
  }
  ['/v1/relay/{position}']: {
    /**
     * get_relay_v1_relay__position__get - Get Relay
     * 
     * Get relay by position.
     * 
     * :param position:
     * :return:
     */
    'get'(
      parameters?: Parameters<Paths.GetRelayV1RelayPositionGet.PathParameters> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.GetRelayV1RelayPositionGet.Responses.$200>
    /**
     * update_relay_v1_relay__position__put - Update Relay
     * 
     * Update relay by position.
     * 
     * :param position:
     * :param relay:
     * :return:
     */
    'put'(
      parameters?: Parameters<Paths.UpdateRelayV1RelayPositionPut.PathParameters> | null,
      data?: Paths.UpdateRelayV1RelayPositionPut.RequestBody,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.UpdateRelayV1RelayPositionPut.Responses.$200>
  }
  ['/v1/info/']: {
    /**
     * get_board_info_v1_info__get - Get Board Info
     * 
     * Get Raspberry Pi board information.
     * 
     * :return:
     */
    'get'(
      parameters?: Parameters<UnknownParamsObject> | null,
      data?: any,
      config?: AxiosRequestConfig  
    ): OperationResponse<Paths.GetBoardInfoV1InfoGet.Responses.$200>
  }
}

export type Client = OpenAPIClient<OperationMethods, PathsDictionary>
