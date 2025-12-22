#import
import math


#pilih
print("Pilih perhitungan")
print("1. Luas")
print("2. Volume")
perinp = int(input("Ketik nomor yang kamu pilih: "))


#Luas
if perinp == 1:
#menu luas
    print("MENU:")
    print("1. Luas persegi")
    print("2. Luas persegi panjang")
    print("3. Luas segitiga")
    print("4. Luas lingkaran")

    inpl = int(input("Masukkan nomor opsi yang kamu pilih: "))

    #Persegi
    if inpl == 1:
        inplp = float(input("Masukkan berapa panjang sisi persegi dalam cm: "))
        perhitunganlp = pow(inplp, 2)
        print(f"Luas persegi adalah {perhitunganlp}cm²")
    
    #Persegi panjang
    elif inpl == 2:
        inplpp1 = float(input("Masukkan sisi panjang dalam cm: "))
        inplpp2 = float(input("Masukkan sisi lebar dalam cm: "))
        perhitunganlpp = inplpp1 * inplpp2
        print(f"Luas persegi panjang adalah: {perhitunganlpp}cm²")
    
    #Segitiga
    elif inpl == 3:
        inpls1 = float(input("Masukkan sisi alas dalam cm: "))
        inpls2 = float(input("Masukkan tinggi dalam cm: "))
        perhitunganls = inpls1 * inpls2 / 2
        print(f"Luas segitiga adalah: {perhitunganls}cm²")
    
    #Lingkaran
    elif inpl == 4:
        inpll = float(input("Masukkan jari-jari lingkaran dalam cm: "))
        if inpll % 7 == 0 :
            perhitunganll1 = 22/7 * pow(inpll, 2)
            print(f"Luas lingkaran adalah: {perhitunganll1}cm²")


        elif inpll % 7 != 0:
            perhitunganll2 = math.pi * pow(inpll, 2)
            print(f"Luas lingkaran adalah: {perhitunganll2:.2f}cm²")
        

#Volume
elif perinp == 2:

    #Menu Volume
    print("List:")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Kerucut")
    print("5. Limas")
    print("6. Prisma")
    print("7. Bola")

    #input
    inpv = int(input("Masukkan nomor opsi yang kamu pilih: "))


    #Kubus
    if inpv == 1:
        inpvku = float(input("Masukkan panjang sisi dalam cm: "))
        perhitunganvku = pow(inpvku, 3)
        print(f"Volume kubus adalah: {perhitunganvku}cm³")
    
    #Balok
    elif inpv == 2:
        inpvba1 = float(input("Masukkan panjang balok dalam cm: "))
        inpvba2 = float(input("Masukkan lebar balok dalam cm: "))
        inpvba3 = float(input("Masukkan tinggi balok dalam cm: "))
        perhitunganvba = inpvba1 * inpvba2 *inpvba3
        print(f"Volume balok adalah: {perhitunganvba}cm³")
    
    #Tabung
    elif inpv == 3:
        inpvta1 = float(input("Masukkan jari-jari alas dalam cm: "))
        inpvta2 = float(input("Masukkan tinggi tabung dalam cm: "))
        #L alas
        if inpvta1 % 7 == 0 :
            lata1 = 22/7 * pow(inpvta1, 2)
        
        elif inpvta1 % 7 != 0:
            lata1 = math.pi * pow(inpvta1, 2)

        perhitunganvta = inpvta2 * lata1

        print(f"Volume tabung adalah: {perhitunganvta}cm³")
    
    #Kerucut
    elif inpv == 4:
        inpker1 = float(input("Masukkan jari-jari dalam cm: "))
        inpker2 = float(input("Masukkan tinggi dalam cm: "))

        #L alas
        if inpker1 % 7 == 0 :
            laker1 = 22/7 * pow(inpker1, 2)
        
        elif inpker1 % 7 != 0:
            laker1 = math.pi * pow(inpker1, 2)
        
        #hitungan
        perhitunganvker = 1/3 * laker1 * inpker2

        print(f"Volume dari kerucut adalah: {perhitunganvker}cm³")

    #Limas
    elif inpv == 5:

        print("List:")
        print("1. Limas segitiga")
        print("2. Limas segiempat")
        print("3. Limas segilima beraturan")
        print("4. Limas segienam beraturan")

        #input
        inpvlim = int(input("Masukkan nomor opsi yang kamu pilih: "))

        #limas segitiga
        if inpvlim == 1:
            inpvlim_al3 = float(input("Masukkan sisi alas segitiga dalam cm:"))
            inpvlim_ting3 = float(input("Masukkan tinggi segitiga dalam cm: "))
            inpvlim_tinglim3 = float(input("Masukkan tinggi limas dalam cm: "))
        
            perhitunganvlim3 = 1/3 * (1/2 * inpvlim_al3 * inpvlim_ting3) * inpvlim_tinglim3
            print(f"Volume limas segitiga adalah: {perhitunganvlim3}cm³")
        
        #Limas segiempat
        elif inpvlim == 2:
            inpvlim_al4 = float(input("Masukkan sisi alas segiempat dalam cm: "))
            inpvlim_tinglim4 = float(input("Masukkan tinggi limas dalam cm: "))
            
            perhitunganvlim4 = 1/3 * pow(inpvlim_al4, 2) * inpvlim_tinglim4
            print(f"Volume limas segiempat adalah: {perhitunganvlim4}cm³")

        #Limas segilima
        elif inpvlim == 3:
            inpvlim_si5 = float(input("Masukkan sisi segilima dalam cm: "))
            inpvlim_apotema = float(input("Masukkan apotema dalam cm: "))
            inpvlim_tinglim5 = float(input("Masukkan tinggi limas dalam cm: "))

            lalim5 = 1/2 * (5 * inpvlim_si5) * inpvlim_apotema
            perhitunganvlim5 = 1/3 * lalim5 * inpvlim_tinglim5
            print(f"Volume limas segilima adalah: {perhitunganvlim5}cm³")
        
        #Limas segienam
        elif inpvlim == 4:
            inpvlim_si6 = float(input("Masukkan sisi segienam dalam cm: "))
            inpvlim_tinglim6 = float(input("Masukkan tinggi limas dalam cm: "))

            lalim6 = 2598 * pow(inpvlim_si6, 2)
            perhitunganvlim6 = 1/3 * lalim6 * inpvlim_tinglim6
            print(f"Volume limas segienam adalah: {perhitunganvlim6}cm³")
    #Prisma
    elif inpv == 6:
        
        #menu
        print("List:")
        print("1. Prisma segitiga")
        print("2. Prisma segilima")
        print("3. Prisma segienam")
        print("4. Prisma trapesium")

        #input
        inpvpr = int(input("Masukkan nomor opsi yang kamu pilih: "))

        #prisma segitiga
        if inpvpr == 1:
            inpvprs3_al3 = float(input("Masukkan sisi alas segitiga dengan cm: "))
            inpvprs3_ting3 = float(input("Masukkan tinggi segitiga dengan cm: "))
            inpvprs3_tingpr3 = float(input("Masukkan tinggi prisma dengan cm: "))

            #hitung
            perhitunganvprs3 = (1/2 * inpvprs3_al3 * inpvprs3_ting3) * inpvprs3_tingpr3
            print(f"Volume prisma segitiga adalah : {perhitunganvprs3}cm³")
        

        #prisma segilima
        elif inpvpr == 2:
            inpvprs5 = float(input("Masukkan sisi segilima dalam cm: "))
            inpvprs_apotema5 = float(input("Masukkan apotema dalam cm: "))
            inpvprs_tingpr5 = float(input("Masukkan tinggi prisma dalam cm: "))

            #hitung
            luas5 = 1/2 * (5 * inpvprs5) * inpvprs_apotema5
            perhitunganvprs5 = luas5 * inpvprs_tingpr5
            print(f"Volume prisma segilima adalah : {perhitunganvprs5}cm³")
        
        
        #prisma segienam
        elif inpvpr == 3:
            inpvprs6 = float(input("Masukkan sisi segienam dengan cm: "))
            inpvprs_apotema6 = float(input("Masukkan apotema dengan cm: "))
            inpvprs_tingpr6 = float(input("Masukkan tinggi prisma dalam cm: "))

            #hitung
            luas6 = 1/2 * (6 * inpvprs6) * inpvprs_apotema6
            perhitunganvprs6 = luas6 * inpvprs_tingpr6
            print(f"Volume prisma segienam adalah : {perhitunganvprs6}cm³")

        
        #prisma trapesium
        elif inpvpr == 4:
            inpvprst_a = float(input("Masukkan sisi (a) dengan cm: "))
            inpvprst_b = float(input("Masukkan sisi (b) dengan cm: "))
            inpvprst_t = float(input("Masukkan sisi (t)/tinggi trapesium dengan cm: "))
            inpvprst_T = float(input("Masukkan tinggi prisma dengan cm: "))

            #hitung
            luasprsmtrap = 1/2 * (inpvprst_a + inpvprst_b) * inpvprst_t
            perhitunganvprstrap = luasprsmtrap * inpvprst_T
            print(f"Volume prisma trapesium adalah: {perhitunganvprstrap}cm³")
    
    #bola
    elif inpv == 7:
        inpvbol_jari = float(input("Masukkan jari-jari(radius) bola dengan cm: "))

        #jika kelipatan 7
        if inpvbol_jari % 7 == 0 or inpvbol_jari % 3 == 0:
            perhitunganvbol = 4/3 * 22/7 * pow(inpvbol_jari, 3)
            print(f"Volume bola adalah: {perhitunganvbol}cm³")
        
        #juka bukan kelipatan 7
        elif inpvbol_jari % 7 != 0 or inpvbol_jari % 3 != 0:
            perhitunganvbol = 4/3 * math.pi * pow(inpvbol_jari, 3)
            print(f"Volume bola adalah: {perhitunganvbol}cm³")
        
input("Tekan enter untuk close")