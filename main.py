from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

isLightEnabled = False


class StateModel(BaseModel):
    isLightEnabled: bool
    isTrainEnabled: bool = False
    isFactoryEnabled: bool = False
    isBlackout: bool = False


@app.get("/energy")
def get_energy():
    global isLightEnabled
    return {
        "state": {
            "isLightEnabled": isLightEnabled,
            "isTrainEnabled": False,
            "isFactoryEnabled": True,
            "isBlackout": False
        },
        "texts": [],
        "variables": {
            "totalPower": 3200 + random.randint(-100, 100),
            "surplusPower": 450
        }
    }


@app.post("/state")
def receive_state(payload: StateModel):
    print(payload.model_dump_json())
    global isLightEnabled
    isLightEnabled = payload.isLightEnabled
    state = {
        "isLightEnabled": isLightEnabled,
        "isTrainEnabled": payload.isTrainEnabled,
        "isFactoryEnabled": payload.isFactoryEnabled,
        "isBlackout": payload.isBlackout
    }

    variables = {
        "totalPower": 3200 + random.randint(-100, 100),
        "surplusPower": 450
    }
    return {
        "state": state,
        "texts": [],
        "variables": variables
    }


# debug用
# @app.post("/state")
# async def receive_state_raw(req: Request):
#     body = await req.body()
#     print("RAW:", body.decode("utf-8", errors="replace"))
#     return {"ok": True}