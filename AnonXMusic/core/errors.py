import traceback
import logging

log = logging.getLogger(__name__)

def capture_err(func):
    """
    Decorator to catch exceptions in async functions
    and log them without crashing the bot.
    """
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            log.error(f"Error in {func.__name__}: {e}")
            traceback.print_exc()
    return wrapper
