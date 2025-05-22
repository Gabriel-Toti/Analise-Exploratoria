import pandas as pd
import os.path as path

ipea_agro_file = "data/ipeadata[19-05-2025-12-08].csv"
ipea_extrat_file = "data/ipeadata[20-05-2025-01-48].csv"

def clear_file(file: str, tipo: str):
    text = ""

    with open(file) as f:
        text = f.read()
    
    new_text = ""
    fields = text.split("\n")
    for i in range(1, len(fields)):
        new_text += fields[i] + "\n"
    
    new_file = "data/ipeadata_clean_"+ tipo +".csv"
    file_mode = "x" if not path.exists(new_file) else "w"

    with open(new_file, file_mode) as f:
        f.write(new_text)
    
    return new_file
    

clear_file(ipea_extrat_file, "extrat")
clear_file(ipea_agro_file, "agro")