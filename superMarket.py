marketProducts={'Sugar':40,"Oil":98,'Rice':540,
                "Salt":85,"Tumeric":110,"Besan":150,
                "Cereals":215,"Wheat":175}
name=input("Enter Customer Name:")
phoneNum=input("Enter Phone no.:")
n=int(input("Enter No. of Products:")) #no. of products
p={}
q={}
for i in range(n):
    c_keys=input("Product name:")
    c_values=int(input("Quantity:"))
    p[c_keys]=c_values
q=p
print(50*'-')
print(50*' ')
print(16*' ',"Jyothi SuperMarket",16*' ')
print(50*' ')
print("Name:",name)
print("Phone No.:",phoneNum)
print(50*' ')
print(2*' ',"SNo.",5*' ',"ItemName",5*' ',"Quantity",5*" ","Price",2*' ')
c=1
total=0
#for i in range(n):
for k in q:
    for j in marketProducts:
        if j==k:
            price=(q.get(k))*(marketProducts.get(j))
            total=total+price
            print(3*' ',c,7*' ',k,8*' ',q.get(k),"kgs",8*' ',price)
            c+=1   
print(50*' ')
print(25*' ',"Total Bill=",total,'/-',5*' ')
print(50*' ')
print(16*' ',"Thanks for Visiting",15*' ')
print(50*' ')
print(50*'-')