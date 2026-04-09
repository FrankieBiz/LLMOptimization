@echo off
REM ============================================================
REM  Ollama Environment Variables — Workout App Dev Setup
REM  Run this once as Administrator, then restart Ollama service
REM ============================================================

echo Setting Ollama environment variables...

REM Force full GPU offload (all layers on GPU)
setx /M OLLAMA_NUM_GPU 999

REM Reserve 512MB VRAM for OS/display (in bytes)
setx /M OLLAMA_GPU_OVERHEAD 536870912

REM Enable flash attention for faster inference
setx /M OLLAMA_FLASH_ATTENTION 1

REM Only keep 1 model loaded at a time (avoid VRAM fights)
setx /M OLLAMA_MAX_LOADED_MODELS 1

REM Unload model after 30 minutes idle to free VRAM
setx /M OLLAMA_KEEP_ALIVE 30m

echo.
echo Done! Environment variables set system-wide.
echo.
echo Next steps:
echo   1. Open Services (services.msc)
echo   2. Find "Ollama" service
echo   3. Right-click → Restart
echo.
echo Or run: net stop ollama ^&^& net start ollama
echo.
pause
