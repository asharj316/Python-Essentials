def Sales():
    Real_time_sales=[]
    total=0

    while True:
        sales_amount=int(input("Enter the sales amount (press '0' to quit ) :")) 
        if sales_amount==0:
            break
        elif sales_amount<=0:
            print("Enter valid value")
        else:
            Real_time_sales.append(sales_amount)
                
    for i in Real_time_sales:
        print("Total sales are :",i)
        total+=i
    print("Total amount of sales in total are:",total)
        
    print("the highest sales is :",max(Real_time_sales))
    print("the lowest sales is :",min(Real_time_sales))
        
Sales()        