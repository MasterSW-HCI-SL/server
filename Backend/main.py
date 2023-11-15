from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import uvicorn

app = FastAPI(root_path="/")

# Display main page by serving its html file. 
# "html = True" automatically locates index.html in directory folder
app.mount("/", StaticFiles(directory = "../../Web/dist", html = True), name = "frontend")

# Serving the ML model
# Remember to define the URL as "/model/keypoint_classifier.hdf5"
app.mount("/model", StaticFiles(directory="../../hand-gesture-recognition-trainer/model/keypoint_classifier"), name = "model")

# Serving the FSA
#TODO: Insert correct directory path
app.mount("/FSA", StaticFiles(directory = ""), name = "FSA")


@app.exception_handler(404)
def exception_404(input1, input2):
    return RedirectResponse('/')


uvicorn.run(app)