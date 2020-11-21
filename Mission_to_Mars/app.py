  
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars # scrape_mars.py
import os
from flask_pymongo import PyMongo

# CONN = os.getenv("CONN")
# client = pymongo.MongoClient(CONN)
# db = client.mars


# Create Flask app instance
app = Flask(__name__)

# Set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo_client = PyMongo(app)

# Route to render index.html template
@app.route('/')
def index():
	mars_info = list(mongo_client.db.mars.find()

	return render_template("index.html", mars_info=mars_info)

@app.route('/scrape')
def scrape():
	mongo_client.db.mars.drop()
    mongo_client.db.mars.insert_one(scrape()) 
    return redirect("/", code=303)
	
if __name__ == "__main__":
	app.run(debug=True)