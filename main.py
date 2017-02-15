

class ShortURL:
	def __init__(self):
		self.url_map = {}
		self.last_url_stored = None

	def find_last_index(self, url):
		for i, char in enumerate(url):
			if char != 'z':
				return i, char
		return None, None

	def set(self, url):
		if url in self.url_map:
			return self.url_map[url]
		else:
			new_url = self.generate_url()
			self.url_map[url] = new_url
			return new_url

	def get(self, url):
		if url in self.url_map:
			return self.url_map[url]
		return None

	def generate_url(self):
		if not self.last_url_stored:
			mapped_url = '0'
		else:
			#find last index that can be upped, then reset the next ones. if the last index is the last char, increase size, reset to all 0's
			i, char = self.find_last_index(self.last_url_stored)
			if i != None:
				if char == '9':
					mapped_url = self.last_url_stored[:i] + 'A' + self.last_url_stored[i+1:]
				elif char == 'Z':
					mapped_url = self.last_url_stored[:i] + 'a' + self.last_url_stored[i+1:]
				else:#go to next char in the sequence
					mapped_url = self.last_url_stored[:i] + chr(ord(char)+1) + self.last_url_stored[i+1:]
			else:
				#all z's, add length
				mapped_url = '0' * (len(self.last_url_stored)+1)

		self.last_url_stored = mapped_url
		return mapped_url

if __name__ == '__main__':
	c = ShortURL()
	for i in range(100):
		url = c.set(str(i))
		print url


