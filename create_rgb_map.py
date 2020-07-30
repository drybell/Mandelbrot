

# R G B 
# (0,0,255) --> (0,255,255) --> (0,255,0) --> (255,255,0) --> (255, 0, 0)
# 255 * 5 total steps --> 1275 

with open('rgbmap.py', 'w') as f: 
	f.write("rgbmap = {\n")
	cutoff = 10
	for i in range(256):
		f.write('%s: [0,%s,255], ' % (i, i))
		if i % cutoff == 0: 
			f.write('\n')
	for i in range(256):
		f.write('%s: [0,255,%s], ' % (i + 256, i))
		if i % cutoff == 0: 
			f.write('\n')
	for i in range(256):
		f.write('%s: [%s,255,0], ' % (i + 512, i))
		if i % cutoff == 0:
			f.write('\n')
	for i in range(256):
		f.write('%s: [255,%s,0], ' % (i + 768, i))
		if i % cutoff == 0: 
			f.write('\n')
	f.write('\n}')

print('Done')
