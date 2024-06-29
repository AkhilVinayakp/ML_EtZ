#!/bin/bash
echo "Setting up"

export MONGO_URL="mongodb://localhost:27017"
export COLLECTION_NAME = "dev-user-data"
export DATABASE = 'dev-db'

echo "exported mongo details"