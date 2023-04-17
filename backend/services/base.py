import os
import shutil
from fastapi import HTTPException


class BaseService():
    def cleanMediaFolder(self):
        folder = os.path.abspath("media")
        for filename in os.listdir(folder):
            if filename == ".gitignore":
                continue
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                raise HTTPException(
                    400, detail='Failed to delete %s. Reason: %s'
                    % (file_path, e))
