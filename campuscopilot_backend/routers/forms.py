from fastapi import APIRouter, Body

router = APIRouter()

@router.post("/kyc")
def submit_kyc(data: dict = Body(...)):
    # Store/process KYC data
    return {"message": "KYC form submitted", "data": data}

@router.post("/tax")
def submit_tax(data: dict = Body(...)):
    # Store/process tax data
    return {"message": "Tax form submitted", "data": data}

@router.post("/visa")
def submit_visa(data: dict = Body(...)):
    # Store/process visa data
    return {"message": "Visa form submitted", "data": data}