#!/bin/bash

curl -X POST http://localhost:8000/readings/ \
  -H "Content-Type: application/json" \
  -H "X-API-Key: my-secret-key" \
  -d '[
    {
      "device_id": 1,
      "metric": "temperatura",
      "value": 25.4,
      "timestamp": "2025-09-14T15:30:00"
    },
    {
      "device_id": 1,
      "metric": "temperatura",
      "value": 25.2,
      "timestamp": "2025-09-14T15:31:00"
    },
    {
      "device_id": 1,
      "metric": "temperatura",
      "value": 25.4,
      "timestamp": "2025-09-14T15:32:00"
    },
    {
      "device_id": 1,
      "metric": "temperatura",
      "value": 26.1,
      "timestamp": "2025-09-14T15:33:00"
    },
    {
      "device_id": 1,
      "metric": "temperatura",
      "value": 25.4,
      "timestamp": "2025-09-14T15:34:00"
    },
    {
      "device_id": 1,
      "metric": "temperatura",
      "value": 26.1,
      "timestamp": "2025-09-14T15:45:00"
    }
  ]'
