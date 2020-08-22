import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

# Create AIRLINEID_TBL Part I
# Only create table if it doesn't exist already
conn.execute('''CREATE TABLE IF NOT EXISTS AIRLINEID_TBL
         (CODE INT PRIMARY KEY     NOT NULL,
         DESCRIPTION           TEXT,
         Airline_Name          TEXT,
         Airline_Initial        CHAR(50)
		 );''')
print ("Table AIRLINEID_TBL created successfully")

# Create AIRPORTID_TBL Part II
# Only create table if it doesn't exist already
conn.execute('''CREATE TABLE IF NOT EXISTS AIRPORTIDS_TBL
         (CODE                     INT,
         DESCRIPTION               TEXT,
         Airport_Location          TEXT,
         Airport_Name              CHAR(250)
		 );''')
print ("Table AIRPORTID_TBL created successfully")

# Create AIRPORTSEQID_TBL Part III
# Only create table if it doesn't exist already
conn.execute('''CREATE TABLE IF NOT EXISTS AIRPORTSEQID_TBL
         (CODE INT PRIMARY KEY     NOT NULL,
         DESCRIPTION               TEXT,
         Airport_Location          TEXT,
         Airport_Name              CHAR(250)
		 );''')
print ("Table AIRPORTSEQID_TBL created successfully")

# Create CITY_MARKET_ID Part IV
# Only create table if it doesn't exist already
conn.execute('''CREATE TABLE IF NOT EXISTS CITYMARKETID_TBL
         (CODE INT PRIMARY KEY     NOT NULL,
         DESCRIPTION               TEXT,
         Airport_Region            TEXT,
         Airport_State_Country     CHAR(250)
		 );''')
print ("Table CITYMARKETID_TBL created successfully")

# Create World_Area_Codes PART V
conn.execute('''CREATE TABLE IF NOT EXISTS WORLAREACODE_TBL
         (CODE INT PRIMARY KEY     NOT NULL

		 );''')
print ("Table WORLAREACODE_TBL created successfully")

# Create Ontime_Tbl PART VI
conn.execute('''CREATE TABLE IF NOT EXISTS ONTIM_TBL
         (ORIGIN_AIRPORT_ID INT                 NOT NULL,
          ORIGIN_AIRPORT_SEQ_ID INT             NOT NULL,
          ORIGIN_CITY_MARKET_ID INT             NOT NULL,
          DEST_AIRPORT_ID                       INT,
          DEST_AIRPORT_SEQ_ID                    INT,
          DEST_CITY_MARKET_ID                   INT,
          hash_key TEXT PRIMARY KEY             NOT NULL,
          FOREIGN KEY(DEST_AIRPORT_ID) REFERENCES AIRPORTIDS_TBL(CODE),
          FOREIGN KEY(DEST_AIRPORT_SEQ_ID) REFERENCES AIRPORTID_TBL(CODE),
          FOREIGN KEY(DEST_CITY_MARKET_ID ) REFERENCES CITYMARKETID(CODE)
          
          
		 );''')
print ("Table Ontime_Tbl created successfully")


# Close connection after table structures get created
conn.close()