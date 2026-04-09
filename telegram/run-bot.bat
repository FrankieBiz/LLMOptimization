@echo off
REM ============================================================
REM  Run Telegram Bot
REM  Prerequisites:
REM    pip install python-telegram-bot ollama python-dotenv
REM  Copy .env.example to .env and fill in your values first!
REM ============================================================

cd /d "%~dp0"

if not exist ".env" (
    echo ERROR: .env file not found!
    echo Copy .env.example to .env and fill in your values.
    pause
    exit /b 1
)

echo Starting Telegram bot...
echo Press Ctrl+C to stop.
echo.
python telegram_bot.py
pause
