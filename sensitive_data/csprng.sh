#!/bin/bash

SECRET_KEY_FILE="sensitive_data/$1"

if test -f "$SECRET_KEY_FILE"; then
  echo "$SECRET_KEY_FILE already exists. Manage deletion manually."
fi

touch ./$SECRET_KEY_FILE

chmod 700 $SECRET_KEY_FILE

python sensitive_data/csprng.py > $SECRET_KEY_FILE
