rest_img = np.array(img_test)

# read the array
arry = np.fromfile(file, dtype=('float, S2'))

# determine where the data "splits" shoule be
col1 = arry['f0']
diff = col1 - np.roll(col1,1)
idxs = np.where(diff<0)[0]

# only loop thru the "splits"
strts = idxs
stops = list(idxs[1:])+[None]
groups = [data[strt:stop] for strt,stop in zip(strts,stops)]
