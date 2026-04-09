@echo off
REM ============================================================
REM  Pull Ollama Models — Workout App Dev Setup
REM  Run AFTER setting environment variables and restarting Ollama
REM  Expected total download: ~15GB  |  Time: 10-30 min depending on connection
REM ============================================================

echo.
echo Pulling PRIMARY model: gemma4:e4b
echo Expected VRAM: ~5-6 GB  (leaves 2GB for KV cache)
echo.
ollama pull gemma4:e4b

echo.
echo Pulling SECONDARY model: qwen3.5:9b-q4_K_M
echo Expected VRAM: ~6.9 GB  (best for extended context, 32K @ 54-58 tok/s)
echo.
ollama pull qwen3.5:9b-q4_K_M

echo.
echo Pulling LIGHTWEIGHT fallback: gemma4:e2b
echo Expected VRAM: ~3-4 GB  (use when multitasking or running the app simultaneously)
echo.
ollama pull gemma4:e2b

echo.
echo Creating custom coding model (gemma4-coder)...
ollama create gemma4-coder -f "C:\Users\frank.DESKTOP-8VOID7R\.ollama\Modelfiles\gemma4-coder"

echo.
echo ============================================================
echo  All models pulled and gemma4-coder created!
echo.
echo  Test with:
echo    ollama run gemma4:e4b "Write a TypeScript interface for a WorkoutSession"
echo    ollama ps
echo    nvidia-smi
echo ============================================================
pause
