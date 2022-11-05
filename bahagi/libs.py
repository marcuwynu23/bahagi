import requests,json,os
import termcolor as tc
import pandas as pd
from bs4 import BeautifulSoup as bs
from yaml import dump

def export_to_json(data,filename):
	with open(filename + ".json","w") as f:
		json.dump(data,f,indent=4)
		return True

def export_to_csv(data,filename):
	df = pd.DataFrame(data)
	df.to_csv(filename + ".csv",index=False)
	return True

def export_to_excel(data,filename):
	df = pd.DataFrame(data)
	df.to_excel(filename + ".xlsx",index=False)
	return True


def export_to_xml(data,filename):
	with open(filename + ".xml","w") as f:
				f.write("<data>")
				for row in data["data"]:
					f.write("<row>")
					for col in row:
						f.write("<col>")
						f.write(col)
						f.write("</col>")
					f.write("</row>")
				f.write("</data>")
				return True

def export_to_html(data,filename):
	with open(filename + ".html","w") as f:
				f.write("<table>")
				for row in data["data"]:
					f.write("<tr>")
					for col in row:
						f.write("<td>")
						f.write(col)
						f.write("</td>")
					f.write("</tr>")
				f.write("</table>")
				return True

def export_to_yaml(data,filename):
	with open(filename + ".yml","w") as f:
		dump(data,f)
		return True


class Bahagi:
	def __init__(self,url):
		self.data = {}
		self.data["data"] = []
		self.content = requests.get(url).content
		self.soup = bs(self.content,'html.parser')

	def get_data(self):
		return self.data

	def get_table(self,class_names=None,id=None):
		if class_names is not None:
			table = self.soup.find("table",{"class":class_names})
			if table is not None:
				return table
			return None
		elif id is not None:
			table = self.soup.find("table",{"id":id})
			if table is not None:
				return table
			return None
		else:
			print("Please specify class_names cls id")
			return None

	def get_table_row_data(self,table):
		data = []
		if table is None:
			print("Table is None")
			return None
		tbody = table.find("tbody")
		if tbody is not None:
				rows = tbody.find_all("tr")
				for row in rows:
					cols = row.find_all("td")
					cols = [ele.text.strip() for ele in cols]
					if len(cols) > 0:
						data.append(cols)
		return data


	def get_table_rows(table):
		rows = table.find_all("tr")
		return rows

	def set_data(self,data):
		self.data["data"] = data
		
	def export(self,type,filename):
		data_folder = os.path.join(os.getcwd(), 'data')
		# create data folder if not exists
		if not os.path.exists(data_folder):
			os.makedirs(data_folder)

		filename = os.path.join(data_folder, filename)
		tcbahagi = tc.colored("bahagi:","green")
		# filter type and export
		if type == "json":
			export_to_json(self.data,filename)
			print(tcbahagi,"Exported to json")
		elif type == "csv":
			export_to_csv(self.data,filename)
			print(tcbahagi,"Exported to csv")
		elif type == "xml":
			export_to_xml(self.data,filename)
			print(tcbahagi,"Exported to xml")
		elif type == "html":
			export_to_html(self.data,filename)
			print(tcbahagi,"Exported to html")
		elif type == "excel":
			export_to_excel(self.data,filename)
			print(tcbahagi,"Exported to excel")	
		elif type	== "yaml":
			export_to_yaml(self.data,filename)
			print(tcbahagi,"Exported to yaml")
		else:
			print(tcbahagi,f"'{type}' Invalid type not supported accept only json, csv,xml,html,yaml and excel")
			return False



