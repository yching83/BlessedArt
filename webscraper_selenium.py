# # # # # # # # # # # # #  # # # # # # # #
#                                        #
#       SELENIUM WEB SCRAPER DOWNLOADING CSVs         #
#       -Yen Ching
#                                        #
#                                        #
# # # # # # # # # # # # #  # # # # # # # #

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from termcolor import cprint
from zipfile import ZipFile
import glob, shutil, time, os

# EDITABLE GLOBAL VARIABLE
DESTINATION_FOLDER = 'C:/Users/yching/Desktop/Assignments/webscraper'
DOWNLOAD_FOLDER = 'C:/Users/yching/Desktop/Downloads'
CHROMEDRIVER_PATH = r'C:/Users/yching/Desktop/Assignments/chromedriver.exe'

# FINAL GLOBAL VARIABLE
URL = 'https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&amp;DB_Short_Name=On-Time'
ZIP_FILE_LAST_PART = 'T_ONTIME_REPORTING.zip'


# downloding files
def download_csv():
    cprint("\n  [+] Opening Webiste to download files.", "cyan")

    # Setting up webdriver
    BROWSER = webdriver.Chrome(executable_path = CHROMEDRIVER_PATH) #, options=options)

    try:
        BROWSER.get(URL)
        time.sleep(1)

        # save main_window
        main_window = BROWSER.current_window_handle

        tds_dataTDRight = BROWSER.find_elements_by_class_name("dataTDRight")
        tab_count = 1
        for td in tds_dataTDRight:
            try:
                href = td.find_element_by_tag_name("a").get_attribute("href")
            except Exception as e:
                try:
                    btn_element = td.find_element_by_tag_name("button")
                    cprint(f"\n    [>] Button Item Found", "yellow")
                    btn_element.click()
                    cprint(f"        [>>>] Button Item Downloaded","green")
                    time.sleep(5)
                    continue
                except:
                    continue

            # download_link = f'https://www.transtats.bts.gov/{href}'
            download_link = href

            # open new blank tab
            BROWSER.execute_script("window.open();")

            # switch to the new window which is second in window_handles array
            BROWSER.switch_to.window(BROWSER.window_handles[tab_count])

            # open successfully and close
            BROWSER.get(download_link)
            cprint(f"\n    [>] URL => {download_link}", "yellow")
            time.sleep(1)
            csv_name = href.split("/")[-1]
            cprint(f"        [>>>] CSV file {csv_name} downloding.", "green")

            # back to the main window
            BROWSER.switch_to.window(main_window)
            tab_count += 1
    except  Exception as e:
        print(f"    [>] EXCEPTION: {str(e)}")
    time.sleep(10)
    BROWSER.quit()
    handeling_CSV_file()


# Moving to Destination Folder, Renaming files and deleting unwanted files
def handeling_CSV_file():
    # moving files to location
    cprint(f"\n  [+] Moving all downloaded file to folder: {DESTINATION_FOLDER}", "cyan")
    for file in glob.glob(f"{DOWNLOAD_FOLDER}/*.csv_"):
        shutil.move(file, DESTINATION_FOLDER)
    cprint(f"      [>>] Done", "green")

    # renaming files
    cprint(f"\n  [+] Renaming all files with proper extensions", "cyan")
    for file in glob.glob(f"{DESTINATION_FOLDER}/*.csv_"):
        os.rename(file, file[:-1])
    cprint(f"      [>>] Done", "green")

    # deleting unwated files
    cprint(f"\n  [+] Deleting all unwated files.", "cyan")
    for file in glob.glob(f"{DESTINATION_FOLDER}/*.csv_"):
        os.remove(file)
    cprint(f"      [>>] Done", "green")


def handeling_Zip_file():
    cprint(f"\n  [+] Started to work with ZIip File", "cyan")

    # moving zip file to location
    cprint(f"      [+] Moving zip file to folder: {DESTINATION_FOLDER}", "yellow")
    for file in glob.glob(f"{DOWNLOAD_FOLDER}/*{ZIP_FILE_LAST_PART}"):
        shutil.move(file, DESTINATION_FOLDER)
    cprint(f"          [>>] Done", "green")

    # extracting all the files
    for file in glob.glob(f"{DESTINATION_FOLDER}/*.zip"):
        with ZipFile(file, 'r') as zip:
            cprint(f"\n      [+] Extracting files from {file}", "yellow")
            zip.extractall()
            cprint(f"          [>>] Extracted", "green")
        os.remove(file)

    # moving all csv files in root folder to CSVs
    for file in glob.glob(f"*.csv"):
        shutil.move(file, DESTINATION_FOLDER)


start_time = time.time()
download_csv()
handeling_Zip_file()
end_time = time.time()

time_diff = (end_time-start_time)
hrs = int((time_diff)//3600)
mins = int(((time_diff)%3600)//60)
secs = int(((time_diff)%3600)%60)

print()
cprint("========================", "red")
cprint(f"[*] Total Time taken: {hrs}hrs {mins}mins {secs}secs", "red")
cprint("========================", "red")
print()
