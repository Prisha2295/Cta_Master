import mysql.connector
from ..gmu_Testcase.gmu_commonfunctions import randomnumber


def otp_connect(logger):
    # Create a MySQL database connection
    conn = mysql.connector.connect(host='10.0.20.192', database='getmyuni_v2_test_04dec', user='ro_user', password='o$JX8qbGHC#jHiZT')
   
    logger.info(conn)
    print(conn)
    
    query = ("""SELECT otp FROM `lead` where mobile = {}""").format(randomnumber)
    
    cursor = conn.cursor()
    
    cursor.execute(query)
    otp = cursor.fetchone()
    print(otp)
    
    # Close the cursor and database connection
    cursor.close()
    conn.close()