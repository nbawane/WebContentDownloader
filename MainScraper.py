import GoogleSearch
import DownloadUtils

class scraper:
	'''
	This class is used to scrap the google and get all the links
	main purpose of this class is to provide a sitemap to navigate better
	'''
	def __init__(self):
		self.search = GoogleSearch.google()
		self.download_links = ''
		self.sitemap = None
	def link_selector(self):
		parent_links = []
		#self.series_name = raw_input("Enter the series you want to download : ")
		self.series_name = 'Friends'	#need to improve case sensetivity
		self.download_links =  self.search.search(self.series_name)#gives all the search links
		self.sitemap = self.search.Crawler(self.download_links[0])
		for key in self.sitemap:
			print 'parent links : %s '%(key)
			parent_links.append(key)
		return parent_links
class Download:
	'''
	This class will do all the download process
	'''
	def __init__(self):
		self.download = DownloadUtils.DownloadUtils()
		self.scraper = scraper()
	def Perform_Download(self):
		GetLinks = self.scraper.link_selector()

if __name__ == '__main__':
	# scraperObj = scraper()
	# web_link = scraperObj.link_selector()
	DownloadObj = Download()
	DownloadObj.Perform_Download()
