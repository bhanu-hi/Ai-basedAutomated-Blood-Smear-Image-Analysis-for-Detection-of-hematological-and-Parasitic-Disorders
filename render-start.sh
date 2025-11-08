#!/usr/bin/env bash
cd bloodsmearimageanalysisproject/project/backend
gunicorn --bind 0.0.0.0:$PORT app:app
