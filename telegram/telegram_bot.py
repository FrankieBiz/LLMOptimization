"""
Telegram Bot — Local Gemma 4 Dev Assistant
==========================================
Connects your Telegram to the local Ollama LLM running on your PC.

Setup:
  1. pip install python-telegram-bot ollama python-dotenv --break-system-packages
  2. Copy .env.example to .env and fill in your values
  3. python telegram_bot.py

Security:
  - Only your Telegram user ID can interact with this bot
  - Ollama only listens on localhost — never exposed to internet
  - Add your user ID to ALLOWED_USER_IDS in .env
"""

import asyncio
import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
import ollama

# ── Config ──────────────────────────────────────────────────────────────────

load_dotenv()

TELEGRAM_TOKEN: str = os.environ["TELEGRAM_BOT_TOKEN"]
MODEL: str = os.getenv("OLLAMA_MODEL", "gemma4:e4b")
OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# Restrict access to your Telegram user ID only
# Find your ID by messaging @userinfobot on Telegram
ALLOWED_USER_IDS: set[int] = {
    int(uid) for uid in os.getenv("TELEGRAM_ALLOWED_USER_ID", "").split(",") if uid.strip()
}

SYSTEM_PROMPT = (
    "You are a dev assistant for a workout tracking and scheduling mobile app. "
    "The app uses TypeScript (strict mode), React Native, WatermelonDB for offline-first "
    "local storage, and follows offline-first architecture (local writes before network). "
    "Give concise, actionable answers. For code, use TypeScript. "
    "Keep responses under 300 words unless the user explicitly asks for more detail."
)

# Per-chat conversation history (in-memory; resets when bot restarts)
conversation_history: dict[int, list[dict]] = {}
MAX_HISTORY = 10  # Keep last N exchanges to maintain context without overloading

# ── Logging ──────────────────────────────────────────────────────────────────

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ── Auth Guard ───────────────────────────────────────────────────────────────

def is_authorized(user_id: int) -> bool:
    if not ALLOWED_USER_IDS:
        logger.warning("No TELEGRAM_ALLOWED_USER_ID set — rejecting all users for safety")
        return False
    return user_id in ALLOWED_USER_IDS

# ── Handlers ─────────────────────────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command."""
    user = update.effective_user
    if not is_authorized(user.id):
        await update.message.reply_text("Unauthorized.")
        return

    await update.message.reply_text(
        f"Hey! Your local {MODEL} is ready.\n\n"
        "Ask me anything about the workout app — code, architecture, debugging, planning.\n\n"
        "Commands:\n"
        "/clear — Reset conversation history\n"
        "/model — Show current model\n"
        "/ping — Check if Ollama is responding"
    )


async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /clear command — reset conversation history."""
    if not is_authorized(update.effective_user.id):
        return
    chat_id = update.effective_chat.id
    conversation_history.pop(chat_id, None)
    await update.message.reply_text("Conversation history cleared.")


async def model_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /model command."""
    if not is_authorized(update.effective_user.id):
        return
    await update.message.reply_text(f"Current model: `{MODEL}`\nOllama URL: `{OLLAMA_BASE_URL}`")


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /ping — verify Ollama is responding."""
    if not is_authorized(update.effective_user.id):
        return
    try:
        client = ollama.Client(host=OLLAMA_BASE_URL)
        models = client.list()
        model_names = [m["name"] for m in models.get("models", [])]
        await update.message.reply_text(
            f"Ollama is running.\nLoaded models: {', '.join(model_names) or 'none'}"
        )
    except Exception as e:
        await update.message.reply_text(f"Ollama not responding: {e}")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming text messages — send to Ollama and reply."""
    user = update.effective_user
    if not is_authorized(user.id):
        logger.warning(f"Unauthorized access attempt from user {user.id} (@{user.username})")
        await update.message.reply_text("Unauthorized.")
        return

    chat_id = update.effective_chat.id
    user_message = update.message.text

    # Initialize history for this chat if needed
    if chat_id not in conversation_history:
        conversation_history[chat_id] = []

    # Add user message to history
    conversation_history[chat_id].append({
        "role": "user",
        "content": user_message,
    })

    # Trim history to avoid context overflow
    if len(conversation_history[chat_id]) > MAX_HISTORY * 2:
        conversation_history[chat_id] = conversation_history[chat_id][-MAX_HISTORY * 2:]

    # Build message list with system prompt
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + conversation_history[chat_id]

    # Show typing indicator
    await context.bot.send_chat_action(chat_id=chat_id, action="typing")

    try:
        client = ollama.Client(host=OLLAMA_BASE_URL)
        response = client.chat(model=MODEL, messages=messages)
        assistant_reply = response["message"]["content"]

        # Store assistant reply in history
        conversation_history[chat_id].append({
            "role": "assistant",
            "content": assistant_reply,
        })

        await update.message.reply_text(assistant_reply)

    except Exception as e:
        logger.error(f"Ollama error: {e}")
        await update.message.reply_text(
            f"Error reaching Ollama: {e}\n\nMake sure Ollama is running:\n`ollama serve`"
        )


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN not set in environment / .env file")

    if not ALLOWED_USER_IDS:
        raise ValueError(
            "TELEGRAM_ALLOWED_USER_ID not set. "
            "Find your ID by messaging @userinfobot on Telegram."
        )

    logger.info(f"Starting bot | Model: {MODEL} | Allowed users: {ALLOWED_USER_IDS}")

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(CommandHandler("model", model_info))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Bot is polling for messages...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
