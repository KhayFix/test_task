# encode:utf-8
from datetime import datetime
import logging
import os
import re
import sys
from collections import Counter

logging.basicConfig(
    filename=f"{os.getcwd()}/logs/{datetime.now().strftime('%Y-%m-%d_%H_%M_%S')}.log",
    level=logging.INFO,
    filemode='w',
    format='%(levelname)s %(asctime)s : %(message)s',
)

if __name__ == "__main__":
    pass
