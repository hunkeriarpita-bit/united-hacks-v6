from flask import Flask, render_template, request
import sqlite3

# Aapne folder ka naam 'template' rakha hai, isliye hum template_folder specify kar rahe hain
app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    # Pehla page: Welcome screen
    return render_template('home.html')

@app.route('/select_city')
def select_city():
    # Doosra page: City chunne ke liye
    return render_template('select_city.html')

@app.route('/select_emergency')
def select_emergency():
    # Teesri screen: Emergency type dikhane ke liye
    city = request.args.get('city')
    return render_template('select_emergency.html', city=city)

@app.route('/result')
def result():
    # Aakhri screen: Database se contact nikal kar dikhane ke liye
    city = request.args.get('city')
    etype = request.args.get('type')
    
    # Database connection
    conn = sqlite3.connect('databasek/resources.db')
    cursor = conn.cursor()
    
    # Query: City aur Emergency ke hisaab se search karna
    cursor.execute("SELECT name, contact FROM resources WHERE city=? AND type=?", (city, etype))
    rows = cursor.fetchall()
    conn.close()
    
    return render_template('result.html', resources=rows, city=city, type=etype)

if __name__ == '__main__':
    app.run(debug=True)