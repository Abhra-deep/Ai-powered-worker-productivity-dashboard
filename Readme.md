# AI-Powered Worker Productivity Dashboard

## Architecture
Edge CCTV → AI CV Model → Event JSON → FastAPI Backend → SQLite → React Dashboard

## Event Handling
- Duplicate events: ignored via timestamp + worker + station
- Out-of-order events: sorted by timestamp
- Intermittent connectivity: events are append-only

## Metrics
- Active time = count of "working" events
- Idle time = count of "idle" events
- Units produced = sum(product_count)
- Utilization = active / (active + idle)

## Scaling
- SQLite → Postgres
- Single site → multi-site via tenant_id
- Kafka for event ingestion

## Model Lifecycle
- Model version stored per event
- Drift detected via confidence decay
- Retraining triggered by threshold alerts

## Run Locally
```bash
docker-compose up --build
