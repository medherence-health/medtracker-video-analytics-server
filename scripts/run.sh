#!/usr/bin/env bash
uvicorn "manage:app" "--host" "0.0.0.0" "--port" "4000" --workers 4

# https://fastapi.tiangolo.com/deployment/server-workers/