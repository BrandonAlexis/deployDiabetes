from pydantic import BaseModel

class DataTest(BaseModel):
    nombre : str
    estudiante: float

class DataPredict(BaseModel):
    Pregnancies	: int
    Glucose	: int
    BloodPressure : int
    SkinThickness : int
    Insulin	: int
    BMI	: float
    DiabetesPedigreeFunction : float
    Age	: int
    