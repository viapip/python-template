import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.core.config import Config
from src.utils.logger import setup_logger

logger = setup_logger("main")


def main():
    try:
        config = Config("config/config.yaml")

        logger.info("Script started")

    except Exception as e:
        logger.error(f"Error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
