# Задание 4
# Имеется папка с файлами
# Реализовать удаление файлов старше N дней

import datetime
import os
import time
from pathlib import Path

n = 10

posix_n_date_ago = time.mktime(
    (datetime.date.today() - datetime.timedelta(days=n)).timetuple()
)

directory = Path(r'')
if not directory.is_dir():
    raise ValueError(f"'{directory.name}' isn't directory")

for file in directory.iterdir():
    if file.is_file() and os.path.getmtime(file) > posix_n_date_ago:
        file.unlink()
