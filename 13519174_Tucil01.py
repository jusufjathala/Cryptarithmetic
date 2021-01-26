# Nama          : Jusuf Junior Athala
# NIM           : 13519174
# Mata kuliah   : IF2211 - Strategi Algoritma
# Kelas         : K-04
# Tugas         : Penyelesaian Cryptarithmetic dengan Algoritma Brute Force
# Nama file     : 13519174_Tucil01.py

import itertools
import time

#Untuk mendapatkan value dari kata
def get_value(word, solution_mapped):
        value = 0
        factor = 1
        for letter in reversed(word):
                value += factor * solution_mapped[letter]
                factor *= 10
        return value

#Untuk menentukan huruf awal yang terdapat pada mapped solution
def lead_is_zero(solution_mapped,leads):
        for lead in leads :
                if solution_mapped.get(lead)==0 :
                        return True


def crypta_permutation():
# Membuka dan membaca file test.txt
        print("Program membaca file test.txt")
        f=open("test.txt", "r")
        contents =f.read()
        
# Memisahkan operand dan hasil
        operand, result = contents.lower().replace(' ', '').split('+\n------')
        result = result.replace ('\n','')
# Memisahkan semua operand
        operand = operand.split('\n')

# Membuat list untuk huruf-huruf yang muncul dan list untuk huruf yang merupakan huruf awal dari kata        
        letters = set(result)
        leads = set(result[0])
        for word in operand:
                leads.add(word[0])
                for letter in word:
                        letters.add(letter)
        letters = list(letters)
        leads = list(leads)

        count = 0
        count_result = 0
        timer_start = time.perf_counter()
        print ("Program dimulai")
        print ()
        print (contents)
# Memulai permutasi dan melakukan mapping terhadap list huruf yang muncul
        for perm in itertools.permutations(range(10), len(letters)):                
                solution_mapped = dict(zip(letters, perm))
                if lead_is_zero(solution_mapped,leads) :        # Melakukan continue dari iterasi jika terdapat huruf awal dengan value 0
                        continue                        
                count = count+1
                if sum(get_value(word, solution_mapped) for word in operand) == get_value(result, solution_mapped):
                        timer_stop = time.perf_counter()
                        count_result = count_result +1
                        print()
                        print('\n'.join(str(get_value(word, solution_mapped)).rjust(len(result)) for word in operand) + '+\n'+'-'*len(result)+'\n' + str(get_value(result, solution_mapped)))#" = {} (mapping: {})".format(get_value(result, solution_mapped), solution_mapped))
                        print("Hasil ditemukan, waktu yang diperlukan untuk menemukan solusi ke-",count_result,"adalah : ", "%.4f" %(timer_stop-timer_start)," detik")
                        print("Jumlah tes substitusi yang dilakukan untuk menemukan solusi ke-",count_result,"adalah : ", count," kali")
        print()
        print ("Program selesai, total waktu yang diperlukan:", "%.4f" %(time.perf_counter()-timer_start)," detik")
        print ("Jumlah total tes yang dilakukan : ", count," kali")
        print ("Jumlah solusi yang ditemukan : ", count_result," solusi")
        f.close()
                    
if __name__ == '__main__':
        crypta_permutation()
        selesai = input('Tekan Enter untuk keluar dari program')

