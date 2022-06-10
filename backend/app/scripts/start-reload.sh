#!/usr/bin/bash

uvicorn \
    --reload \
    --host="0.0.0.0" \
    --port=8000 \
    --log-level info \
    app.main:app
