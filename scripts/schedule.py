import os
import schedule
import time

def delete_folder(folder_path: str):
    os.rmdir(folder_path)# replace with the path to the folder you want to delete

schedule.every().day.at("00:00").do(delete_folder) # schedule the deletion to happen every day at midnight

while True:
    schedule.run_pending()
    time.sleep(1)
