#!/bin/bash
# Script to set n8n variables on Raspberry Pi with password

PI_HOST="pi@192.168.1.226"
SCRIPT_FILE="robot-set-n8n-env-vars.py"

echo "🔧 Setting n8n Environment Variables on Raspberry Pi"
echo ""
echo "This will:"
echo "  1. Copy the Python script to the Pi"
echo "  2. Run it on the Pi to set variables"
echo "  3. Restart n8n on the Pi"
echo ""
echo "You'll be prompted for the SSH password."
echo ""

# Copy script to Pi
echo "📤 Copying script to Raspberry Pi..."
scp "${SCRIPT_FILE}" "${PI_HOST}:~/"

if [ $? -ne 0 ]; then
  echo "❌ Failed to copy script. Please check:"
  echo "  1. Raspberry Pi is accessible"
  echo "  2. SSH password is correct"
  exit 1
fi

echo "✅ Script copied"
echo ""

# Run script on Pi
echo "🚀 Running script on Raspberry Pi..."
ssh "${PI_HOST}" "python3 ~/${SCRIPT_FILE}"

if [ $? -eq 0 ]; then
  echo ""
  echo "✅ Variables set successfully!"
  echo ""
  echo "🔄 Restarting n8n on Raspberry Pi..."
  ssh "${PI_HOST}" "sudo systemctl restart n8n"
  
  if [ $? -eq 0 ]; then
    echo "✅ n8n restarted"
  else
    echo "⚠️  Could not restart n8n automatically"
    echo "   Please SSH and run: sudo systemctl restart n8n"
  fi
else
  echo "❌ Failed to set variables"
  exit 1
fi

echo ""
echo "✅ Complete! Variables are set and n8n is restarting."
echo "   Test at: http://192.168.1.226:5678"
