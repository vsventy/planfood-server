#!/bin/sh

# Sort imports
isort -rc ./planfood

# Format style:
black -S --exclude migrations .
