import sqlite3
from sqlite3 import Error
import pandas as pd

DB_FILE_PATH = 'test.db'
CSV_FILE_PATH_AIRLINEID = 'C:\\Users\\yching\\Desktop\\Assignments\\dbinteraction\\L_AIRLINE_ID_OUTCOME.csv'
CSV_FILE_PATH_AIRPORTID = 'C:\\Users\\yching\\Desktop\\Assignments\\dbinteraction\\L_AIRPORT_ID_OUTCOME.csv'
CSV_FILE_PATH_AIRPORTSEQID = 'C:\\Users\\yching\\Desktop\\Assignments\\dbinteraction\\L_AIRPORT_SEQ_ID_OUTCOME.csv'
CSV_FILE_PATH_CITYMARKETID = 'C:\\Users\\yching\\Desktop\\Assignments\\dbinteraction\\L_CITY_MARKET_ID_OUTCOME.csv'
CSV_FILE_PATH_ONTIME = 'C:\\Users\\yching\\Desktop\\Assignments\\dbinteraction\\L_ONTIME_OUTCOME.csv'

def connect_to_db(db_file):
    """
    Connect to an SQlite database, if db file does not exist it will be created
    https://www.excelcise.org/python-sqlite-insert-data-pandas-data-frame/
    """
    sqlite3_conn = None

    try:
        sqlite3_conn = sqlite3.connect(db_file)
        return sqlite3_conn

    except Error as err:
        print(err)

        if sqlite3_conn is not None:
            sqlite3_conn.close()
            
def insert_values_to_table(table_name, csv_file):
    """
    Open a csv file with pandas, store its content in a pandas data frame, change the data frame headers to the table
    column names and insert the data to the table
    """
    
    conn = connect_to_db(DB_FILE_PATH)

    if conn is not None:
        c = conn.cursor()
    
    #At this point, we should have already created our tables in the Create_Tbl_sqlite3 file
    #Continue reading through csv file
    df = pd.read_csv(csv_file)
    
    #Read into cursor and table name from function column names
    df.columns = get_column_names_from_db_table(c, table_name)
    
    #Append the data to the table
    df.to_sql(name=table_name, con=conn, if_exists='append', index=False)
    
    conn.close()
   
        
def get_column_names_from_db_table(sql_cursor, table_name):
    """
    Scrape the column names from a database table to a list
    :param sql_cursor: sqlite cursor
    :param table_name: table name to get the column names from
    :return: a list with table column names
    """

    table_column_names = 'PRAGMA table_info(' + table_name + ');'
    sql_cursor.execute(table_column_names)
    table_column_names = sql_cursor.fetchall()

    column_names = list()

    for name in table_column_names:
        column_names.append(name[1])

    return column_names

#Function created to check data is appended correctly
def select_all_tasks(tablename):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    conn = connect_to_db(DB_FILE_PATH)
    querytbl = tablename
    if conn is not None:
        cur = conn.cursor()
    cur.execute("SELECT * FROM " + querytbl )

    rows = cur.fetchall()

    for row in rows:
        print(row)
    conn.close()
        
#Function to truncate data in case of bad data
def truncate_all_tasks(tablename):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    conn = connect_to_db(DB_FILE_PATH)
    querytbl = tablename
    if conn is not None:
        cur = conn.cursor()
    cur.execute("TRUNCATE TABLE " + querytbl )
    conn.close()
    
if __name__ == '__main__':
    #insert values to AIRLINEID_TBL
    insert_values_to_table('AIRLINEID_TBL', CSV_FILE_PATH_AIRLINEID)
    #insert values to AIRPORTID
    insert_values_to_table('AIRPORTIDS_TBL', CSV_FILE_PATH_AIRPORTID)
    #insert values to AIRPORTSEQID
    insert_values_to_table('AIRPORTSEQID_TBL', CSV_FILE_PATH_AIRPORTSEQID)
    #insert values to CITYMARKETID
    insert_values_to_table('CITYMARKETID_TBL', CSV_FILE_PATH_CITYMARKETID)
    #insert values to ONTIME
    insert_values_to_table('ONTIM_TBL', CSV_FILE_PATH_ONTIME)
    
    #*Check data are in tables
    select_all_tasks('ONTIM_TBL')