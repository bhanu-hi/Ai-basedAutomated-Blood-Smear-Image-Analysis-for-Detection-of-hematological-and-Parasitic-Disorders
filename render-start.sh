#!/usr/bin/env bash
cd bloodsmearimageanalysisproject/project/backend && gunicorn --bind 0.0.0.0:$PORT --workers 1 --timeout 120 app:app
