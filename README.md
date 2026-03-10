# URL Shortner - Scalable URL Shortener

A beautiful, scalable URL shortener web application with a high-performance backend. Built with Django, Django REST Framework, React, MongoDB Atlas, and Upstash Redis.

## Architecture

- **Frontend**: React (Vite) styled with premium Vanilla CSS.
- **Backend API**: Django + DRF
- **Database**: MongoDB Atlas (Primary Data Store)
- **Cache**: Upstash Redis (For blazing fast url redirection)
- **Deployment**: Docker & Docker Compose

## Features

- **URL Shortening**: Generates a reliable, short alphanumeric code for long URLs.
- **Lightning Fast Redirection**: Uses Redis cache to bypass database latency for hit URLs.
- **Analytics Tracking**: Logs user agent, timestamp, and click count for every lookup.
- **Premium UI**: Smooth animations, glow effects, and a modern dark aesthetic.

## Setup Instructions

### Prerequisites
- Docker and Docker Compose installed.
- A MongoDB Atlas connection string.
- An Upstash Redis connection URL.

### Local Development Setup

1. Rename the existing `backend/.env` file or create a new `.env` file at the root or `backend` folder containing:

```env
MONGO_URI="your-mongodb-atlas-uri-here"
REDIS_URL="your-upstash-redis-url-here"
```

2. Run the deployment using Docker Compose:

```bash
docker-compose up --build
```

3. Access your fully running application!
- **Frontend App**: [http://localhost](http://localhost)
- **Backend API**: [http://localhost:8000](http://localhost:8000)

## API Endpoints

- `POST /api/shorten`
  - Body: `{ "long_url": "https://..." }`
  - Response: `{ "short_url": "/code", "short_code": "code" }`

- `GET /<short_code>/`
  - Action: Automatically redirects to `long_url` while updating click analytics.

- `GET /api/analytics/<short_code>`
  - Action: Fetches the analytics statistics for the generated code.

## OUTPUT
<img width="1919" height="1077" alt="image" src="https://github.com/user-attachments/assets/ab4b9c2a-3d42-4a39-a9c7-27429e62b0bc" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/63719053-8f45-46c2-8f32-5c9ab0af3858" />
<img width="1919" height="1077" alt="image" src="https://github.com/user-attachments/assets/5f4fa6b3-9e85-433f-a206-bbbe0cdd9723" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/fb586c36-3ab4-44eb-99a0-052b24559a7c" />
<img width="1919" height="1069" alt="image" src="https://github.com/user-attachments/assets/62e278c9-2ffe-4457-a2ea-6a72c506b239" />
