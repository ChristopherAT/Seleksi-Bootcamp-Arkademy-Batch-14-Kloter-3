import numpy as np # Untuk ubah list ke array
def findSame(list_input):
	# Urutkan string pada list untuk mempermudah pengecekan
	list_sorted = []
	for kata in list_input:
		list_sorted.append(''.join(sorted(kata)))
	# Ubah list menjadi array
	array=np.array(list_input)
	
	# Hitung frekuensi kemunculan kata yang sama, ubah array
	array_sorted = np.array(list_sorted)
	kata_unik, count_kata = np.unique(array_sorted, return_counts=True)
	
	# Print hasil
	if max(count_kata) == 1:
		print('Tidak ditemukan!')
		return None
	else:
		list_output = []
		for i in range(len(kata_unik)):
			if count_kata[i]>1:
				list_output.append(list(array[array_sorted==kata_unik[i]]))
				print(array[array_sorted==kata_unik[i]])
		return list_output