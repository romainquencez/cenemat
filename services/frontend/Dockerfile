FROM node:lts-alpine

WORKDIR /app

COPY . .

RUN npm i && \
    npm i -g @quasar/cli

EXPOSE 9000

CMD ["quasar", "dev", "-m", "pwa", "-p", "9000"]
