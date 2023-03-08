#!/usr/bin/env bash
uvicorn "manage:app" "--host" "0.0.0.0" "--port" "8000"