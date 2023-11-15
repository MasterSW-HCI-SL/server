# Server endpoint functionality

Very basic Python static file server, using FastAPI.

The server contains three endpoints:
* ```"/"```
    * The front page. This endpoint serves index.html, which in turn utilizes the .css and .js files.
* ```"/model"```
    * This endpoint serves the ML model for recognizing different hand gestures as words. **Remember** to include the actual model file when calling the endpoint. Should look something like this: ```"/model/keypoint_classifier.tflite"```.
* ```"/FSA"```
    * This endpoint serves the state machine used to string different gestures together as words. **Remember** to include the actual FSA file when calling the endpoint. Should look something like this: ```"/FSA/FSA_file.json"```