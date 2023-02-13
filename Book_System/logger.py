from datetime import datetime
import os
import logging
#log_file_name
LOG_FILE_NAME=f"{datetime.now().strftime('%m%d%y_%H%M%S')}.log"

 #log_directory
LOG_FILE_DIR=os.path.join(os.getcwd(),"logs")

os.makedirs(LOG_FILE_DIR,exist_ok=True)
logging.basicConfig(
    filename=LOG_FILE_NAME,format="[%(asctime)s]%(lineno)d%(name)s-%(levelname)s-%(message)s",
    level=logging.INFO,
)

