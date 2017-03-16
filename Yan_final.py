import pandas as pd
import matplotlib.pyplot as plt

#%matplotlib inline

url="http://pbpython.com/extras/sample-salesv2.csv"
sales = pd.read_csv(url)


def menu_options():
    """
        Give the a user a choice to select an option
    """
    reader_choices = [
                        '1. Calculate Average Price',
                        '2. Calculate Total Price',
                        '3. Display a drawing',
                        '4. Quit'
                      ]
    

    #just add a try/except block
    try:
        for i in range(0, len(reader_choices)):
            print(reader_choices[i])
    except:
        print("No choice Available")

    print ()

    return len(reader_choices)
    

def cal_avg_of_cat(category, whatprice):
    """
        Get the average unit or ext price of a category
    """
    whatprice += " price"
    avg_price = 0

    try:
        salesCatSale=sales[sales.category==category]
        avg_price = sum(salesCatSale[whatprice])/sum(salesCatSale['quantity'])
    except:
        print('Something is wrong, you did not get what you expected')

    return avg_price


def cal_ttl_of_cat(category, whatprice):
    """
        Get the total unit or ext price of a category
    """
    whatprice += " price"
    ttl_price = 0

    try:
        salesCatSale=sales[sales.category==category]
        ttl_price = sum(salesCatSale[whatprice])
    except:
        print('Something is wrong, you did not get what you expected')

    return ttl_price


def draw_top10_of_cat(category, whatprice):
    """
        Draw a bar graph with company name and sales category
    """
    whatprice += " price"
    salesCatSale=sales[sales.category==category]

    saleCatSaleComapy = salesCatSale.sort_values(by='name', ascending=False)

    #graph the top 10 shirt sales
    saleCatTopTen = salesCatSale.sort_values(by=whatprice,ascending=False).head(10)


    belt_plot = saleCatTopTen.plot(kind="bar", 
                                   title = 'Total ' + category + ' Sales by Company',
                                   x="name",
                                   y=whatprice)
    belt_plot.set_xlabel("Company Name")
    belt_plot.set_ylabel(category + ' Sold ($)')

    plt.show()

# Save read file content to a file with different format
f = open("csv_content","w")
a = ""
for row in sales.iterrows():
    a += "\n" + str(row) +"\n"
    
f.write(a)

f.close()


# Setup a counter to store user choice
reader_choice =0

# Display the user menu
ttl_choices = menu_options()

# As long as the reader choice isn't "quit" get user options
while reader_choice != ttl_choices:
    main_disp = 'Type in a number (1-' + str(ttl_choices) + ')'
    
    # guard against non integer number
    try:
        reader_choice = int(input(main_disp))
    except:
        print("Wrong choice.")
        continue

    print("the input is {}\n".format(reader_choice))
    # Calculate Average Price
    if reader_choice == 1:
        category, whatprice = input("Please select a category(Shirt, Shoes or Belt) and price (unit or ext)").split()

        avg = cal_avg_of_cat(category, whatprice)

        print (avg)
                 
    # Calculate Total Price
    elif reader_choice == 2:
        category, whatprice = input("Please select a category(Shirt, Shoes or Belt) and price (unit or ext)").split()

        total =  cal_ttl_of_cat(category, whatprice)

        print (avg)
        
        
    # remove an entry
    elif reader_choice == 3:
        category, whatprice = input("Please select a category(Shirt, Shoes or Belt) and price (unit or ext)").split()

        draw_top10_of_cat(category, whatprice)
      
    # is user enters something strange, show them the menu
    elif reader_choice != 4:
        menu_options ()
