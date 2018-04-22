import os
from flask import Flask, request
import models

# Create a flask app of the specified name
app = Flask(__name__)


# When you go to localhost:PORT in your browser, this code will run
# Port is likely 5000, unless otherwise set. 
@app.route("/")
def hello():
    #Get this IP address of the viewer
    viewerIp=request.remote_addr
    #Create a new Viewer object to save in the database
    viewer=models.Viewer(ip=viewerIp)
    #Save the viewer in the database using our model
    models.save(viewer)
    #Get the count of all viewers in the database
    count=models.count(models.Viewer)
    #Return the string of how many users have accessed this page
    return "Hello #{0}".format(count)

#On startup, if this is main, this section of code will run
if __name__ == "__main__":
    # Get the port to liston on. By default, it will listen on 5000
    # This uses an environmental variable to figure out if another port is requested
    port = int(os.environ.get("PORT", 5000))
    # Tell the Flask app to listen on the specified port and serve requests
    app.run(host='0.0.0.0', port=port)
    


