import pickle 
import numpy as np
from interfaces import DataPredict
from fastapi import APIRouter

router = APIRouter()



with open("RFDiabetesv132.pkl", "rb") as file:
    model =pickle.load(file)
    labels = ["Sano", "Enfermo"]



@router.post("/predict")
def predict(data: DataPredict):
    data = data.model_dump()
    print(data)

    

    Pregnancies=data["Pregnancies"]
    Glucose=data["Glucose"]
    BloodPressure=data["BloodPressure"]
    SkinThickness=data["SkinThickness"]
    Insulin=data["Insulin"]
    BMI=data["BMI"]
    DiabetesPedigreeFunction=data["DiabetesPedigreeFunction"]
    Age=data["Age"]
    

    xin = np.array([Pregnancies,Glucose,BloodPressure,	SkinThickness,	Insulin	,BMI,DiabetesPedigreeFunction,Age]).reshape(1,8)
    
    prediction = model.predict(xin)
    print("prediction: ", labels[prediction[0]])
    return{"prediction": labels[prediction[0]]}

    

    

