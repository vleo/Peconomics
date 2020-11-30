from dataclasses import dataclass

from Model.resources import Resource, resources, resourcesDict
from typing import Dict


@dataclass
class Occupation:
    name: str
    resource: Resource
    productivity: float
    socialLevel: int


occupations = [
    Occupation(name="CropFarmer", resource=resourcesDict["Grain"], productivity=0.0, socialLevel=1),
    Occupation(name="CattleFarmer", resource=resourcesDict["Cheese"], productivity=0.0, socialLevel=1),
    Occupation(name="SheepFarmer", resource=resourcesDict["Wool"], productivity=0.0, socialLevel=1),
    Occupation(name="Salter", resource=resourcesDict["Salt"], productivity=0.0, socialLevel=2),
    Occupation(name="Hunter", resource=resourcesDict["Furs"], productivity=0.0, socialLevel=2),
    Occupation(name="Brewer", resource=resourcesDict["Beer"], productivity=0.0, socialLevel=2),
    Occupation(name="Sericulturist", resource=resourcesDict["Silk"], productivity=0.0, socialLevel=3),
    Occupation(name="Dyer", resource=resourcesDict["Dyes"], productivity=0.0, socialLevel=3)
]

occupations = {o.name: o for o in occupations}


@dataclass
class DataBase:
    # базовая продуктивность разных родов деятельности
    baseProductivity: Dict
    socialPointsCoeff: float
    priceGrowCoeff: float
#    cropFarmerBaseProductivity: float
#    cattleFarmerBaseProductivity: float
#    sheepFarmerBaseProductivity: float
#    hunterBaseProductivity: float
#    brewerBaseProductivity: float
#    sericulturistBaseProductivity: float
#    salterBaseProductivity: float
#    dyerBaseProductivity: float
