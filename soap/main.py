def soap(brand,price,no_of_pieces):
    print("brand of soap: " +brand)
    print("price of soap: ₹"+str(price))
    print("No. of pieces: "+str(no_of_pieces))
    return no_of_pieces*price
    
soap1 = soap("Dettol", 30, 4)
soap2 = soap("lifebouy",20, 5)
Total_price = soap1+soap2
print("toal price: " +str(Total_price))