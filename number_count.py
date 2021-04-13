dictionary={0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,100:7}
total=0
for i in range(1,1001):
    if(i<=20):
        total=total+dictionary[i]
    elif(i<100):
        tens=(i//10)*10
        units=i%10
        total=total+dictionary[tens]+dictionary[units]
    elif(i<1000):
        hundreds=i//100
        if (i%100==0):
            total=total+dictionary[hundreds]+dictionary[100]
            continue
        else:
            total=total+dictionary[hundreds]+dictionary[100]+3
        tens=(i%100)
        if(tens<=20):
            total=total+dictionary[tens]
        elif(tens<100):
            units=tens%10
            tens=(tens//10)*10
            total=total+dictionary[tens]+dictionary[units]
    else:
        total=total+dictionary[1]+8

print(total)
