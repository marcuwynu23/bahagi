from bahagi.libs import Bahagi

if __name__ == '__main__':
	url = "https://www.worldometers.info/coronavirus/"
	fileName = "coronavirus"
	# create bahagi object and pass url containing table
	bahagi = Bahagi(url)
	# get table with class name
	table = bahagi.get_table("main_table_countries")
	#	get table row data
	data = bahagi.get_table_row_data(table)
	# set data to bahagi 
	bahagi.set_data(data)
	# export data to json
	bahagi.export("json",fileName)
	# export data to excel
	bahagi.export("excel",fileName)
	# export data to xml
	bahagi.export("xml",fileName)
	# export data to html
	bahagi.export("html",fileName)
	# export data to csv
	bahagi.export("csv",fileName)
	# export data to yaml
	bahagi.export("yaml",fileName)
