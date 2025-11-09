import sqlite3
from config import DATABASE 
con = sqlite3.connect(DATABASE) 
cur = con.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS DATABASE(name,silka,author,desc)
""")


cur.execute("""
    INSERT OR IGNORE INTO DATABASE VALUES

        ('hor1eblePlayer','https://github.com/Hor1e/hor1eblePlayer.git','hor1e', 'Не работающий музыкальный плеер'),
        ('PokeBattles-bot','https://www.youtube.com/watch?v=OmX1V6_gukY','hor1e', 'Бот c боями покемонов'),
        ('EcoVictorina-bot','https://github.com/Hor1e/EcoVictorinaBot.git','hor1e',"Экологичный квиз")
        
""")


cur.execute("""
SELECT name,silka,author,desc FROM DATABASE
""")




info = cur.fetchall()

print(info)


cur.execute("""
DROP TABLE DATABASE
""")







con.commit()

