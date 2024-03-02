import { defaults } from './defaults';
import { Environment } from './environment.models';

export const environment: Environment = {
  ...defaults,
  production: true,
  appConfigUrl: '/assets/config/appConfig.prod.json',
};
