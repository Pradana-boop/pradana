namamhs = input("Masukkan Nama: ")
nalgoritma = int(input("Masukkan Nilai nalgoritma : "))
nagama = int(input("Masukkan Nilai nagama : "))
nbasisdata = int(input("Masukkan Nilai nbasisdata : "))
npancasila = int(input("Masukkan Nilai npancasila : "))
nindonesia = int(input("Masukkan Nilai nindonesia : "))
nmatematika = int(input("Masukkan Nilai nmatematika : "))
ninggris = int(input("Masukkan Nilai ninggris : "))

print(namamhs)
rata_rata = (nalgoritma + nagama + nbasisdata + npancasila + nindonesia + nmatematika + ninggris) / 7
print(rata_rata)

#penentuan lulus atau tidak 
if rata_rata>=80 and rata_rata<=100:
    print("Nilai : A")
elif rata_rata>=70 and rata_rata<=80:
    print("Nilai : B")
elif rata_rata>=50 and rata_rata<=70:
    print("Nilai = C")
elif rata_rata>=30 and rata_rata<=50:
    print("Nilai = D")
elif rata_rata>=10 and rata_rata<=30:
    print("Nilai = E")
else:
    print("Nilai Lebih dari 100 atau dibawah 10") 