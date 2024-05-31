import { Components } from 'frontend/@types/openapi';

export type RaspberryPiBoardInfo = Components.Schemas.RaspberryPiBoardInfo;

export const BoardInfoDisplayMapping: Record<string, string> = {
  revision: 'Raspberry Pi revision',
  model: 'Raspberry Pi model',
  pcb_revision: 'Printed Circuit Board (PCB) revision',
  released: 'Release date',
  soc: 'System On a Chip (SoC)',
  manufacturer: 'Manufacturer',
  memory: 'Memory (SDRAM)',
  storage: 'Storage type',
  usb: 'Number of USB ports',
  usb3: 'Number of USB3 ports',
  ethernet: 'Number of ethernet ports',
  eth_speed: 'Ethernet speed',
  wifi: 'Wifi available',
  bluetooth: 'Bluetooth available',
  csi: 'Number of Camera Serial Interfaces (CSI)',
  dsi: 'Number of Display Serial Interfaces (DSI)',
};
