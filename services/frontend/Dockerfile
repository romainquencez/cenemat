FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli@5.0.8 -g

COPY --chown=node:node package*.json ./
RUN npm install

COPY --chown=node:node . .
USER node

CMD ["npm", "run", "serve"]
