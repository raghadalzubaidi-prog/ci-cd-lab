#!/bin/bash

if grep -qE '^FROM .+:latest$' Dockerfile; then
  echo "Error: Do not use latest as the base image."
  exit 1
fi

echo "Dockerfile check passed."
