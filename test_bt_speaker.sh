#!/bin/bash


SINK_ID=69

echo "🔍 Checking for Bluetooth sink ID '$SINK_ID'..."


if wpctl inspect $SINK_ID > /dev/null 2>&1; then
    echo "✅ Sink $SINK_ID found. Playing test sound..."
    paplay /usr/share/sounds/alsa/Front_Center.wav
else
    echo "❌ No Bluetooth sink with ID '$SINK_ID' found."
    echo "🔁 Try reconnecting your speaker and run this again."
fi
