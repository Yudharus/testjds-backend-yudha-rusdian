from pydantic import BaseModel

class IndeksPembangunanManusiaBerdasarkanKabupatenKota(BaseModel):
    id: int
    kode_provinsi: int
    nama_provinsi: str
    kode_kabupaten_kota: int
    nama_kabupaten_kota: str
    indeks_pembangunan_manusia: float
    satuan: str
    tahun: int

    class Config:
        orm_mode = True
        from_attributes = True

class AgamaKepercayaanMasyarakat(BaseModel):
    kode_provinsi: int
    nama_provinsi: str
    bps_kode_kabupaten_kota: int
    bps_nama_kabupaten_kota: str
    bps_kode_kecamatan: int
    bps_nama_kecamatan: str
    bps_kode_desa_kelurahan: int
    bps_nama_desa_kelurahan: str
    kemendagri_kode_kecamatan: str
    kemendagri_nama_kecamatan: str
    kemendagri_kode_desa_kelurahan: str
    kemendagri_nama_desa_kelurahan: str
    mayoritas_penganut_agama_lainnya: str
    tahun: int
    id: int

    class Config:
        orm_mode = True
        from_attributes = True

class JumlahPendudukMiskin(BaseModel):
    id: int
    kode_provinsi: str
    nama_provinsi: str
    kategori_daerah: str
    periode_bulan: str
    jumlah_penduduk: float
    satuan: str
    tahun: int

    class Config:
        orm_mode = True
        from_attributes = True
