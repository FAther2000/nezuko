#!/bin/bash

echo "🔍 Searching for Bluetooth audio sinks..."

# Find Bluetooth audio sink (usually has 'bluez' in its name)
SINK=$(wpctl status | grep -A 10 "Audio" | grep bluez | awk '{print $2}' | tr -d '.')

if [ -z "$SINK" ]; then
  echo "❌ No Bluetooth audio sink found. Make sure your speaker is connected!"
  exit 1
fi

echo "🔊 Found Bluetooth audio sink ID: $SINK"
echo "🎚️ Setting it as the default output..."

# Set as default output
wpctl set-default "$SINK"

echo "✅ Bluetooth speaker set as default audio output."

# Play test sound
echo "📢 Playing test sound..."
aplay /usr/share/sounds/alsa/Front_Center.wav

