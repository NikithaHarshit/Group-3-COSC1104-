import os
import shutil

def create_folders(folder_path, categories):
    """
    Create folders for each category if they do not exist.
    """
    for category in categories:
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

def organize_files(folder_path):
    """
    Organize files into folders based on their type.
    """
    # Define file categories and their extensions
    categories = {
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Music": [".mp3", ".wav"],
        "Others": []  # Files that do not match any category
    }

    # Create folders for each category
    create_folders(folder_path, categories.keys())

    # Move files to their respective folders
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        file_moved = False
        for category, extensions in categories.items():
            if any(file_name.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(folder_path, category, file_name))
                file_moved = True
                break
        
        # Move files that don't match any category to "Others"
        if not file_moved:
            shutil.move(file_path, os.path.join(folder_path, "Others", file_name))
    
    print("Files organized successfully!")

def main():
    """
    Main function to run the file organizer.
    """
    folder_path = input("Enter the folder path to organize: ").strip()
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        organize_files(folder_path)
    else:
        print("Invalid folder path. Please try again.")

if __name__ == "__main__":
    main()
