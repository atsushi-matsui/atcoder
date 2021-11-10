import csv

def read_csv(file_name):
    """
    ファイル読み込み
    Parameters
    ----------
    file_name:str
        ファイル名（絶対パスで記述）
    
    Returns
    -------
    file:dict
        ファイルの情報
    """
    csv_file = open(file_name, "r", encoding="utf-8", errors="", newline="" )
    file = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    
    return file
