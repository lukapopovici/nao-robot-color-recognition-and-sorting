#!/bin/bash

#LINUX VERSION

#use this to kill the robot after closing the server

PID=$(lsof -t -i:8080)

if [ -z "$PID" ]; then
  echo "Beep boop. No process detected on port 8080."
  exit 0
fi

echo "Beep boop. Scanning... Process found on port 8080:"
lsof -i:8080

read -p "Do you wish for me to terminate this process? (yes/no): " CONFIRM

if [[ "$CONFIRM" =~ ^[Yy][Ee][Ss]$ || "$CONFIRM" =~ ^[Yy]$ ]]; then
  kill -9 $PID
  echo "Beep boop. Process $PID has been eliminated. Mission complete."
else
  echo "Beep boop. Process $PID remains operational. No action taken."
fi
