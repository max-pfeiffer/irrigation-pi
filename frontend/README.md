# Irrigation Pi Frontend

## Installation

Install Nodejs using [nvm](https://github.com/nvm-sh/nvm#installing-and-updating).

Install version 20 using nvm

```shell
nvm install --lts=iron
```

Activate Nodejs v20

```zsh
nvm use lts/iron
npm install -g npm@latest @ionic/cli@latest @angular/cli@latest
```

## Start fronted development server

```zsh
nvm use lts/iron
cd frontend && ionic serve
```


## Build production static files

```zsh
nvm use lts/iron
cd frontend && ionic build
```
