FROM node:20-alpine as build-stage

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN cp .env.production .env

RUN npm run build

FROM nginx:stable-alpine as production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html

COPY --from=build-stage /app/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"] 