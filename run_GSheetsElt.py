from GSheetsEtl import GSheetsEtl

if __name__ == "__main__":
    etl_instance = GSheetsEtl(
        "https://docs.google.com/spreadsheets/d/e/2PACX-1vTDjitOlmILea7koCORJkq6QrUcwBJM7K3vy4guXB0mU_nWR6wsPn136bpH6ykoUxyYMW7wTwkzE37l/pub?output=csv",
        "C:/Users/micha/Desktop/School/GIS_305_Programming_forGIS/Assignment 9",
        "csv",
        "C:/Users/micha/Desktop/School/GIS_305_Programming_forGIS/Lab1/Lab1.gdb"
    )

    etl_instance.process()