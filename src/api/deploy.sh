#!/bin/bash

# spin containers down
docker compose -f docker-compose.yml down

# spin containers up
docker compose -f docker-compose.yml up -d --build