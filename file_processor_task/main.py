import os
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run(**kwargs) -> bool:
    """
    Creates a file and writes content into it.

    Expected kwargs:
        file_name (str)  -> Required
        content (str)    -> Optional
        directory (str)  -> Optional (default: /tmp)
    """

    file_name = kwargs.get("file_name")
    content = kwargs.get("content", "Default content from file_processor_task")
    directory = kwargs.get("directory", "/tmp")

    if not file_name:
        logging.error("file_name is required")
        return False

    try:
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, file_name)

        with open(file_path, "w") as f:
            f.write(f"{content}\n")
            f.write(f"Generated at: {datetime.utcnow()}\n")

        logging.info(f"File successfully created at {file_path}")
        return True

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return False
