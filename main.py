from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# Load coordinates from JSON file
with open("result_coords.json") as f:
    coordinates_data = json.load(f)

with open("scoring_routes.json") as f:
    routes_data = json.load(f)

with open("scores.json") as f:
    scores = json.load(f)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from all origins (you might want to restrict this in production)
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/coords")
async def get_coordinates():
    return JSONResponse(content=coordinates_data)

@app.get("/routes")
async def get_coordinates():
    return JSONResponse(content=routes_data)

@app.get("/scores")
async def get_coordinates():
    return JSONResponse(content=scores)