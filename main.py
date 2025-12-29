from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

# isHouseEnabled = False
# isFacilityEnabled = False
# isLightEnabled = False
isTrainEnabled = False
# isFactoryEnabled = False
isBlackout = False

houseLitPercent = 0
facilityLitPercent = 0
lightLitPercent = 0
factoryLitPercent = 0


class CurrentWorldStateModel(BaseModel):
    sessionId: str


class EquipmentPercentModel(BaseModel):
    sessionId: str
    equipment: str
    percent: int


@app.post("/get-current-world-state")
def get_current_world_state(payload: CurrentWorldStateModel):
    print(payload.sessionId)

    global houseLitPercent
    global facilityLitPercent
    global lightLitPercent
    global factoryLitPercent
    global isTrainEnabled
    global isBlackout

    state = {
        "houseLitPercent": houseLitPercent,
        "facilityLitPercent": facilityLitPercent,
        "lightLitPercent": lightLitPercent,
        "isTrainEnabled": isTrainEnabled,
        "factoryLitPercent": factoryLitPercent,
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


@app.post("/set-equipment-percent")
def set_equipment_percent(payload: EquipmentPercentModel):
    print(payload.sessionId)
    print(payload.equipment)
    print(payload.percent)

    global houseLitPercent
    global facilityLitPercent
    global lightLitPercent
    global factoryLitPercent
    global isTrainEnabled
    global isBlackout

    if payload.equipment == "house":
        houseLitPercent = payload.percent
    elif payload.equipment == "facility":
        facilityLitPercent = payload.percent
    elif payload.equipment == "light":
        lightLitPercent = payload.percent
    elif payload.equipment == "factory":
        factoryLitPercent = payload.percent
    elif payload.equipment == "train":
        if payload.percent == 0:
            isTrainEnabled = False
        else:
            isTrainEnabled = True

    state = {
        "houseLitPercent": houseLitPercent,
        "facilityLitPercent": facilityLitPercent,
        "lightLitPercent": lightLitPercent,
        "isTrainEnabled": isTrainEnabled,
        "factoryLitPercent": factoryLitPercent,
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

# @app.post("/turn-on-equipment")
# def turn_on_equipment(payload: EquipmentModel):
#     print(payload.sessionId)
#     print(payload.equipment)

#     global isHouseEnabled
#     global isFacilityEnabled
#     global isLightEnabled
#     global isTrainEnabled
#     global isFactoryEnabled
#     global isBlackout

#     if payload.equipment == "light":
#         isLightEnabled = True
#     elif payload.equipment == "train":
#         isTrainEnabled = True
#     elif payload.equipment == "factory":
#         isFactoryEnabled = True
#     elif payload.equipment == "house":
#         isHouseEnabled = True
#     elif payload.equipment == "facility":
#         isFacilityEnabled = True

#     state = {
#         "isHouseEnabled": isHouseEnabled,
#         "isFacilityEnabled": isFacilityEnabled,
#         "isLightEnabled": isLightEnabled,
#         "isTrainEnabled": isTrainEnabled,
#         "isFactoryEnabled": isFactoryEnabled,
#         "isBlackout": isBlackout
#     }

#     variables = {
#         "totalPower": 3200 + random.randint(-100, 100),
#         "surplusPower": 450
#     }
#     print(state)
#     return {
#         "state": state,
#         "texts": [],
#         "variables": variables
#     }


# @app.post("/turn-off-equipment")
# def turn_off_equipment(payload: EquipmentModel):
#     print(payload.sessionId)
#     print(payload.equipment)

#     global isHouseEnabled
#     global isFacilityEnabled
#     global isLightEnabled
#     global isTrainEnabled
#     global isFactoryEnabled
#     global isBlackout

#     if payload.equipment == "light":
#         isLightEnabled = False
#     elif payload.equipment == "train":
#         isTrainEnabled = False
#     elif payload.equipment == "factory":
#         isFactoryEnabled = False
#     elif payload.equipment == "house":
#         isHouseEnabled = False
#     elif payload.equipment == "facility":
#         isFacilityEnabled = False

#     state = {
#         "isHouseEnabled": isHouseEnabled,
#         "isFacilityEnabled": isFacilityEnabled,
#         "isLightEnabled": isLightEnabled,
#         "isTrainEnabled": isTrainEnabled,
#         "isFactoryEnabled": isFactoryEnabled,
#         "isBlackout": isBlackout
#     }

#     variables = {
#         "totalPower": 3200 + random.randint(-100, 100),
#         "surplusPower": 450
#     }
#     print(state)
#     return {
#         "state": state,
#         "texts": [],
#         "variables": variables
#     }
