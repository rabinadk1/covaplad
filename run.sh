#! /usr/bin/sh

export FLASK_APP=covaplad
export FLASK_ENV=development

## Used to optimized python. NOTE: This disables assert statements
export PYTHONOPTIMIZE=2
flask run