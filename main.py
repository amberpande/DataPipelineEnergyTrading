from src.workflows import workflow1, workflow2
from src.db import create_db_session
from src.utils import setup_logging

import logging


# Set up logging
logger = logging.getLogger(__name__)
setup_logging()


# Define main function
def main():
    # Create database session
    db_session = create_db_session()

    # Run workflows
    try:
        workflow1.run(db_session)
    except Exception as e:
        logger.error(f"Workflow 1 failed: {str(e)}")

    try:
        workflow2.run(db_session)
    except Exception as e:
        logger.error(f"Workflow 2 failed: {str(e)}")

    # Close database session
    db_session.close()


if __name__ == "__main__":
    main()
