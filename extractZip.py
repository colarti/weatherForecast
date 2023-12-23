import zipfile
import glob, os
from pathlib import Path


def extractAll():
    data = glob.glob('*zip')

    for x in data:
        fn = Path(x).stem
        if not os.path.exists(fn):
            with zipfile.ZipFile(x, 'r') as zip:
                zip.extractall(f'{fn}\\')
        else:
            print(f'No Action, {fn} already exists')


if __name__ == '__main__':
    extractAll()