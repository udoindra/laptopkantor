#learn_deco.py

def decoration(func):
    def wrapper(*args, **kwargs):
        print("Function started...")
        func(*args, **kwargs)
        print("Function ended")
    return wrapper

@decoration
def cetak_nama():
    print("Indra Afriza Arsad")

@decoration
def hitung_ab(a,b):
    print(f"Hasil: {a+b}")

cetak_nama()
hitung_ab(70,8)