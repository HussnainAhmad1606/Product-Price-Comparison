import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import webbrowser
from tkinter import *
import urllib
from PIL import ImageTk, Image

# Array for storing daraz product after retrieving it from daraz website
darazProductArr = []


root = Tk()
root.title("Product Price Comparison")
root.geometry("600x600")
search = StringVar()

# Function to get product of name entered by the user
def getDetailsDaraz():
	productClassName = "info--ifj7U"


	darazURL = f"https://www.daraz.pk/catalog/?q={search.get()}"
	# Entering options to not open the browser just get the data without opening the browser
	options = Options()
	options.headless = True
	print("Search Started")
	driver = webdriver.Firefox(options=options, executable_path=r'geckodriver.exe')
	driver.get(darazURL)
	print("Search End")
	print("Finding Elements")

	# Finding Product title, price and photo
	div = driver.find_element(By.CSS_SELECTOR, f".{productClassName} .title--wFj93 a")
	photo = driver.find_element(By.CSS_SELECTOR, ".img--VQr82 .mainPic--ehOdr a img")
	price = driver.find_element(By.CSS_SELECTOR, f".{productClassName} .price--NVB62 span")
	

	link = div.get_attribute("href")
	title = div.text
	print("Elements Found")	
	print("Showing Elements on UI")	

	# Clearing all previous items from array
	darazProductArr.clear()

	# Adding prouduct to array
	darazProductArr.append(link)
	darazProductArr.append(title)
	darazProductArr.append(price.text)
	darazProductArr.append(photo.get_attribute("src"))

	print("Elements Appear on UI")	

	# Checking if no product found
	assert "No results found." not in driver.page_source
	driver.close()


# Function to add spacing to text
def addSpacing(text):
	newText = ""
	i = 0
	text = text.split(" ")
	for val in text:
		if i == 10:
			newText += "\n "
			i = 0
		newText += f"{val} "
		i += 1
		
	return newText

def deleteFrame(frame):
	for item in frame.winfo_children():
		item.destroy()

	print("Items Deleted")

# Main function that will run when user enter product name and click on SEARCH PRODUCT
def getResult():
	getDetailsDaraz()
	deleteFrame(darazProductFrame)
	global darazProductArr
	# Showing the Daraz product on UI
	darazTitle = Label(darazProductFrame, text="DARAZ", font=("Calibri", 20, "bold"))
	darazTitle.pack()
	darazProductName = Label(darazProductFrame, text=addSpacing(darazProductArr[1]))  
	darazProductName.pack()

	darazPriceLabel = Label(darazProductFrame, text=darazProductArr[2])
	darazPriceLabel.pack()

	darazLinkBtn = Button(darazProductFrame, text="Open in DARAZ", command=lambda: webbrowser.open(darazProductArr[0]))
	darazLinkBtn.pack()


	# Showing Daraz product photo on UI
	raw_data = urllib.request.urlopen(darazProductArr[3])
	u = raw_data.read()
	raw_data.close()

	photo = ImageTk.PhotoImage(data=u)
	label1 = Label(darazProductFrame, image=photo, width=600, height=600)
	label1.image = photo
	label1.pack(side=RIGHT)

	print("DONE")


# Search Entry for entering product name on UI
label = Label(root, text="Enter Search Result: ")
label.pack()
entry = Entry(root, textvariable=search)
entry.pack()


button = Button(root, text="Search Product", command=getResult)
button.pack()


# Product Frame for showing daraz and other websites product
productFrame = Frame(root, relief=SUNKEN)

# Daraz Frame where Daraz product will be shown
darazProductFrame = Frame(root)
darazProductFrame.pack(side=LEFT)
productFrame.pack(side=TOP)
root.mainloop()
