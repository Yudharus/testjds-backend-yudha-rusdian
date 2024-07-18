from collections import defaultdict
from sqlalchemy.orm import Session
from models.model import IndeksPembangunanManusiaBerdasarkanKabupatenKota, AgamaKepercayaanMasyarakat, JumlahPendudukMiskin
from schemas.data_schemas import IndeksPembangunanManusiaBerdasarkanKabupatenKota as IndeksPembangunanManusiaBerdasarkanKabupatenKotaSchema, AgamaKepercayaanMasyarakat as AgamaKepercayaanMasyarakatSchema, JumlahPendudukMiskin as JumlahPendudukMiskinSchema
from typing import List

def get_indeks_pembangunan_manusia_berdasarkan_kabupatenkota_data(db: Session) -> List[dict]:
    data = db.query(IndeksPembangunanManusiaBerdasarkanKabupatenKota).all()

    # Menggunakan defaultdict untuk mengelompokkan data berdasarkan nama_kabupaten_kota
    grouped_data = defaultdict(lambda: {"kode_kabupaten_kota": None, "nama_kabupaten_kota": None, "indeks_pembangunan_manusia": 0.0, "tahun": []})

    for item in data:
        key = item.nama_kabupaten_kota
        if grouped_data[key]["nama_kabupaten_kota"] is None:
            grouped_data[key]["kode_kabupaten_kota"] = item.kode_kabupaten_kota
            grouped_data[key]["nama_kabupaten_kota"] = item.nama_kabupaten_kota
        
        grouped_data[key]["indeks_pembangunan_manusia"] += item.indeks_pembangunan_manusia
        
        if item.tahun not in grouped_data[key]["tahun"]:
            grouped_data[key]["tahun"].append(item.tahun)

    # Format ulang data ke dalam format yang diinginkan
    formatted_data = []
    for key, value in grouped_data.items():
        formatted_data.append({
            "kode_kabupaten_kota": value["kode_kabupaten_kota"],
            "nama_kabupaten_kota": value["nama_kabupaten_kota"],
            "indeks_pembangunan_manusia": round(value["indeks_pembangunan_manusia"], 2),  # Bulatkan nilai indeks_pembangunan_manusia
            "satuan": "POIN",  # Sesuai dengan data asli, Anda dapat mengubahnya sesuai kebutuhan
            # "tahun": value["tahun"]
        })

    return formatted_data


def get_agama_kepercayaan_masyarakat(db: Session) -> List[dict]:
    data = db.query(AgamaKepercayaanMasyarakat).all()

    # Menggunakan defaultdict untuk mengelompokkan data berdasarkan kode_kabupaten_kota dan bps_nama_kabupaten_kota
    processed_data = defaultdict(lambda: defaultdict(lambda: {"agama_count": defaultdict(int),
                                                              "kode_provinsi": None,
                                                              "nama_provinsi": None}))

    for item in data:
        key = (item.bps_kode_kabupaten_kota, item.bps_nama_kabupaten_kota)
        kecamatan_key = item.bps_nama_kecamatan

        # Ambil kode_provinsi dan nama_provinsi dari satu data yang valid
        if processed_data[key][kecamatan_key]["kode_provinsi"] is None:
            processed_data[key][kecamatan_key]["kode_provinsi"] = item.kode_provinsi
            processed_data[key][kecamatan_key]["nama_provinsi"] = item.nama_provinsi

        # Hitung jumlah kemunculan setiap nilai mayoritas_penganut_agama_lainnya dalam satu kecamatan
        processed_data[key][kecamatan_key]["agama_count"][item.mayoritas_penganut_agama_lainnya] += 1

    # Format ulang data ke dalam format yang diinginkan
    formatted_data = []
    for kabupaten_kota, kecamatan_data in processed_data.items():
        for kecamatan, data in kecamatan_data.items():
            # Tentukan mayoritas_penganut_agama_lainnya berdasarkan nilai yang paling sering muncul
            mayoritas_agama = max(data["agama_count"], key=data["agama_count"].get)

            formatted_data.append({
                "kode_provinsi": data["kode_provinsi"],
                "nama_provinsi": data["nama_provinsi"],
                "bps_kode_kabupaten_kota": kabupaten_kota[0],
                "bps_nama_kabupaten_kota": kabupaten_kota[1],
                "bps_nama_kecamatan": kecamatan,
                "mayoritas_penganut_agama_lainnya": mayoritas_agama,
            })

    return formatted_data

def get_jumlah_penduduk_miskin(db: Session) -> List[dict]:
    data = db.query(JumlahPendudukMiskin).all()
    
    # Menggunakan defaultdict untuk mengelompokkan data berdasarkan tahun, kode_provinsi, dan kategori_daerah
    grouped_data = defaultdict(lambda: defaultdict(float))

    for item in data:
        key = (item.tahun, item.kode_provinsi, item.nama_provinsi, item.satuan)
        grouped_data[key][item.kategori_daerah] += float(item.jumlah_penduduk)

    # Format ulang data ke dalam format yang diinginkan
    formatted_data = []
    for key, kategori_daerah_data in grouped_data.items():
        formatted_item = {
            "tahun": key[0],
            "kode_provinsi": key[1],
            "nama_provinsi": key[2],
            "satuan": key[3]
        }
        for kategori_daerah, jumlah_penduduk in kategori_daerah_data.items():
            formatted_item[kategori_daerah] = jumlah_penduduk
        formatted_data.append(formatted_item)

    return formatted_data

