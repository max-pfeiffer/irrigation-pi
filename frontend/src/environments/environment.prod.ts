import { defaults } from './defaults';
import { Environment } from './environment.models';

export const environment: Environment = {
  ...defaults,
  production: true,
  api: {
    ...defaults.api,
    host: 'http://raspberrypi.local:8000',
  },
};
