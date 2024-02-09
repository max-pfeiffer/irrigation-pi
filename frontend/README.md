# Irrigation Pi Frontend

## Environment setup

Install Nodejs using [nvm](https://github.com/nvm-sh/nvm#installing-and-updating).

### Install version 20 using nvm

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

## Openapi

### Generating type definitions

```zsh
manage run backend
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
