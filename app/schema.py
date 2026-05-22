from pydantic import BaseModel

class cardio(BaseModel):
    age_years : int
    height : int
    weight : int
    ap_hi : int
    ap_lo : int
    cholestrol : int
    gluc : int
    smoke : int
    alco : int
    active : int