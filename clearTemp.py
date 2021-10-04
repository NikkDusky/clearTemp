from shutil import rmtree
from os import listdir, remove
import tempfile

tempDir = tempfile.gettempdir()

for _ in listdir(tempDir):
    try:
        rmtree(f"{tempDir}\\{_}", ignore_errors=False, onerror=None)
        print(f"Дирректория удалена {_}.")
    except:
        try:
            remove(f"{tempDir}\\{_}")
            print(f"Файл удалён {_}.")
        except PermissionError:
            pass