import winsound
n=int(input("Enter number"))
l=len(str(n))
c=['0.wav','1.wav','2.wav','3.wav','4.wav','5.wav','6.wav','7.wav','8.wav','9.wav']
c1=['10.wav','11.wav','12.wav','13.wav','14.wav','15.wav','16.wav','17.wav','18.wav','19.wav','20.wav','30.wav','40.wav','50.wav','60.wav','70.wav','80.wav','90.wav']
c2=[10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90]
if l==1:
    winsound.PlaySound(c[n],winsound.SND_FILENAME)
    print(c[n])
elif l==2:
    if n in c2:
        winsound.PlaySound(c1[c2.index(n)],winsound.SND_FILENAME)
    else:
        a=n//10
        a=a*10
        winsound.PlaySound(c1[c2.index(a)],winsound.SND_FILENAME)
        r=n%10
        if r!=0:
            winsound.PlaySound(c[r],winsound.SND_FILENAME)
else:
    print("We can download more .wav files to get more sound for more numbers")
