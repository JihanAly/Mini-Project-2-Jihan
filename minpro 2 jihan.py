akun = {
    "admin1": {"password": "admin123", "role": "admin"},
    "user0001": {"password": "nanda", "role": "user"},
    "user0002": {"password": "liya", "role": "user"},
    "user0003": {"password": "melody", "role": "user"},
    "user0004": {"password": "farhan", "role": "user"}
}

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in akun and akun[username]["password"] == password:
        print(f"Selamat datang, {username}!")
        return akun[username]["role"], username
    else:
        print("Username atau password salah.")
        return None, None

users = {
    "user0001": {"nama": "nanda", "tagihan": [{"jumlah": 10000000, "status": "Belum Bayar"}]},
    "user0002": {"nama": "liya", "tagihan": [{"jumlah": 50000000, "status": "Belum Bayar"}]},
    "user0003": {"nama": "melody", "tagihan": [{"jumlah": 150000, "status": "Belum Bayar"}]},
    "user0004": {"nama": "farhan", "tagihan": [{"jumlah": 750000, "status": "Belum Bayar"}]},
}



def tambah_pengguna():
    id_pengguna = input("Masukkan ID pengguna: ")
    nama_pengguna = input("Masukkan nama pengguna: ")
    users[id_pengguna] = {"nama": nama_pengguna, "tagihan": []}
    print(f"Pengguna {nama_pengguna} berhasil ditambahkan.")

def lihat_pengguna():
    if users:
        for id_pengguna, data in users.items():
            print(f"ID: {id_pengguna}, Nama: {data['nama']}")
    else:
        print("Belum ada pengguna.")



def tambah_tagihan():
    id_pengguna = input("Masukkan ID pengguna: ")
    if id_pengguna in users:
        jumlah_tagihan = float(input("Masukkan jumlah tagihan: "))
        users[id_pengguna]["tagihan"].append({"jumlah": jumlah_tagihan, "status": "Belum Bayar"})
        print(users[id_pengguna]["tagihan"])  
        print(f"Tagihan sebesar {jumlah_tagihan} berhasil ditambahkan.")
    else:
        print("Pengguna tidak ditemukan.")


def lihat_tagihan():
    id_pengguna = input("Masukkan ID pengguna: ")
    if id_pengguna in users and users[id_pengguna]["tagihan"]:
        for i, tagihan in enumerate(users[id_pengguna]["tagihan"], 1):
            print(f"Tagihan {i}: Jumlah {tagihan['jumlah']}, Status: {tagihan['status']}")
    else:
        print("Tidak ada tagihan atau pengguna tidak ditemukan.")

def hapus_tagihan():
    id_pengguna = input("Masukkan ID pengguna: ")
    if id_pengguna in users and users[id_pengguna]["tagihan"]:
        lihat_tagihan()  
        pilihan = int(input("Pilih nomor tagihan yang ingin dihapus: ")) - 1
        if 0 <= pilihan < len(users[id_pengguna]["tagihan"]):
            users[id_pengguna]["tagihan"].pop(pilihan)
            print("Tagihan berhasil dihapus.")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Pengguna atau tagihan tidak ditemukan.")



def bayar_tagihan(username):
    if username in users and users[username]["tagihan"]:
        for i, tagihan in enumerate(users[username]["tagihan"], 1):
            if tagihan["status"] == "Belum Bayar":
                print(f"Tagihan {i}: Jumlah {tagihan['jumlah']}, Status: {tagihan['status']}")
        pilihan = int(input("Pilih nomor tagihan yang ingin dibayar: ")) - 1
        if 0 <= pilihan < len(users[username]["tagihan"]) and users[username]["tagihan"][pilihan]["status"] == "Belum Bayar":
            users[username]["tagihan"][pilihan]["status"] = "Sudah Bayar"
            print("Pembayaran berhasil!")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Tidak ada tagihan untuk dibayar.")



def menu_admin():
    while True:
        print("\n--- Menu Admin ---")
        print("1. Tambah Pengguna")
        print("2. Lihat Pengguna")
        print("3. Tambah Tagihan")
        print("4. Lihat Tagihan")
        print("5. Hapus Tagihan")
        print("6. Logout")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            tambah_pengguna()
        elif pilihan == '2':
            lihat_pengguna()
        elif pilihan == '3':
            tambah_tagihan()
        elif pilihan == '4':
            lihat_tagihan()
        elif pilihan == '5':
            hapus_tagihan()
        elif pilihan == '6':
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")




def menu_user(username):
    while True:
        print("\n--- Menu User ---")
        print("1. Bayar Tagihan")
        print("2. Logout")
        
        pilihan = input("Pilih menu (1-2): ")
        
        if pilihan == '1':
            bayar_tagihan(username)
        elif pilihan == '2':
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")



role, username = login()

if role == "admin":
    menu_admin()
elif role == "user":
    menu_user(username)
else:
    print("Login gagal.")