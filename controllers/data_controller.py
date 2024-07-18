from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from services import data_service
from schemas.data_schemas import IndeksPembangunanManusiaBerdasarkanKabupatenKota, AgamaKepercayaanMasyarakat
from database import get_db
from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


router = APIRouter()

# Dependency function untuk verifikasi token
async def verify_token(x_token: str = Header(...)):
    expected_token = "xYEq9m2f8C8X4F9fZvp2QbndsPfESunN"
    if x_token != expected_token:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.get("/api/indeks-pembangunan-manusia-berdasarkan-kabupatenkota-data", response_model=dict)
async def read_all_data(db: Session = Depends(get_db)):
    data = data_service.get_indeks_pembangunan_manusia_berdasarkan_kabupatenkota_data(db)
    return JSONResponse(content={
        "message": "Get data successful!",
        "error": 0,
        "data": data
    })
    
@router.get("/api/agama-kepercayaan-masyarakat")
async def read_agama_kepercayaan_masyarakat(db: Session = Depends(get_db), authorized: bool = Depends(verify_token)):
    data = data_service.get_agama_kepercayaan_masyarakat(db)
    return JSONResponse(content={
        "message": "Get data successful!",
        "error": 0,
        "data": data
    })

@router.get("/api/jumlah-penduduk-miskin")
async def read_jumlah_penduduk_miskin(db: Session = Depends(get_db), authorized: bool = Depends(verify_token)):
    data = data_service.get_jumlah_penduduk_miskin(db)
    return JSONResponse(content={
        "message": "Get data successful!",
        "error": 0,
        "data": jsonable_encoder(data)
    })
