
# Product Price Comparison

This repository contains code of the tool that compare the product from differnet websites and show them on UI for comparison. The Products are taken from DARAZ website and AMAZON website and software show the products side by side.

# Features
- User can search for a particular product & software will show that product by scraping it from **Daraz.pk** & **Amazon**.
- Software will convert the Amazon curreny from USD to PKR for user experience.
- Search for products on the website by targeting the specific classes of elements.
- Show products side by side to user for price comparison.
- Show the actual photo of the product from website.
- Give the user a link for opening the product for buying & other purposes.

## Technologies:

- **Python** (Programming Language)
- **Selenium** (For Web Scraping Purpose)
- **Tkinter** (For making GUI)


## Installation

1 - Clone the repo by using the following command on your terminal:
```bash
  git clone https://github.com/HussnainAhmad1606/Product-Price-Comparison.git
```
2 - Download gecokodriver from [Here](https://github.com/mozilla/geckodriver/releases)

3 - Copy and Paste it to your script directory.

4 - Run the software as usual by running:
```bash
python main.py
```

5 - Enter the Product name on search box and click on Search Product

6 - After some time, you will see products from DARAZ & AMAZON side by side for comparison.
## Lessons Learned

After completing the project, I got the idea of web scraping using **Python**. Now I can do more advanced web scraping projects in future.
## Future Features
If you want to work on future features of this software then consider implementing the following features:

- Show No Product Found when there is no product related to user searched keyword.

- User can see more than one product by clicking next and go back to previous product.

- Software become unresponsive when you search for the product. Improve this by using multithreading module for running main function in a separate process.
