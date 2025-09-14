#!/bin/bash

if [ -n "$1" ]; then
  echo "Criando dispositivo."
else
  echo "Você deve passar a informação do dispositivo."
  exit 1
fi

source .env

curl -X POST http://localhost:8000/devices/ \
  -H "Content-Type: application/json" \
  -H "X-API-Key: ${API_KEY}" \
  -d "{\"name\": \"$1\"}"
