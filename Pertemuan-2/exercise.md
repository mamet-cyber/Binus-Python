x=int(input("panjang="))
y=int(input("lebar="))
z=int(input("tinggi="))
volume_balok= x*y*z
print("volume_balok=",volume_balok,"m3")

rb=int(input("jari-jari="))
pi=3.14
volume_bola=(4/3)*pi*rb*rb*rb
print("volume_bola=", volume_bola, "m3")

rt=int(input("jari-jari="))
t=int(input("tinggi="))
volume_silinder=pi*rt*rt*t
print("volume_silinder=", volume_silinder, "m3")

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
D=(b*b)-(4*a*c)
print("diskriminan=",D)

#A=lokasi binus centre bintaro
#B=lokasi cafe sarang semut jalan bulungan
lonA=float(input("lonA=")) #garis bujur 0 sampai 90, dalam radian, -6.269996126625754
latA=float(input("latA=")) #garis lintang sampai 180, dalam radian, 106.7619382376305
lonB=float(input("lonB=")) #-6.2449587555355714
latB=float(input("latB=")) #106.79735371621442
pi=3.14
d_lon=lonB-lonA
d_lat=latB-latA
import math as m
hav_theta=1/2*((1-m.cos(d_lat))+m.cos(latA)*m.cos(latB)*(1-m.cos(d_lon)))
theta=2*m.asin(m.sqrt(hav_theta))
theta_rad=theta*(pi/180)
rbumi=6371 #jari-jari bumi dalam km
jarak=rbumi*theta_rad
print("theta=", theta, "derajat")
print("jarak 2 lokasi=", jarak, "km") #jarak garis lurus ya, bukan jarak main road
