<!-- Core Project -->
Object Detection for Blind People

<!-- Backend.py -->
Backend.py is the server file used to run this program. It will initiate a server at localhost:5000 and run the index.html file over there.
A button press in that webpage will run the python script yolo for image detection through webcam in realtime.

<!-- index.html -->
index.html stores the main html of the website.

<!-- FLASK -->
Flask is necessary to create a backend and to integrate html with python code. 
For a website to run using flask:
1. index.html(the main html file) must be inside templates folder under the main folder.
2. all the images and css files must be stored inside static folder so that the index.html file can access those files.

<!-- Running the code -->
1. Run 'python backend.py'
2. Once the server is setup, open 'localhost:5000' in web browser. The website will be running there.


