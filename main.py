from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

isHouseEnabled = False
isFacilityEnabled = False
isLightEnabled = False
isTrainEnabled = False
isFactoryEnabled = False
isBlackout = False


class StateModel(BaseModel):
    isHouseEnabled: bool = False
    isFacilityEnabled: bool = False
    isLightEnabled: bool = False
    isTrainEnabled: bool = False
    isFactoryEnabled: bool = False
    isBlackout: bool = False


class CurrentWorldStateModel(BaseModel):
    sessionId: str

class EquipmentModel(BaseModel):
    sessionId: str
    equipment: str

@app.post("/get-current-world-state")
def get_current_world_state(payload: CurrentWorldStateModel):
    print(payload.sessionId)
    global isHouseEnabled
    global isFacilityEnabled
    global isLightEnabled
    global isTrainEnabled
    global isFactoryEnabled
    global isBlackout

    
    return {
        "state": {
            "isHouseEnabled": isHouseEnabled,
            "isFacilityEnabled": isFacilityEnabled,
            "isLightEnabled": isLightEnabled,
            "isTrainEnabled": isTrainEnabled,
            "isFactoryEnabled": isFactoryEnabled,
            "isBlackout": isBlackout
        },
        "texts": [],
        # "texts": ["&cHello, \nI am an &bVillager 0!", "&cHello, \nI am an &bVillager 1!", "&cHello, \nI am an &bVillager 2!"],
        "variables": {
            "totalPower": 3200 + random.randint(-100, 100),
            "surplusPower": 450 + random.randint(-100, 100)
        }
    }

@app.post("/turn-on-equipment")
def turn_on_equipment(payload: EquipmentModel):
    print(payload.sessionId)
    print(payload.equipment)

    global isHouseEnabled
    global isFacilityEnabled
    global isLightEnabled
    global isTrainEnabled
    global isFactoryEnabled
    global isBlackout

    if payload.equipment == "light":
        isLightEnabled = True
    elif payload.equipment == "train":
        isTrainEnabled = True
    elif payload.equipment == "factory":
        isFactoryEnabled = True
    elif payload.equipment == "house":
        isHouseEnabled = True
    elif payload.equipment == "facility":
        isFacilityEnabled = True

    state = {
        "isHouseEnabled": isHouseEnabled,
        "isFacilityEnabled": isFacilityEnabled,
        "isLightEnabled": isLightEnabled,
        "isTrainEnabled": isTrainEnabled,
        "isFactoryEnabled": isFactoryEnabled,
        "isBlackout": isBlackout
    }

    variables = {
        "totalPower": 3200 + random.randint(-100, 100),
        "surplusPower": 450
    }
    print(state)
    return {
        "state": state,
        "texts": [],
        "variables": variables
    }


@app.post("/turn-off-equipment")
def turn_off_equipment(payload: EquipmentModel):
    print(payload.sessionId)
    print(payload.equipment)

    global isHouseEnabled
    global isFacilityEnabled
    global isLightEnabled
    global isTrainEnabled
    global isFactoryEnabled
    global isBlackout

    if payload.equipment == "light":
        isLightEnabled = False
    elif payload.equipment == "train":
        isTrainEnabled = False
    elif payload.equipment == "factory":
        isFactoryEnabled = False
    elif payload.equipment == "house":
        isHouseEnabled = False
    elif payload.equipment == "facility":
        isFacilityEnabled = False

    state = {
        "isHouseEnabled": isHouseEnabled,
        "isFacilityEnabled": isFacilityEnabled,
        "isLightEnabled": isLightEnabled,
        "isTrainEnabled": isTrainEnabled,
        "isFactoryEnabled": isFactoryEnabled,
        "isBlackout": isBlackout
    }

    variables = {
        "totalPower": 3200 + random.randint(-100, 100),
        "surplusPower": 450
    }
    print(state)
    return {
        "state": state,
        "texts": [],
        "variables": variables
    }


# @app.post("/state")
# def receive_state(payload: StateModel):
#     print(payload.model_dump_json())
#     global isLightEnabled
#     isLightEnabled = payload.isLightEnabled
#     state = {
#         "isLightEnabled": isLightEnabled,
#         "isTrainEnabled": payload.isTrainEnabled,
#         "isFactoryEnabled": payload.isFactoryEnabled,
#         "isBlackout": payload.isBlackout
#     }

#     variables = {
#         "totalPower": 3200 + random.randint(-100, 100),
#         "surplusPower": 450
#     }
#     return {
#         "state": state,
#         "texts": [],
#         "variables": variables
#     }



# debug用
# @app.post("/state")
# async def receive_state_raw(req: Request):
#     body = await req.body()
#     print("RAW:", body.decode("utf-8", errors="replace"))
#     return {"ok": True}