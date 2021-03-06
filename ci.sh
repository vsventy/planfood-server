#!/bin/sh

set -o errexit
set -o nounset

pyclean () {
  # Clean cache:
  find . | grep -E '(__pycache__|\.py[cod]$)' | xargs rm -rf
}

run_ci () {
  # Compile message files
  django-admin compilemessages

  # Run tests:
  mypy planfood
  py.test

  # Check style:
  black -S --exclude migrations --check .

  # Check that all migrations worked fine:
  python manage.py makemigrations --dry-run --check
}

# Remove any cache before the script:
pyclean

# Clean everything up:
trap pyclean EXIT INT TERM

# Run the CI process:
run_ci
