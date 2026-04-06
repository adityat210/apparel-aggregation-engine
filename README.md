# Apparel Aggregation & Discovery Engine
A full-stack apparel search application that aggregates product listings from multiple retailers into a unified browsing. The project combines a Next.js frontend, FastAPI backend, PostgreSQL-backed data storage, and a small ingestion pipeline that normalizes retailer-specific product data into a shared schema

## Features 
- Aggregates apparel products from multiple retailer-specific data sources 
- Normalizes inconsistent source fields into unified product model
- Products through FastAPI REST API
- Supports configurable filters:
    - retailer
    - category
    - min price, max price
    - in-stock options
- Supports sorting by: price ascending, descending, rating descending
- Displays products in a simple Next.js frontend
- Uses PostgreSQL with Docker Compose for containerized locality
- Includes backend tests for normalization, ingestion refresh and API routes
- Runs backend tests automatically with GitHub Actions CI

## Tech Stack 
### Frontend
- Next.js
- TypeScript
- React

### Backend
- FastAPI
- SQLAlchemy
- Pydantic

### Testing/CI
- pytest
- GitHub Actions