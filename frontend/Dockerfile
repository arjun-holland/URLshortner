FROM node:20-alpine as build

WORKDIR /app

# accept env variable
ARG VITE_API_URL
ENV VITE_API_URL=$VITE_API_URL

COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

COPY frontend/ ./

RUN npm run build

# production server
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
