FROM node:latest AS build

WORKDIR /client
COPY . .
RUN npm install

CMD ["npm", "run", "start"]
EXPOSE 3000