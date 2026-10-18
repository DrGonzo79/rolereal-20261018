FROM node:22-alpine AS web
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
FROM nginx:1.27-alpine
COPY --from=web /app/out /usr/share/nginx/html/rolereal-20261018
EXPOSE 80
