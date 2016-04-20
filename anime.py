import psycopg2
import psycopg2.extras

import os
from flask import Flask, render_template, request
app = Flask(__name__)

def connectToDB():
    connectionString = 'dbname=anime user=userx password=abcdefg host=localhost'
    print connectionString
    try:
        return psycopg2.connect(connectionString)
    except:
        print("Can't connect to database.")

@app.route('/')
def mainIndex():
    edit = {'editor': 'Jeffrey Carey', 'date': '2/10/2016', 'time': '3:50 P.M.'}
    isEdit = True
    return render_template('index.html', selected='home', edit=edit, didEdit=isEdit)
    
@app.route('/index')
def showHome():
    edit = {'editor': 'Jeffrey Carey', 'date': '2/10/2016', 'time': '3:50 P.M.'}
    isEdit = True
    return render_template('index.html', selected='home', edit=edit, didEdit=isEdit)

@app.route('/action.html')
def showAction():
    recom1 = "Full Metal Alchemist: Brotherhood"
    descr1 = "This is the story of the two Elric brothers as they search for a philosipher's stone in order to heal their bodies. This is considered one of the all time great animes and is an excellent starting point for new fans."
    recom2 = "Gurren Lagann"
    descr2 = "Our all time favorite anime. This show takes over-the-top to the extreme as it covers the story of Simon and Kamina as they escape their underground village in search of adventrue."
    
    videos = [{'title': 'Full Metal Alchemist: Brotherhood', 'vidlink': 'nkgIKFs17Yc', 'desc': 'Trailer for Full Metal Alchemist: Brotherhood'},
        {'title': 'Gurren Lagann', 'vidlink': 'oXkkMhCuCMg', 'desc': 'Trailer for Gurren Lagann'}]
    
    return render_template('action.html', selected='action', rec1=recom1, desc1=descr1, rec2=recom2, desc2=descr2, clips=videos)
    
@app.route('/comedy.html')
def showComedy():
    recone = "Monthly Girl's Nozaki-kun"
    descone = "A sweet, side-splittingly funny comedy about a high school girl and her crush, who happens to be completely oblivious."
    rectwo = "Good Luck Girl"
    desctwo = "Centers around a girl with more good luck than anyone else in the world and the god of misfortune that tries to take her luck away."
    
    videos = [{'title': 'Monthly Girls Nozaki-kun', 'vidlink': 'vaM2_dPArBM', 'desc': 'Trailer for Monthly Girls Nozaki-kun'},
        {'title': 'Good Luck Girl', 'vidlink': 'JQ5ew_29MYc', 'desc': 'Trailer for Good Luck Girl'}]
    
    return render_template('comedy.html', selected='comedy', rec1=recone, desc1=descone, rec2=rectwo, desc2=desctwo, clips=videos)
    
@app.route('/romance.html')
def showRomance():
    reco1 = "Love, Chunibyo & Other Delusions"
    dscp1 = "This is the story of two young high schoolers as they deal with their first romance, that is muddled by delusions."
    reco2 = "Engaged to the Unidentified"
    dscp2 = "On her 16th birthday, a girl finds out she has a fiance, thanks to her grandfather. The only problem is, there is more to him, than meets the eye."
    
    videos = [{'title': 'Love, Chunibyo & Other Delusions', 'vidlink': 'USgrD2Dqsa0', 'desc': 'Trailer for Love, Chunibyo & Other Delusions'},
        {'title': 'Engaged to the Unidentified', 'vidlink': '_ipk_yuQ1og', 'desc': 'Trailer for Engaged to the Unidentified'}]
    
    return render_template('romance.html', selected='romance', rec1=reco1, desc1=dscp1, rec2=reco2, desc2=dscp2, clips=videos)

@app.route('/horror.html')
def showHorror():
    rcm1 = "Hellsing Ultimate"
    dcpn1 = "A remake of the original Hellsing anime, made to more closely follow the original manga, this story follows the Hellsing organization in England and its greatest agent, Alucard, as they hunt down vampires throughout the country."
    rcm2 = "Elfen Lied"
    dcpn2 = "This is the story of a girl from a new race, called the diclonius, as she struggles to find a place in the world. This show is intended for a mature audience and viewer discretion is advised."
    
    videos = [{'title': 'Hellsing Ultimate', 'vidlink': 'MX5SGyMUbdE', 'desc': 'Trailer for Hellsing Ultimate'},
        {'title': 'Elfen Lied', 'vidlink': 'cJz1YsnIwaw', 'desc': 'Trailer for Elfen Lied'}]
    
    return render_template('horror.html', selected='horror', rec1=rcm1, desc1=dcpn1, rec2=rcm2, desc2=dcpn2, clips=videos)
    
@app.route('/database.html', methods=['GET', 'POST'])
def showDatabase():
    return render_template('database.html', selected='database')

@app.route('/adb.html', methods=['POST'])
def reply():
    conn = connectToDB()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM anime_ratings WHERE name = %s ORDER BY rating DESC, enjoy DESC", (request.form['name1'],))
    except:
        print("No results found")
    results = cur.fetchall()
    return render_template('adb.html', selected='database', animes=results)

@app.route('/all.html', methods=['GET'])
def rtrn():
    conn = connectToDB()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM anime_ratings ORDER BY name, rating DESC, enjoy DESC")
    except:
        print("Could not return results")
    results = cur.fetchall()
    return render_template('all.html', selected='database', table=results)

@app.route('/rate.html', methods=['POST'])
def rate():
    conn = connectToDB()
    cur = conn.cursor()
    animeName=request.form['name']
    try:
        cur.execute("INSERT INTO anime_ratings (name, genre1, genre2, genre3, rating, enjoy) VALUES (%s, %s, %s, %s, %s, %s)", (request.form['name'], request.form['genre'], request.form['genre2'], request.form['genre3'], request.form['rating'], request.form['enjoy']))
    except:
        print ("ERROR Could not insert data into table")
        conn.rollback()
    conn.commit()
    return render_template('rate.html', selected='database', name=animeName)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port =int(os.getenv('PORT', 8080)), debug=True)    