  
from flask import Flask, render_template, redirect
from flask_cors import CORS
import pymongo
import scrape_mars # scrape_mars.py

# Create Flask app instance
app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars

# Route to render index.html template
@app.route('/')
def index():
	mars_data = db.mars_data.find_one()
	return render_template("index.html", mars_data=mars_data)

@app.route('/scrape')
def scrape():
	db_mars_dict = db.mars_data
	mars_data = scrape_mars.scrape
	print(mars_data)
	db_mars_dict.update({}, mars_data, upsert=True)
	return redirect("/", code=302)
	
if __name__ == "__main__":
	app.run(debug=True)