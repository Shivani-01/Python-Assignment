import winsound

number=(input("Enter your number:-"))
one_place={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
two_place={11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",
           19:"ninteen",1:"ten",2:"twenty",3:"thirty",4:"fourty",5:"fivty",6:"sixty",7:"seventy",8:"eighty",9:"ninty"}
digit={1:one_place,2:two_place,3:" hundred ",4:" thousand "}
s1=list(number)
length=len(s1)
final=""
for i in s1:
    if(len(number)==1 and i=='0'):
        final+=one_place[int(i)]
    if(i=='0'):
        length-=1
        continue
    if(length==2 and (int(number[-2:]) in range(11,20))):
        final+=two_place[int(number[-2:])]
        break
    elif(length>=3):
        final+=one_place[int(i)]+digit[length]
    else:
        overall=digit[length]
        final+=overall[int(i)]+" "
    length-=1
print(final)
if(final=="sixty five "):
    winsound.PlaySound('60.wav', winsound.SND_FILENAME) 
    winsound.PlaySound('5.wav', winsound.SND_FILENAME)
elif(final=="ninty two "):
    winsound.PlaySound('90.wav', winsound.SND_FILENAME) 
    winsound.PlaySound('2.wav', winsound.SND_FILENAME)
elif(final=="fourty nine "):
    winsound.PlaySound('40.wav', winsound.SND_FILENAME) 
    winsound.PlaySound('9.wav', winsound.SND_FILENAME)
else:
    print("You can download other .wav files and check other sound")