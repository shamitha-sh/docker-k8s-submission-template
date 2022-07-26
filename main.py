from fastapi import FastAPI, Request, Response
import requests

app = FastAPI()

@app.get("/")
def root():
    return "CWiCS Assessment"

@app.get("/cc")
def getcc():
    return "POST to this endpoint with JSON to convert to YAML"

@app.post("/cc")
async def postcc(request: Request, response: Response):
    json = await request.json()
    requests.post("http://counter:8080/count").raise_for_status()
    resp = requests.post("http://converter:8080/convert", json=json)
    response.status_code = resp.status_code
    return resp.text

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", workers=1, port=8080)