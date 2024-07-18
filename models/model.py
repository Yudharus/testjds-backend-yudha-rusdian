from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class IndeksPembangunanManusiaBerdasarkanKabupatenKota(Base):
    __tablename__ = 'indeks_pembangunan_manusia_berdasarkan_kabupatenkota_data'

    id = Column(Integer, primary_key=True, index=True)
    kode_provinsi = Column(Integer)
    nama_provinsi = Column(String)
    kode_kabupaten_kota = Column(Integer)
    nama_kabupaten_kota = Column(String)
    indeks_pembangunan_manusia = Column(Float)
    satuan = Column(String)
    tahun = Column(Integer)

class AgamaKepercayaanMasyarakat(Base):
    __tablename__ = 'agamakepercayaan_dianut_warga'

    id = Column(Integer, primary_key=True, autoincrement=True)
    kode_provinsi = Column(Integer)
    nama_provinsi = Column(String(256))
    bps_kode_kabupaten_kota = Column(Integer)
    bps_nama_kabupaten_kota = Column(String(256))
    bps_kode_kecamatan = Column(Integer)
    bps_nama_kecamatan = Column(String(256))
    bps_kode_desa_kelurahan = Column(Integer)
    bps_nama_desa_kelurahan = Column(String(256))
    kemendagri_kode_kecamatan = Column(String(256))
    kemendagri_nama_kecamatan = Column(String(256))
    kemendagri_kode_desa_kelurahan = Column(String(256))
    kemendagri_nama_desa_kelurahan = Column(String(256))
    mayoritas_penganut_agama_lainnya = Column(String(256))
    tahun = Column(Integer)

class JumlahPendudukMiskin(Base):
    __tablename__ = 'jumlah_penduduk_miskin'

    id = Column(Integer, primary_key=True, index=True)
    kode_provinsi = Column(String(2))
    nama_provinsi = Column(String(255))
    kategori_daerah = Column(String(50))
    periode_bulan = Column(String(10))
    jumlah_penduduk = Column(Float(5, 2))
    satuan = Column(String(50))
    tahun = Column(Integer)
