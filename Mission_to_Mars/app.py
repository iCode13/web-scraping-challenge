
from flask import Flask, render_template, redirect
import os
import pymongo
import scrape_mars  # scrape_mars.py
from scrape_mars import mars_info
from scrape_mars import scrape


# # Create Flask app instance
app = Flask(__name__)

# Setup mongoDB connection
CONN = os.getenv("CONN")
client = pymongo.MongoClient(CONN)

db = client.mars
db.mars_info.insert_one(mars_info)

@app.route('/')
def index():
	mars_info = db.mars_info.find_one()
	return render_template("index.html", mars_info=mars_info)


@app.route('/scrape')
def scrape():
	db_mars_info = db.mars_info
	mars_info = scrape_mars.scrape()
    # print(mars_info)
	db_mars_info.update({}, mars_info, upsert=True)
	return redirect("/", code=302)
	

if __name__ == "__main__":
	app.run(debug=True)
