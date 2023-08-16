# Program to create and display an invoice for Honesty Hairy Car Sales
# Author: Tanner Jones
# Date written: February 10 2023

# Importing Library's for the program 
import datetime

# Constants for the program

LOW_LICENSE_FEE = 75.00  
HIGH_LICENSE_FEE = 165.00  
TRANSFER_FEE = 0.01
LUXURY_FEE = 0.016  
HST_RATE = 0.15
FINANCE_FEE = 39.99

# Inputs for the program, Using while loops for input validation

while True:
    while True:
        first_name = input("Enter the customer's first name (type 'END' to exit): ").title()
        
        if first_name == "":
            print("Customer name can't be blank, please re-enter.")
            
        elif first_name.upper() == "END":
            exit()
            
        else:
            break

    while True:
        last_name = input("Enter the customer's last name: ").title()
        
        if last_name == "":
            print("Customer name can't be blank, please re-enter.")
            
        else:
            break

    streetAdd = input("Enter the customer's street address: ")
    city = input("Enter the customer's city: ")
    province = input("Enter the customer's province (XX): ")
    postal = input("Enter the customer's postal code : ")

    while True:
        phone_number = input("Enter the customer's 10 digit phone number : ")
        if phone_number == "":
            print("Phone number cannot be left blank, please re-enter.")
            
        elif len(phone_number) != 10:
            print("Phone number must be 10 digits only.")
            
        else:
            break

    while True:
        plate_number = input("Enter the customer's license plate number (XXX###): ").upper()

        if plate_number == "":
            print("Plate number cannot be left blank, please re-enter.")
            
        elif len(plate_number) != 6:
            print("Plate number must be 6 characters only ")
            
        elif not plate_number[:3].isalpha():
            print("First three characters of plate number must be letters.")
            
        elif not plate_number[-3:].isdigit():
            print("Last three characters of plate number must be numbers.")
            
        else:
            break

    carMake = input("Enter the make of the car: ")
    carModel = input("Enter the model of the car: ")
    carYear = input("Enter the year car was manufactured: ")

    while True:
        try:
            salePrice = float(input("Enter the sale price of the car (must be less than $50,000.00): "))
            
        except:
            print("Sale price of car is not valid, please re-enter price.")
            
        else:
            if salePrice > 50000.00:
                
                print("Sale price of car cannot be greater then $50,000.00, please re-enter the price.")
                
            else:
                break

    while True:
        
        try:
            tradeValue = float(input("Enter the trade-in value of the customer's car (if none enter 0): "))
            
        except:
            print("Trade-in value of car is not valid, please re-enter.")
            
        else:
            if tradeValue > salePrice:
                print("The trade-in value cannot be greater than the sale price of car, please re-enter.")
                
            else:
                break

    sales_person = input("Enter the sales persons name:  ")

    # Beginning of printing required outputs

    print("-" * 78)
    print()
    print()

    # Calculations for required outputs

    priceTrade = salePrice - tradeValue

    if salePrice <= 5000.00:
        license_fee = LOW_LICENSE_FEE

    else:
        license_fee = HIGH_LICENSE_FEE

    if salePrice > 20000.00:
        luxury_tax = LUXURY_FEE

    else:
        luxury_tax = 0

    # Calculating fees and totals

    transFee = (TRANSFER_FEE * salePrice) + luxury_tax
    subtotal = priceTrade + license_fee + transFee
    salesTax = subtotal * HST_RATE
    totSales = subtotal + salesTax

    current_date = datetime.datetime.now()
    print("Honest Harry Car Sales", " " * 29, "Invoice Date:", current_date.strftime("%m %d, %Y"))

    # Generating Receipt Number

    receipt_num = first_name[0] + last_name[0] + "-" + plate_number[:3] + "-" + phone_number[-4:]
    print("Used Car Sale and Receipt", " " * 26, "Receipt No:  ", receipt_num)
    print()

    # printing rest of required values formatted

    salePriceDsp = "${:,.2f}".format(salePrice) # formatting totals to display $ and correct amount of decimals
    print(" " * 39, "Receipt No:", " " * 15, f"{salePriceDsp:>10s}")

    tradeValueDsp = "${:,.2f}".format(tradeValue)
    print("Sold to:", " " * 30, "Trade Allowance:", " " * 10, f"{tradeValueDsp:>10s}")

    print(" " * 39, "-" * 38)

    priceTradeDsp = "${:,.2f}".format(priceTrade)
    print(" " * 4, first_name[0] + ".", f"{last_name:<26s}", " " * 4, "Price after Trade:", " " * 8,
          f"{priceTradeDsp:>10s}")

    license_feeDsp = "${:,.2f}".format(license_fee)
    print(" " * 4, f"{streetAdd:<29s}", " " * 4, "License Fee:", " " * 14, f"{license_feeDsp:>10s}")

    transFeeDsp = "${:,.2f}".format(transFee)
    print(" " * 4, f"{city:<19s}" + "," + province, postal, " " * 4, "Transfer Fee:", " " * 13, f"{transFeeDsp:>10s}")

    print(" " * 39, "-" * 38)

    subtotalDsp = "${:,.2f}".format(subtotal)
    print("Car Details:", " " * 26, "Subtotal:", " " * 17, f"{subtotalDsp:>10s}")

    salesTaxDsp = "${:,.2f}".format(salesTax)
    print(" " * 39, "HST_RATE:", " " * 22, f"{salesTaxDsp:>10s}")

    print(" " * 4, carYear, f"{carMake:<13s}", f"{carModel:<15s}", "-" * 38)

    totSalesDsp = "${:,.2f}".format(totSales)
    print(" " * 39, "Total sales price:", " " * 8, f"{totSalesDsp:>10s}")
    print("-" * 78)
    print(" " * 21, "Best used cars at the best prices!")
    print()
    print("-" * 78)
    print()

    # setting up payment table.

    print(" " * 29, "Financing", " " * 3, "Total", " " * 6, "Monthly")
    print(" " * 3, "# Years", "  ", "# Payments", " " * 6, "Fee", " " * 6, "Price", " " * 6, "Monthly")
    print(" " * 3, "-" * 60)

    # loop for payment information table and payment start date

    for years in range(1, 5):

        payments = years * 12
        finFee = years * FINANCE_FEE
        totPrice = totSales + finFee
        monPayment = totPrice / payments

        finFeeDsp = "${:.2f}".format(finFee)
        totPriceDsp = "${:,.2f}".format(totPrice)
        monPaymentDsp = "${:,.2f}".format(monPayment)
        print(" " * 5, years, " " * 9, payments, " " * 8, f"{finFeeDsp:>7s}", "  ", f"{totPriceDsp}", " ", f"{monPaymentDsp:>8s}")

    print(" " * 3, "-" * 60)

    # Creating current date and first payment date for invoice

    curDatePlus30 = current_date + datetime.timedelta(days=30)
    print(" " * 3, "Invoice date:", current_date.strftime("%d-%M-%Y"), " " * 4, "First payment date:",
          curDatePlus30.strftime("%d-%M-%Y"))
    print()
    print()


