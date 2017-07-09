import requests

class DownloadUtils:
	def __init__(self):
		pass

	def Download(self,link_to_download):
		file_name = link_to_download.split('/')[-1]

		print "Downloading file:%s" % file_name

		# create response object
		r = requests.get(link_to_download, stream=True)

		# download started
		with open(file_name, 'wb') as f:
			for chunk in r.iter_content(chunk_size=1024):
				if chunk:
					
					f.write(chunk)

		print "%s downloaded!\n" % file_name

		print "All videos downloaded!"
		return