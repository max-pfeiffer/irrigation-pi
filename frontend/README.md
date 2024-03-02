# Irrigation Pi Frontend

## Environment setup

Install Nodejs using [nvm](https://github.com/nvm-sh/nvm#installing-and-updating).

### Install Nodejs version 20 using nvm

```shell
nvm install --lts=iron
```

### Activate Nodejs v20 and install global packages

```zsh
nvm use lts/iron
npm install -g npm@latest @ionic/cli@latest @angular/cli@latest openapicmd@latest
```

## Development setup

### Install frontend dependencies

```zsh
cd frontend && npm clean-install
```

### Start fronted development server

```zsh
nvm use lts/iron
cd frontend && ionic serve
```

### Development server configurations

The `ionic serve` command takes the same configuration arguments like the `ionic build` command. The configurations differ in which backend URL is used by the frontend. See also [Build configurations](#build-configurations)

```zsh
ionic serve --configuration=development # default
ionic serve --configuration=production
```

## Openapi

### Generating type definitions

```zsh
irrigation-pi run backend
openapi typegen http://localhost:8000/openapi.json > frontend/@types/openapi.d.ts
```

## Deployment

### Build production frontend application

```zsh
nvm use lts/iron
cd frontend && ionic build
```
The frontend application is compiled to static HTML and JavaScript files into the `fronted/www/browser` directory. It can be served using a web server.

### Testing production build locally

The production build can be served locally to test wether it compiled successfully.

```zsh
npx http-server --port=8100 --proxy http://localhost:8100\?  www/browser
```

### Build configurations

The frontend build has 2 configurations:

- production (default)
    - Uses http://raspberrypi.local/api as backend URL
- development
    - Uses http://localhost:8000/api as backend URL

#### Production

The production build configuration is the default. Hence the two commands are equivalent:

```zsh
ionic build --configuration=production
ionic build # equivalent to above
```

#### Development

Development builds can be made using the following command:

```zsh
ionic build --configuration=development
```
