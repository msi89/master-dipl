FROM node:18.12.1 AS build 
ARG API_URL
# ARG NODE_ENV

# ENV NODE_ENV=$NODE_ENV
ENV VITE_APP_API_URL=$API_URL


WORKDIR /app

COPY ./package.json  .

RUN npm install
COPY . .
RUN npm run build

FROM nginx:1.22.1-alpine as production

COPY --from=build /app/dist /usr/share/nginx/html
COPY --from=build /app/nginx/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

ENTRYPOINT [ "nginx", "-g", "daemon off;" ]



