import { Environment } from './environment.models';

export const defaults: Environment = {
  production: false,
  api: {
    host: 'http://localhost:8000',
  },
};
