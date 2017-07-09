'''
It is designed to download full season as of now
'''

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
		'''
		scrape through the parent link and gives all the last parents in form of list
		this list is basically the list of the keys in sitemap of the site

		:return:
		'''
		parent_links = []
		#self.series_name = raw_input("Enter the series you want to download : ")
		self.series_name ='Despicable me'	#need to improve case sensetivity
		self.download_links = self.search.search(self.series_name)#gives all the search links
		count = 0
		flag = 1
		try:
			self.sitemap = self.search.Crawler(self.download_links[count])

		except:
			'''if link is not iterable'''
			print 'search for next link'
			count += 1
		else:
			flag = 1

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
		series_to_download = GetLinks[4]	#need to figure out how to get season number and name
		for link in self.scraper.sitemap[series_to_download]:
			self.download.Download(link)

if __name__ == '__main__':
	# scraperObj = scraper()
	# web_link = scraperObj.link_selector()
	DownloadObj = Download()
	DownloadObj.Perform_Download()
