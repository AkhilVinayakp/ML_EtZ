from datetime import datetime
import logging
import os




LOG_DIR = os.path.join(os.getcwd(), "logs")
file_name = f"{datetime.now().strftime('%d_%m_%Y')}.log"
file_path = os.path.join(LOG_DIR, file_name)
def setUp_logger():
    try:
        os.makedirs(LOG_DIR,exist_ok=True)
    except Exception as e:
        logging.error("Can not initiate folder path")
    logging.basicConfig(
        filename=file_path,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )

if __name__ == "__main__":
    setUp_logger()
    logging.info("logger initialized")