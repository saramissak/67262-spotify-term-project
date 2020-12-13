import psycopg2 as pg2

con = pg2.connect(database='spotify', user='isdb')  
con.autocommit = True
cur = con.cursor()

print("As a listener I want to see the 5 songs I listened to the most in 2020 so that I can share my music taste with my Instagram followers.")

username = input("Please enter your username: ")

def query(username):
  tmp = '''
    SELECT s.song_name, COUNT(s.song_id)
      FROM Song AS s
           JOIN Listen_Song AS ls ON s.song_id=ls.song_id
     WHERE ls.username = %s
     GROUP BY s.song_id 
     ORDER BY COUNT(s.song_id) DESC
     LIMIT 5;
  '''

  cmd = cur.mogrify(tmp, (username, ))
  cur.execute(cmd)
  rows = cur.fetchall()
  print("\nYour top 5 songs of 2020 are: ")
  for row in rows:
    print(row)

query(username)
