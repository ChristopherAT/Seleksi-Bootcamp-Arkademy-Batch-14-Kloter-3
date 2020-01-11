# Seleksi-Bootcamp-Arkademy-Batch-14-Kloter-3
Jawaban dan Project untuk seleksi bootcamp dari Arkademy Batch 14-3. Ada 5 soal dan 3 project yang harus dikerjakan. Karena soal tidak diijinkan untuk dipublikasi, mohon maaf jika repo ini kurang jelas. Silahkan kunjungi <https://www.arkademy.com/> jika anda tertarik untuk ikut bootcamp ini.

## Daftar Isi

- [Soal 1-5](#Soal-1-Sampai-5)
    - [Soal 1](#Soal-1)
    - [Soal 2](#Soal-2)
    - [Soal 3](#Soal-3)
    - [Soal 4](#Soal-4)
    - [Soal 5](#Soal-5)
- [Soal 6](#Soal-6-(Project))
    - [Soal 6A](#Soal-6A)
    - [Soal 6B](#Soal-6B)
    - [Soal 6C](#Soal-6C)

## Soal 1 Sampai 5
Soal 1 sampai 5 dikerjakan dengan bahasa Python 3. Program tersebut bisa dijalankan dari browser dengan menggunakan [GDB Online Debugger](https://onlinegdb.com/) atau [Repl.it](https://repl.it/languages/python3). Tidak perlu copas kode dari sini ke interpreter online tersebut. Pada penjelasan tiap jawaban sudah diberikan link untuk mencoba program, disertai dengan contoh keluarannya.

### Soal 1
Diminta sebuah fungsi untuk mengembalikan biodata dalam format JSON. [Klik link ini](https://onlinegdb.com/Syo-UVDe8) untuk menjalankan `1.py` yang sudah diberi tambahan kode untuk mengecek hasilnya. Berikut contoh keluaran dari program:

```
{"age": 25, "skills": {"level": "beginner", "skill_name": "web development"}, "is_married": false, "interest_in_coding": true, "hobbies": ["Nonton Film", "Baca buku/vn"], "list_school": {"year_out": 2019, "year_in": 2012, "name": "UGM", "major": "Mathematics"}, "name": "Christopher", "address": "Jl. Martadireja I No 29, Purwokerto, Jawa Tengah"}  
```
Output yang dihasilkan adalah 1 baris teks dalam format JSON. Agar lebih mudah untuk dibaca, dapat digunakan <https://codebeautify.org/>. Berikut hasilnya

```
{
  "age": 25,
  "skills": {
    "level": "beginner",
    "skill_name": "web development"
  },
  "is_married": false,
  "interest_in_coding": true,
  "hobbies": [
    "Nonton Film",
    "Baca buku/vn"
  ],
  "list_school": {
    "year_out": 2019,
    "year_in": 2012,
    "name": "UGM",
    "major": "Mathematics"
  },
  "name": "Christopher",
  "address": "Jl. Martadireja I No 29, Purwokerto, Jawa Tengah"
}
```

### Soal 2
Diminta 2 buah fungsi untuk mengecek apakah username/password sudah memenuhi format yang diberikan. Format untuk username:

- Diawali huruf kecil, 
- Tidak boleh menggunakan special character kecuali ‘_’
- Minimal 5 karakter dan maksimal 12 karakter

Format untuk Password:

- merupakan 7 digit karakter dengan kombinasi 1 simbol, 1 angka dan 5 huruf besar

[Klik link ini](https://onlinegdb.com/By0YT4wlL) untuk menjalankan `2.py`. Berikut contoh output dari program tersebut:

```
---Tes Username---            
arka            : False       
Arka_demy12     : False       
arka_demy12     : True        
arka-demy12     : False       
arka__demy      : True        
arka_12345_demy : False                               
---Tes Password---                                     
CHRIS-7  : True    
CHRIS77  : False   
cHrIs_7  : False   
EMPAT+6  : True    
8*LIMA   : False    
P4SS0RD  : True    
P@SSW0RD : False   
```

### Soal 3

[Klik link ini](https://onlinegdb.com/SyAnJSwgL) untuk menjalankan `3.py`. Berikut contoh masukannya:
```
teks_1 = printer('Hello {0} {1}', 'Arkademian', 'Fighters!')
teks_2 = printer('This is an {2}','Halangan','Rintangan','Exercise')
teks_3 = printer('Nama ikan: {0} {2} {4} {5}','nila','sepeda','lele','arkademy','gurameh','tongkol','wkwkwk')
```
Keluaran:
```
Hello Arkademian Fighters!                
This is an Exercise     
Nama ikan: nila lele gurameh tongkol
```

### Soal 4
[Klik link ini](https://repl.it/repls/InstructiveLoathsomeLesson) untuk menjalankan `4.py`. Berikut contoh masukan dan keluaran yang dihasilkan:

```
Input  1:  ['cat', 'listen', 'code', 'act', 'silent', 'tac']
Output 1:
['cat' 'act' 'tac']
['listen' 'silent']
Input  2:  ['try', 'fire', 'dark']
Output 2:
Tidak ditemukan!
```

Untuk soal ini tidak digunakan <https://onlinegdb.com/> karena versi numpy yang disediakan belum di-upgrade.

### Soal 5
Diminta fungsi untuk membuat sebuah array yang didalamnya terdiri dari deret angka bilangan ganji 1-10. Lalu jumlahkan semuanya.

[Klik link ini](https://onlinegdb.com/SJT8zBvgL) untuk menjalankan `5.py`. Berikut contoh masukannya:

```
randomize(5)
randomize(5)
randomize(5)
randomize(10)
```

Keluarannya:

```
Array: [5, 1, 9, 3, 3]
Sum  : 21
Array: [1, 7, 5, 7, 5]
Sum  : 25
Array: [7, 1, 9, 9, 9]
Sum  : 35
Array: [7, 1, 5, 3, 7, 1, 5, 9, 7, 5]
Sum  : 50
```

Karena array yang dihasilkan acak, jika `randomize(5)` dipanggil berkali-kali belum tentu keluarannya akan sama.

## Soal 6 (Project)

Diberikan 3 buah project, yaitu: 
- 6A - membuat database, 
- 6B - tampilan website statis, dan 
- 6c - website dinamis dengan database

### Soal 6A

Diminta membuat database dengan 3 tabel, kemudian gabungkan 3 tabel tersebut dengan SQL query. Database dan query yang diminta sudah disimpan dalam folder `6A`. Berikut Screenshot hasilnya:

![Screenshot SQL query](https://github.com/ChristopherAT99/Seleksi-Bootcamp-Arkademy-Batch-14-Kloter-3/blob/master/Gambar/SS-Query.png "Screenshot SQL query")

### Soal 6B

Diminta membuat website dengan tampilan seperti pada <https://www.figma.com/proto/5vO33YdM2KljNPpkvmGw0S/POS-App-Test?node-id=1%3A2&scaling=scale-down>. Untuk membuka website yang sudah saya buat, clone atau download repo ini kemudian buka `index.html` di folder `6A`. Berikut screenshot tampilan website:

![Screenshot Website](https://github.com/ChristopherAT99/Seleksi-Bootcamp-Arkademy-Batch-14-Kloter-3/blob/master/Gambar/SS-Web6B-1.png "Screenshot Website")

![Screenshot Website](https://github.com/ChristopherAT99/Seleksi-Bootcamp-Arkademy-Batch-14-Kloter-3/blob/master/Gambar/SS-Web6B-2.png "Screenshot Website")

![Screenshot Website](https://github.com/ChristopherAT99/Seleksi-Bootcamp-Arkademy-Batch-14-Kloter-3/blob/master/Gambar/SS-Web6B-3.png "Screenshot Website")

![Screenshot Website](https://github.com/ChristopherAT99/Seleksi-Bootcamp-Arkademy-Batch-14-Kloter-3/blob/master/Gambar/SS-Web6B-4.png "Screenshot Website")

