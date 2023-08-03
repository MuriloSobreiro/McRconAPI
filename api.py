from fastapi import FastAPI
from aiomcrcon import Client
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
args = {"host": os.getenv("HOST", "0.0.0.0"),"port":os.getenv("PORT",25575)}
print(args)

async def comando(request: str, senha: str):
    client = Client(args["host"], args["port"], senha)
    await client.connect()

    response = await client.send_cmd(request)

    await client.close()

    return response[0]

@app.put("/players")
async def white_list_add(id: str, senha: str):
    response = await comando(f"whitelist add {id}", senha)
    return response

@app.delete("/players")
async def white_list_remove(id: str, senha: str):
    response = await comando(f"whitelist remove {id}", senha)
    return response

@app.post("/players")
async def white_list(senha: str):
    response = await comando(f"whitelist list", senha)
    return response