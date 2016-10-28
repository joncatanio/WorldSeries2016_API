from flask import Flask

from content import content_api

# Create the app. 
app = Flask(__name__)

# Register blueprints.
app.register_blueprint(content_api)

@app.route("/")
def main():
   return {"MLB App"}, 200

if __name__ == "__main__":
   app.debug = True
   app.run()
