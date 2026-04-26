import joblib
from fastapi import FastAPI
from pydantic import BaseModel

class ClientData(BaseModel):
    gender: bool
    age: int
    car_own: bool
    work: bool
    income: float
    high_edu: bool

app = FastAPI()
model = joblib.load('models/credit_model_gb.pkl')

@app.post('/score')
def score(data: ClientData):
    features = [data.gender, data.age, data.car_own, data.work, data.income, data.high_edu]
    approved = not model.predict([features])[0].item()
    return {'approved': approved}