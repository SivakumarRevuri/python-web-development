from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def greet():
    return {
        "greet": "Good Morning!!!"
    }
    

@app.get('/about')
def get_about():
    return {"data": "about goes here"}