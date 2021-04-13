import csv
import psycopg2
conn = psycopg2.connect("host=localhost dbname=zno_db user=postgres password = Aleksandra2 port=5432")
cursor = conn.cursor()
with open('D:\dbis\Odata2019File_0.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_2.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_3.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_4.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_5.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_6.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_7.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_8.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_9.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_10.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_11.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_12.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_13.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_14.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_15.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_16.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_17.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_18.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_19.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_20.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_21.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_22.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_23.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_24.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_25.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_26.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_27.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_28.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_29.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_30.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_31.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_32.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_33.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_34.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2019File_35.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_0.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_2.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_3.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_4.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_5.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_6.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_7.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_8.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_9.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_10.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_11.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_12.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_13.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_14.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_15.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_16.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_17.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_18.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_19.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_20.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_21.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_22.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_23.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_24.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_25.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_26.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_27.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_28.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_29.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_30.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_31.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_32.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_33.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_34.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_35.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_36.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
with open('D:\dbis\Odata2020File_37.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    cursor.copy_from(f, 'odata', sep=';')
conn.commit()
query1 = '''
Select regname, max(ukrball100), years
from odata
where ukrteststatus = 'Зараховано'
group by regname, years
'''
cursor.execute(query1)
print("Selecting rows from mobile table using cursor.fetchall")
zno_results = cursor.fetchall()
print("Print each row and it's columns values")
with open('zno_results.csv', 'w', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Region', 'Max2019', 'Max2020'])
    for row in zno_results:
        print("regname= ", row[0], )
        print("ukrball100 = ", row[1])
        print("year  = ", row[2], "\n")
        writer.writerow(row)
cursor.close()
conn.close()
