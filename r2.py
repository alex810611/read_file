def read_file(filename) : # 讀取檔案
	lines = []
	with open(filename ,'r', encoding = 'utf-8-sig') as f :
		for line in f :
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_word_count = 0
	viki_word_count = 0
	for line in lines :
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)

		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
				for m in s[2:]:
					viki_word_count += len(m)
			
	print('viki說了',viki_word_count,'傳了',allen_sticker_count)
	print('allen說了',allen_word_count,'傳了',viki_sticker_count)
	

def write_file(filename,lines): #寫入檔案
	with open(filename , 'w' ) as f:
		for line in lines :
			f.write(line + '\n')


def main():
 	lines = read_file('LINE-Viki.txt')
 	lines = convert(lines)
 	# write_file('output.txt', lines)
 

main()
