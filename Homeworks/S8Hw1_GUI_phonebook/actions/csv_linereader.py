from pathlib import Path

def csv_linereader(path: str, filename: str) -> list:
    filepath = Path(path, filename)
    with open (filepath, 'r') as file:
        return file.readlines()
        
    