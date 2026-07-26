# IPL Analytics System

A complete end-to-end Flask project demonstrating REST API development and API consumption using historical IPL match data.

---

## Project Overview

This project consists of two applications:

### 1. REST API Server

Built using Flask and Pandas.

Provides IPL statistics through REST endpoints.

Examples:

- Get all teams
- Team vs Team statistics
- Overall team records
- Season-wise points table

---

### 2. Client Web Application

Built using Flask.

Consumes the REST API using the Requests library and displays results in a web interface.

---

## Tech Stack

- Python
- Flask
- Pandas
- NumPy
- Requests
- HTML
- Jinja2

---

## Project Architecture

User

↓

Flask Client Application

↓

HTTP Requests

↓

Flask REST API

↓

Pandas

↓

IPL Dataset (CSV)

---

## Features

### REST API

- List all IPL teams
- Head-to-head statistics
- Team winning percentage
- Home vs Away record
- Season points table

### Client Application

- Select two teams
- Fetch statistics from API
- Display results dynamically
- Simple web interface

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /api/teams | Get all teams |
| GET | /api/teamvteam | Team vs Team statistics |
| GET | /api/AllTeamsRecord | Overall team records |
| GET | /api/SeasonRecord | Season points table |

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/IPL-Analytics-System.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the API

```bash
cd api

python app.py
```

Runs on

```
http://127.0.0.1:5000
```

---

## Running the Client

Open another terminal

```bash
cd client

python app.py
```

Runs on

```
http://127.0.0.1:7000
```

---

## Future Improvements

- Docker support
- Swagger/OpenAPI documentation
- Database integration (MySQL/PostgreSQL)
- Authentication
- Deploy on Render
- Interactive charts

---

## Learning Outcomes

- REST API Development
- API Consumption
- Flask Routing
- HTTP Requests
- Data Processing using Pandas
- Backend Architecture
