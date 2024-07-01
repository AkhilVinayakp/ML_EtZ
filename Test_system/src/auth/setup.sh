#!/bin/bash
echo "Setting up"

export MONGO_URL="mongodb://Alioth.local"
export COLLECTION_NAME="dev-user-data"
export DATABASE='dev-db'
export JWT_SECRET='this_is_my_key'

echo "added details"
echo $MONGO_URL
echo $COLLECTION_NAME
echo $DATABASE


echo "exported mongo details"