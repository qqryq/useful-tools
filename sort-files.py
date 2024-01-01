import os
import shutil
from datetime import datetime

def move_files(source_folder, destination_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            modification_time = os.path.getmtime(file_path)
            modification_date = datetime.fromtimestamp(modification_time)
            
            # Tworzenie nazwy folderu na podstawie daty modyfikacji
            folder_name = modification_date.strftime("%Y-%m")
            destination_path = os.path.join(destination_folder, folder_name)
            
            # Tworzenie folderu, jeśli nie istnieje
            os.makedirs(destination_path, exist_ok=True)
            
            # Przenoszenie pliku do odpowiedniego folderu
            shutil.move(file_path, os.path.join(destination_path, file))

if __name__ == "__main__":
    source_folder = "/sciezka/do/zrodlowego/folderu"
    destination_folder = "/sciezka/do/docelowego/folderu"
    
    move_files(source_folder, destination_folder)
