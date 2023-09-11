from datetime import datetime


def create_timestamp_folder_with_data_subfolder():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    folder_name = f"folder_{timestamp}"
    data_folder = os.path.join(folder_name, "data")

    try:
        os.makedirs(data_folder)  
    except FileExistsError:
        print(f"Folder '{folder_name}' and 'data' subfolder already exist.")


if __name__ == "__main__":

    create_timestamp_folder_with_data_subfolder()