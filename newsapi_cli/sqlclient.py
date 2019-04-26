import sqlite3
from sqlite3 import Error

class SqlClient(object):

    def __init__(self, db):
        self.db = db
        
  
    def create_connection(self):
        """ create a database connection to the SQLite database
            specified by the db
        :param self: self object
        :return: Connection object or None
        """
        try:
            connection = sqlite3.connect(self.db)
            #print("Connection is established: Database is created")
            return connection
        except Error as e:
            print(e)
     
        return None

    def create_table(self,connection,table):
        """ create a table for the given connection to the SQLite database
            specified by the db
        :param connection: sqlite connection object
        :return: None
        """
        cursor = connection.cursor()
        
        try:
           cursor.execute(
                "CREATE TABLE if not exists "+table+" (source_id text, source_name text, author text, title text, description text, url text PRIMARY KEY, urlToImage text, publishedAt text, content text)")
           print("Table is created")
        except Exception as e:
            print(e)
            
        cursor.close()
        connection.commit()

    def add_newsitem(self, connection, table, top_headlines):
        query = "REPLACE INTO "+table+" VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"

        #connection = sqlite3.connect(database_file)
        try:
            news = list()
            for article in top_headlines['articles']:
                news.clear()
                news.append(article['source']['id'])
                news.append(article['source']['name'])
                news.append(article['author'])
                news.append(article['title'])
                news.append(article['description'])
                news.append(article['url'])
                news.append(article['urlToImage'])
                news.append(article['publishedAt'])
                news.append(article['content'])
            
                cursor = connection.cursor()
                cursor.execute(query, list(news))
        except Exception as e:
            print(e)
            
        cursor.close()
        connection.commit()
        #connection.close()
        #print("Added News Items")
    
    def export_to_csv(self, connection, table, f):                  
        
        connection.row_factory=sqlite3.Row
        crsr=connection.execute("SELECT * From "+table+" LIMIT 2")
        row=crsr.fetchone()
        header=row.keys()
        
        cursor = connection.cursor()
        data = cursor.execute("SELECT * FROM "+table+" ORDER BY publishedAt LIMIT 2")
        #rows = data.fetchall()
        import csv
        file = open(f, 'w', newline="")
        writer = csv.writer(file,delimiter=';')
        writer.writerow(header)  # keys=title you're looking for
        # write the rest
        writer.writerows(data)
        file.close()
        
        #print(header)
        print("Exported latest headlines to "+f)  
        cursor.close()
        connection.close()
    
#def main():
#    sqlClient = SqlClient("newshd")
#    sqlClient.create_connection()
    
#main()
