FROM node:20-alpine AS build

WORKDIR /app

# pass environment variable during build
ARG VITE_API_URL
ENV VITE_API_URL=$VITE_API_URL

# install dependencies
COPY package.json package-lock.json ./
RUN npm install

# copy source code
COPY . .

# build the react app
RUN npm run build


# production image
FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
