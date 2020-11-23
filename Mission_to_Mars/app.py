from flask import Flask, render_template, redirect
import os
from flask_pymongo import pymongo
from scrape_mars import scrape, driver_setup


# Create Flask app instance
app = Flask(__name__)


# Setup mongoDB connection
CONN = os.getenv("CONN")
client = pymongo.MongoClient(CONN)
db = client.mars_app

# Add mars_dict to mongoDB database
def add_to_database():
    mars_driver = driver_setup()
    mars_dict = scrape(mars_driver)
    db.mars_info.insert_one(mars_dict)

add_to_database()


# Route to Index page
@app.route('/')
def index():
    mars_info = db.mars_info.find_one()
    return render_template("index.html", mars_info=mars_info)


# # Route to start new scrape
@app.route("/scrape")
def webscrape():
    mars_driver = driver_setup()
    mars_data = scrape(mars_driver)
    mars_info = db["mars_info"]
    mars_info.update_one({}, {"$set": mars_data}, upsert=True)
    return redirect("/")


if __name__ == "__main__":
	app.run(debug=True)
