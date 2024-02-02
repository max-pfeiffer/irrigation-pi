# Irrigation Pi Frontend

## Installation

Install Nodejs using [nvm](https://github.com/nvm-sh/nvm#installing-and-updating).

### Install version 20 using nvm

```shell
nvm install --lts=iron
```

### Activate Nodejs v20 and install global packages

```zsh
nvm use lts/iron
npm install -g npm@latest @ionic/cli@latest @angular/cli@latest
```

### Install frontend dependencies

```zsh
cd frontend && npm clean-install
```

## Start fronted development server

```zsh
nvm use lts/iron
cd frontend && ionic serve
```


## Build production frontend application

```zsh
nvm use lts/iron
cd frontend && ionic build
```
The frontend application is compiled to static HTML and JavaScript files into the `fronted/www` directory. It can be served using a web server.
