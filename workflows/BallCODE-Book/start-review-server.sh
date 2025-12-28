#!/bin/bash
# Start localhost server to review Unity UI/UX guide

PORT=8000
DIR="/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book"

echo "🌐 Starting localhost server on port $PORT..."
echo ""

cd "$DIR"

# Check if port is already in use
if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null ; then
    echo "⚠️  Port $PORT is already in use"
    echo "   Using existing server or choose different port"
else
    python3 -m http.server $PORT > /dev/null 2>&1 &
    SERVER_PID=$!
    echo "✅ Server started (PID: $SERVER_PID)"
    echo ""
fi

echo "📋 Access the guide:"
echo "   http://localhost:$PORT/UNITY-LANDING-PAGE-UI-IMPROVEMENT-GUIDE.md"
echo ""
echo "📄 Other files:"
echo "   http://localhost:$PORT/Unity-Scripts/ImprovedButton.cs"
echo "   http://localhost:$PORT/REVIEW-GUIDE-LOCALHOST.md"
echo ""
echo "🎮 Unity Game Review:"
echo "   1. Open Unity Editor"
echo "   2. Load landing page scene"
echo "   3. Click Play to see current UI"
echo "   4. Note bottom-left button issues"
echo "   5. Compare with guide recommendations"
echo ""
echo "💡 To stop server:"
echo "   pkill -f 'python3 -m http.server $PORT'"
echo "   or: kill $SERVER_PID"


