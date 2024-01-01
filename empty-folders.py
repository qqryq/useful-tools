import os

def get_folder_stats(folder):
    total_size = 0
    total_files = 0
    total_folders = 0

    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
            total_files += 1

        total_folders += len(dirs)
        print(f'\r{root}', end="", flush=True)
    print("\n")
    return total_size, total_files, total_folders

def remove_empty_folders(folder):
    empty_folders_count = 0
    deleted_folders = []
    failed_to_delete_folders = []

    # Przed usunięciem pustych folderów
    size_before, files_before, folders_before = get_folder_stats(folder)
    print(f"Przed usunięciem: {files_before} plików, {folders_before} podfolderów, {size_before / 1024/1024:.2f} MB\n")
    
    for root, dirs, files in os.walk(folder, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            
            try:
                if not os.listdir(dir_path):
                    # Jeśli folder jest pusty, usuń go
                    os.rmdir(dir_path)
                    empty_folders_count += 1
                    deleted_folders.append(dir_path)
            except Exception as e:
                failed_to_delete_folders.append((dir_path, str(e)))

    # Po usunięciu pustych folderów
    size_after, files_after, folders_after = get_folder_stats(folder)
    print(f"Po usunięciu: {files_after} plików, {folders_after} podfolderów, {size_after / 1024/1024:.2f} MB\n")
   
    # Wyświetl foldery, które nie udało się usunąć
    if failed_to_delete_folders:
        print("\nNie udało się usunąć następujących folderów:")
        for folder, error_message in failed_to_delete_folders:
            print(f"{folder}: {error_message}")

    return empty_folders_count, deleted_folders

if __name__ == "__main__":
    target_folder = "Z:\\"

    deleted_folders_count, deleted_folders = remove_empty_folders(target_folder)

    print(f"\nUsunięto {deleted_folders_count} pustych folderów.")

    if deleted_folders_count > 0:
        print("\nUsunięte foldery:")
        for folder in deleted_folders:
            print(folder)
