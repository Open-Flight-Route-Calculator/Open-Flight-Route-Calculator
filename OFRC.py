#!/usr/bin/python
#-*- coding: utf-8 -*-

"""OFRC.py: This program has been developed with academic intends. It is not recommended using it with other purposes.

This program calculates ortodromic and loxodromic routes between two given points in the world and will plot them in a selected projection.

At first, the program would ask the user two options: 1 (One) to enter in a 50 airports database; 2 (Two) for the user to give the exact coordinates of the origin and destination.
Once this step is done, it comes to choose the type of projection. Currently there are 6 of them to choose:
1. (One) for Mercator 
2. (Two) for Ortographic 
3. (Three) for Lambert 
4. (Four) for Cylindrical Equidistant 
5. (Five) for Estereographic
6. (Six) for Azimutal Equidistant

Whether it is not written a valid number, this question will be repeating itself until it is introduced. 

In a more specific topic, the code is programmed in a way that the longitude is being increased to the right (just for no special reason).

At the time of introducing coordinates, North and East are positive, with their value in degrees (with decimals).

Some point you can test are:
Madrid 40N 6W, Tokyo: 35N 139E, Chile 33S 70W.

The expected output is a map with the plotted routes, and once it is closed, a graph which prints latitude, longitude and heading vs distance.
"""

__author__ = "Alberto de Celis Romero, Eduardo Gil Rodríguez, Enrique Olvera Ruíz, Qiang Yang"
__credits__ = ["Pablo Moreno García"]
__license__ = "GNU"
__version__ = "1.0.0"
__maintainer__ = "Alberto de Celis Romero, Eduardo Gil Rodríguez, Enrique Olvera Ruíz"
__email__ = "alberto.decelisro@alum.uca.es, eduardo.gilrodriguez@alum.uca.es, enrique.olveraruiz@alum.uca.es"
__status__ = "Production"


from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from math import *
import os
os.system('cls' if os.name == 'nt' else 'clear') #limpieza.


#Comentarios:

#Definimos los puntos A y B según su latitud y longitud.
#Punto A.

modo=input("Este software está diseñado para calcular la ruta ortodrómica tanto como la loxodrómica que debería seguir una aeronave en un vuelo entre dos puntos cualesquiera de la superficie de la Tierra.\nPara ello, debemos definir los puntos de salida y de destino.\n\nContamos con dos posibilidades, una pequeña base de datos con los 50 principales aeropuertos del mundo, o bien una ventana donde introducir las coordenadas manualmente.\nPulse 1 si desea probar la base de datos o pulse 2 si desea introducir las coordenadas de forma manual (en grados y con decimales): ")
#destino=1 PMG: Esta línea no la entiendo, la dejo comentada
modo=int(modo) # PMG: añado esto para que no haya que introducir comillas
while modo!=1 and modo!=2: # PMG: Quito comillas

    modo=input("\nEl valor no coincide con las opciones del menú.\nPulse 1 si desea probar la base de datos o pulse 2 si desea introducir las coordenadas de forma manual: ")
    modo=int(modo) # PMG: añado esto para que no haya que introducir comillas

#----------------------------------------------
#Base de datos.
if modo==1: # PMG: Quito comillas
	os.system('cls' if os.name == 'nt' else 'clear')
	origen=input("\nLos aeropuertos disponibles son:\n0.Si desea introducir las coordenadas manualmente\n1.Aeropuerto de Atlanta\n2.Aeropuerto de Beijing\n3.Aeropuerto de Chicago\n4.Aeropuerto de Londres (LHR)\n5.Aeropuerto de Tokyo\n6.Aeropuerto de Los Ángeles\n7.Aeropuerto de París\n8.Aeropuerto de Dallas/FT Worth\n9.Aeropuerto de Frankfurt\n10.Aeropuerto de Denver\n11.Aeropuerto de Hong Kong\n12.Aeropuerto de Madrid\n13.Aeropuerto de Dubai\n14.Aeropuerto John F.Kennedy\n15.Aeropuerto de Amsterdam\n16.Aeropuerto de Jakarta\n17.Aeropuerto de Bangkok\n18.Aeropuerto de Singapur\n19.Aeropuerto de Guangzhou\n20.Aeropuerto de Shanghai (PVG)\n21.Aeropuerto de Houston\n22.Aeropuerto de Las Vegas\n23.Aeropuerto de San Francisco\n24.Aeropuerto de Phoenix\n25.Aeropuerto de Charlotte\n26.Aeropuerto de Roma\n27.Aeropuerto de Sydney\n28.Aeropuerto de Miami\n29.Aeropuerto de Munich\n30.Aeropuerto de Orlando\n31.Aeropuerto de Kuala Lumpur\n32.Aeropuerto de Seul Incheon\n33.Aeropuerto de Narita\n34.Aeropuerto de Newark\n35.Aeropuerto de Minneapolis-Saint Paul\n36.Aeropuerto de Estambul\n37.Aeropuerto de Detroit\n38.Aeropuerto de Shanghai (SHA)\n39.Aeropuerto de Toronto\n40.Aeropuerto de Seattle-Tacoma\n41.Aeropuerto de Londres (LGW)\n42.Aeropuerto de Filadelfia\n43.Aeropuerto de Barcelona\n44.Aeropuerto de New Delhi\n45.Aeropuerto de Mumbai\n46.Aeropuerto de Melbourne\n47.Aeropuerto de Sao Paulo\n48.Aeropuerto de Manila\n49.Aeropuerto de Boston\n50.Aeropuerto de Shenzhen\nElija el aeropuerto de origen introduciendo el número de la opción: ")
	origen=int(origen)  # PMG: Añado esto para que no haya que introducir comillas

	while origen!=0 and origen!=1 and origen!=2 and origen!=3 and origen!=4 and origen!=5 and origen!=6 and origen!=7 and origen!=8 and origen!=9 and origen!=10 and origen!=11 and origen!=12 and origen!=13 and origen!=14 and origen!=15 and origen!=16 and origen!=17 and origen!=18 and origen!=19 and origen!=20 and origen!=21 and origen!=22 and origen!=23 and origen!=24 and origen!=25 and origen!=26 and origen!=27 and origen!=28 and origen!=29 and origen!=30 and origen!=31 and origen!=32 and origen!=33 and origen!=34 and origen!=35 and origen!=36 and origen!=37 and origen!=38 and origen!=39 and origen!=40 and origen!=41 and origen!=42 and origen!=43 and origen!=44 and origen!=45 and origen!=46 and origen!=47 and origen!=48 and origen!=49 and origen!=50:
	# PMG: Quito comillas. Ahora que son números se puede simplificar este while
		os.system('cls' if os.name == 'nt' else 'clear')
		origen=input("\nEl valor no coincide con las opciones del menú. Los aeropuertos disponibles son:\n0.Si desea introducir las coordenadas manualmente\n1.Aeropuerto de Atlanta\n2.Aeropuerto de Beijing\n3.Aeropuerto de Chicago\n4.Aeropuerto de Londres (LHR)\n5.Aeropuerto de Tokyo\n6.Aeropuerto de Los Ángeles\n7.Aeropuerto de París\n8.Aeropuerto de Dallas/FT Worth\n9.Aeropuerto de Frankfurt\n10.Aeropuerto de Denver\n11.Aeropuerto de Hong Kong\n12.Aeropuerto de Madrid\n13.Aeropuerto de Dubai\n14.Aeropuerto John F.Kennedy\n15.Aeropuerto de Amsterdam\n16.Aeropuerto de Jakarta\n17.Aeropuerto de Bangkok\n18.Aeropuerto de Singapur\n19.Aeropuerto de Guangzhou\n20.Aeropuerto de Shanghai (PVG)\n21.Aeropuerto de Houston\n22.Aeropuerto de Las Vegas\n23.Aeropuerto de San Francisco\n24.Aeropuerto de Phoenix\n25.Aeropuerto de Charlotte\n26.Aeropuerto de Roma\n27.Aeropuerto de Sydney\n28.Aeropuerto de Miami\n29.Aeropuerto de Munich\n30.Aeropuerto de Orlando\n31.Aeropuerto de Kuala Lumpur\n32.Aeropuerto de Seoul Incheon\n33.Aeropuerto de Narita\n34.Aeropuerto de Newark\n35.Aeropuerto de Minneapolis/St Paul\n36.Aeropuerto de Estanbul\n37.Aeropuerto de Detroit\n38.Aeropuerto de Shanghai (SHA)\n39.Aeropuerto de Toronto\n40.Aeropuerto de Seattle/Tacoma\n41.Aeropuerto de Londres (LGW)\n42.Aeropuerto de Philadelfia\n43.Aeropuerto de Barcelona\n44.Aeropuerto de New Delhi\n45.Aeropuerto de Mumbai\n46.Aeropuerto de Melbourne\n47.Aeropuerto de Sao Paulo\n48.Aeropuerto de Manila\n49.Aeropuerto de Boston\n50.Aeropuerto de Shenzhen\nEscriba el número de la opción deseada: ")
		origen=int(origen)  # PMG: Añado esto para que no haya que introducir comillas
	# PMG: Quito comillas de abajo
	if origen==0:
		destino=0
	if origen==1:
		lat1=33.636666666667
		lon1=-84.428056
	elif origen==2:
		lat1=40.08
		lon1=116.584444
	elif origen==3:
		lat1=41.978611
		lon1=-87.904722
	elif origen==4:
		lat1=51.4775
		lon1=-0.461389
	elif origen==5:
		lat1=35.553333
		lon1=139.781111
	elif origen==6:
		lat1=33.9425
		lon1=-118.408056
	elif origen==7:
		lat1=49.009722
		lon1=2.547778
	elif origen==8:
		lat1=32.896944
		lon1=-97.038056
	elif origen==9:
		lat1=50.033333
		lon1=8.570556
	elif origen==10:
		lat1=39.861667
		lon1=-104.673056
	elif origen==11:
		lat1=22.308889
		lon1=113.914444
	elif origen==12:
		lat1=40.472222
		lon1=-3.560833
	elif origen==13:
		lat1=25.252778
		lon1=55.364444
	elif origen==14:
		lat1=40.639722
		lon1=-73.778889
	elif origen==15:
		lat1=52.3081
		lon1=4.764169
	elif origen==16:
		lat1=-6.127361
		lon1=106.653833
	elif origen==17:
		lat1=13.681111
		lon1=100.747222
	elif origen==18:
		lat1=1.359167
		lon1=103.989444
	elif origen==19:
		lat1=23.392436
		lon1=113.298786
	elif origen==20:
		lat1=31.143333
		lon1=121.805278
	elif origen==21:
		lat1=29.984444
		lon1=-95.341389
	elif origen==21:
		lat1=36.08
		lon1=-115.152222 # PMG: hay dos 21, aclarar
	elif origen==22:
		lat1=37.618889
		lon1=-122.375
	elif origen==23:
		lat1=33.434167
		lon1=-112.011667
	elif origen==24:
		lat1=35.213889
		lon1=-80.943056
	elif origen==25:
		lat1=41.800278
		lon1=12.238889
	elif origen==26:
		lat1=41.48
		lon1=12.14
	elif origen==27:
		lat1=-33.5
		lon1=151.1
	elif origen==28:
		lat1=25.4
		lon1=-80.17
	elif origen==29:
		lat1=48.21
		lon1=11.47
	elif origen==30:
		lat1=28.25
		lon1=-81.18
	elif origen==31:
		lat1=2.44
		lon1=101.42
	elif origen==32:
		lat1=37.27
		lon1=126.26
	elif origen==33:
		lat1=35.45
		lon1=140.23
	elif origen==34:
		lat1=40.41
		lon1=-74.10
	elif origen==35:
		lat1=44.52
		lon1=-93.13
	elif origen==36:
		lat1=40.58
		lon1=28.48
	elif origen==37:
		lat1=42.12
		lon1=-83.21
	elif origen==38:
		lat1=31.11
		lon1=121.20
	elif origen==39:
		lat1=43.40
		lon1=-79.37
	elif origen==40:
		lat1=47.26
		lon1=-122.18
	elif origen==41:
		lat1=51.08
		lon1=-0.11
	elif origen==42:
		lat1=39.52
		lon1=-75.14
	elif origen==43:
		lat1=41.17
		lon1=2.04
	elif origen==44:
		lat1=28.33
		lon1=77.05
	elif origen==45:
		lat1=19.05
		lon1=72.52
	elif origen==46:
		lat1=-37.4
		lon1=144.50
	elif origen==47:
		lat1=-23.26
		lon1=-46.28
	elif origen==48:
		lat1=14.30
		lon1=121.01
	elif origen==49:
		lat1=42.21
		lon1=-71.00
	elif origen==50:
		lat1=22.38
		lon1=113.48
	os.system('cls' if os.name == 'nt' else 'clear')
	# PMG: Aquí había un if que no entiendo y creo que no hace falta, lo quito
	destino=input("\nLos aeropuertos disponibles son:\n0.Si desea introducir las coordenadas manualmente\n1.Aeropuerto de Atlanta\n2.Aeropuerto de Beijing\n3.Aeropuerto de Chicago\n4.Aeropuerto de Londres (LHR)\n5.Aeropuerto de Tokyo\n6.Aeropuerto de Los Ángeles\n7.Aeropuerto de París\n8.Aeropuerto de Dallas/FT Worth\n9.Aeropuerto de Frankfurt\n10.Aeropuerto de Denver\n11.Aeropuerto de Hong Kong\n12.Aeropuerto de Madrid\n13.Aeropuerto de Dubai\n14.Aeropuerto John F.Kennedy\n15.Aeropuerto de Amsterdam\n16.Aeropuerto de Jakarta\n17.Aeropuerto de Bangkok\n18.Aeropuerto de Singapur\n19.Aeropuerto de Guangzhou\n20.Aeropuerto de Shanghai (PVG)\n21.Aeropuerto de Houston\n22.Aeropuerto de Las Vegas\n23.Aeropuerto de San Francisco\n24.Aeropuerto de Phoenix\n25.Aeropuerto de Charlotte\n26.Aeropuerto de Roma\n27.Aeropuerto de Sydney\n28.Aeropuerto de Miami\n29.Aeropuerto de Munich\n30.Aeropuerto de Orlando\n31.Aeropuerto de Kuala Lumpur\n32.Aeropuerto de Seoul Incheon\n33.Aeropuerto de Narita\n34.Aeropuerto de Newark\n35.Aeropuerto de Minneapolis/St Paul\n36.Aeropuerto de Estanbul\n37.Aeropuerto de Detroit\n38.Aeropuerto de Shanghai (SHA)\n39.Aeropuerto de Toronto\n40.Aeropuerto de Seattle/Tacoma\n41.Aeropuerto de Londres (LGW)\n42.Aeropuerto de Philadelfia\n43.Aeropuerto de Barcelona\n44.Aeropuerto de New Delhi\n45.Aeropuerto de Mumbai\n46.Aeropuerto de Melbourne\n47.Aeropuerto de Sao Paulo\n48.Aeropuerto de Manila\n49.Aeropuerto de Boston\n50.Aeropuerto de Shenzhen\nElija el aeropuerto de destino introduciendo el número de la opción: ")
	destino=int(destino) # PMG: añado esto para que no haya que introducir comillas
	
	while destino!=0 and destino!=1 and destino!=2 and destino!=3 and destino!=4 and destino!=5 and destino!=6 and destino!=7 and destino!=8 and destino!=9 and destino!=10 and destino!=11 and destino!=12 and destino!=13 and destino!=14 and destino!=15 and destino!=16 and destino!=17 and destino!=18 and destino!=19 and destino!=20 and destino!=21 and destino!=22 and destino!=23 and destino!=24 and destino!=25 and destino!=26 and destino!=27 and destino!=28 and destino!=29 and destino!=30 and destino!=31 and destino!=32 and destino!=33 and destino!=34 and destino!=35 and destino!=36 and destino!=37 and destino!=38 and destino!=39 and destino!=40 and destino!=41 and destino!=42 and destino!=43 and destino!=44 and destino!=45 and destino!=46 and destino!=47 and destino!=48 and destino!=49 and destino!=50:
	# PMG: Quito comillas. Ahora que son números se puede simplificar este while
		os.system('cls' if os.name == 'nt' else 'clear')		
		destino=input("\nEl valor no coincide con las opciones del menú. Los aeropuertos disponibles son:\n0.Si desea introducir las coordenadas manualmente\n1.Aeropuerto de Atlanta\n2.Aeropuerto de Beijing\n3.Aeropuerto de Chicago\n4.Aeropuerto de Londres (LHR)\n5.Aeropuerto de Tokyo\n6.Aeropuerto de Los Ángeles\n7.Aeropuerto de París\n8.Aeropuerto de Dallas/FT Worth\n9.Aeropuerto de Frankfurt\n10.Aeropuerto de Denver\n11.Aeropuerto de Hong Kong\n12.Aeropuerto de Madrid\n13.Aeropuerto de Dubai\n14.Aeropuerto John F.Kennedy\n15.Aeropuerto de Amsterdam\n16.Aeropuerto de Jakarta\n17.Aeropuerto de Bangkok\n18.Aeropuerto de Singapur\n19.Aeropuerto de Guangzhou\n20.Aeropuerto de Shanghai (PVG)\n21.Aeropuerto de Houston\n22.Aeropuerto de Las Vegas\n23.Aeropuerto de San Francisco\n24.Aeropuerto de Phoenix\n25.Aeropuerto de Charlotte\n26.Aeropuerto de Roma\n27.Aeropuerto de Sydney\n28.Aeropuerto de Miami\n29.Aeropuerto de Munich\n30.Aeropuerto de Orlando\n31.Aeropuerto de Kuala Lumpur\n32.Aeropuerto de Seoul Incheon\n33.Aeropuerto de Narita\n34.Aeropuerto de Newark\n35.Aeropuerto de Minneapolis/St Paul\n36.Aeropuerto de Estanbul\n37.Aeropuerto de Detroit\n38.Aeropuerto de Shanghai (SHA)\n39.Aeropuerto de Toronto\n40.Aeropuerto de Seattle/Tacoma\n41.Aeropuerto de Londres (LGW)\n42.Aeropuerto de Philadelfia\n43.Aeropuerto de Barcelona\n44.Aeropuerto de New Delhi\n45.Aeropuerto de Mumbai\n46.Aeropuerto de Melbourne\n47.Aeropuerto de Sao Paulo\n48.Aeropuerto de Manila\n49.Aeropuerto de Boston\n50.Aeropuerto de Shenzhen\nEscriba el número de la opción deseada: ")
		destino=int(destino) # PMG: añado esto para que no haya que introducir comillas
	# PMG: Quito comillas de abajo
	if destino==1:
		lat2=33.636666666667
		lon2=-84.428056
	elif destino==2:
		lat2=40.08
		lon2=116.584444
	elif destino==3:
		lat2=41.978611
		lon2=-87.904722
	elif destino==4:
		lat2=51.4775
		lon2=-0.461389
	elif destino==5:
		lat2=35.553333
		lon2=139.781111
	elif destino==6:
		lat2=33.9425
		lon2=-118.408056
	elif destino==7:
		lat2=49.009722
		lon2=2.547778
	elif destino==8:
		lat2=32.896944
		lon2=-97.038056
	elif destino==9:
		lat2=50.033333
		lon2=8.570556
	elif destino==10:
		lat2=39.861667
		lon2=-104.673056
	elif destino==11:
		lat2=22.308889
		lon2=113.914444
	elif destino==12:
		lat2=40.472222
		lon2=-3.560833
	elif destino==13:
		lat2=25.252778
		lon2=55.364444
	elif destino==14:
		lat2=40.639722
		lon2=-73.778889
	elif destino==15:
		lat2=52.3081
		lon2=4.764169
	elif destino==16:
		lat2=-6.127361
		lon2=106.653833
	elif destino==17:
		lat2=13.681111
		lon2=100.747222
	elif destino==18:
		lat2=1.359167
		lon2=103.989444
	elif destino==19:
		lat2=23.392436
		lon2=113.298786
	elif destino==20:
		lat2=31.143333
		lon2=121.805278
	elif destino==21:
		lat2=29.984444
		lon2=-95.341389
	elif destino==21:
		lat2=36.08
		lon2=-115.152222 # PMG: hay dos 21, aclarar
	elif destino==22:
		lat2=37.618889
		lon2=-122.375
	elif destino==23:
		lat2=33.434167
		lon2=-112.011667
	elif destino==24:
		lat2=35.213889
		lon2=-80.943056
	elif destino==25:
		lat2=41.800278
		lon2=12.238889
	elif destino==26:
		lat2=41.48
		lon2=12.14
	elif destino==27:
		lat2=-33.5
		lon2=151.1
	elif destino==28:
		lat2=25.4
		lon2=-80.17
	elif destino==29:
		lat2=48.21
		lon2=11.47
	elif destino==30:
		lat2=28.25
		lon2=-81.18
	elif destino==31:
		lat2=2.44
		lon2=101.42
	elif destino==32:
		lat2=37.27
		lon2=126.26
	elif destino==33:
		lat2=35.45
		lon2=140.23
	elif destino==34:
		lat2=40.41
		lon2=-74.10
	elif destino==35:
		lat2=44.52
		lon2=-93.13
	elif destino==36:
		lat2=40.58
		lon2=28.48
	elif destino==37:
		lat2=42.12
		lon2=-83.21
	elif destino==38:
		lat2=31.11
		lon2=121.20
	elif destino==39:
		lat2=43.40
		lon2=-79.37
	elif destino==40:
		lat2=47.26
		lon2=-122.18
	elif destino==41:
		lat2=51.08
		lon2=-0.11
	elif destino==42:
		lat2=39.52
		lon2=-75.14
	elif destino==43:
		lat2=41.17
		lon2=2.04
	elif destino==44:
		lat2=28.33
		lon2=77.05
	elif destino==45:
		lat2=19.05
		lon2=72.52
	elif destino==46:
		lat2=-37.4
		lon2=144.50
	elif destino==47:
		lat2=-23.26
		lon2=-46.28
	elif destino==48:
		lat2=14.30
		lon2=121.01
	elif destino==49:
		lat2=42.21
		lon2=-71.00
	elif destino==50:
		lat2=22.38
		lon2=113.48
	

#----------------------------------------------   
if modo==2 or origen == 0 or destino == 0:# PMG: Quito comillas. 
   
    os.system('cls' if os.name == 'nt' else 'clear')
    lat1=float(input("Introduzca la latitud del origen: "))
    while lat1> 90 or lat1< -90:
        os.system('cls' if os.name == 'nt' else 'clear')
        lat1=float(input("Valor de la latitud del primer punto incorrecto.\nEl valor debe     estar entre -90 y 90: "))

    lon1=float(input("Introduzca la longitud del origen: "))
    while lon1> 180 or lon1< -180:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Valor de la latitud del primer punto punto: {}".format(lat1))
        lon1=float(input("Valor de la longitud del primer punto incorrecto.\nEl valor debe     estar entre -180 y 180: "))
    os.system('cls' if os.name == 'nt' else 'clear') #limpieza.

#Punto B.

    lat2=float(input("Introduzca la latitud del destino: "))
    while lat2> 90 or lat2< -90:
        os.system('cls' if os.name == 'nt' else 'clear')
        lat2=float(input("Valor de la latitud del segundo punto incorrecto,\nEl valor debe     estar entre -90 y 90: "))

    lon2=float(input("Introduzca la longitud del destino: "))
    while lon2> 180 or lon2< -180:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Valor de la latitud del segundo punto: {}".format(lat2))
        lon2=float(input("Valor de la longitud del segundo punto incorrecto,\nEl valor         debe estar entre -180 y 180: "))
    os.system('cls' if os.name == 'nt' else 'clear')


#----------------------------------------------
os.system('cls' if os.name == 'nt' else 'clear')
proyeccion=input("¿Qué tipo de proyección desea representar? Escriba el número de la opción deseada:\nEstán disponibles:\n1. Mercator\n2. Ortográfica\n3. Lambert\n4. Cilíndrica Equidistante\n5. Estereográfica\n6. Acimutal Equidistante\n\n")
proyeccion=int(proyeccion) # PMG: añado esto para que no haya que introducir comillas
#Elección de mapa.
while proyeccion!=1 and proyeccion!=2 and proyeccion!=3 and proyeccion!=4 and proyeccion!=5 and proyeccion!=6:# PMG: Quito comillas. Ahora que son números se puede simplificar este while
    os.system('cls' if os.name == 'nt' else 'clear')
    proyeccion=input("Escriba el número de la opción deseada:\nEstán disponibles:\n1. Mercator\n2. Ortográfica\n3. Lambert\n4. Cilíndrica Equidistante\n5. Estereográfica\n6. Acimutal Equidistante\n\n")
    proyeccion=int(proyeccion) # PMG: añado esto para que no haya que introducir comillas


#----------------------------------------------
#Lambert
#Coeficiente de ampliación
Coef=sqrt(fabs((lon1-lon2)**2+(lat1-lat2)**2))/140

if proyeccion==3:# PMG: Quito comillas.
	if (lon2-lon1)<=-180 or (lon2-lon1)>=180:
		m = Basemap(width=28000000,height=28000000,projection='lcc',lat_0=40,lon_0=((lon1+lon2)/2)-180)
		plt.title(u"Proyección de Lambert")# PMG: Añado la "u" para que matplotlib no se queje de que no entiende las tildes
	else:
		m = Basemap(width=19000000*Coef,height=16000000*Coef, rsphere=(6378137.00,6356752.3142),resolution='l',projection='lcc',area_thresh=10000,lat_0=((lat1+lat2)/2),lon_0=((lon1+lon2)/2))
		plt.title(u"Proyección de Lambert")# PMG: Añado la "u" para que matplotlib no se queje de que no entiende las tildes

#----------------------------------------------
#Azimutal equidistante.

if proyeccion==6:# PMG: Quito comillas.
	if (lon2-lon1)<=-180 or (lon2-lon1)>=180:
		m = Basemap(width=28000000,height=28000000,projection='aeqd',lat_0=40,lon_0=180)
		plt.title(u"Proyección Acimutal Equidistante")# PMG: Añado la "u" para que matplotlib no se queje de que no entiende las tildes
	else:	
		m = Basemap(width=28000000,height=28000000,projection='aeqd',lat_0=40,lon_0=105)
		plt.title(u"Proyección Acimutal Equidistante")# PMG: Añado la "u" para que matplotlib no se queje de que no entiende las tildes
#----------------------------------------------
# Proyección Cilíndrica Equidistante.
if proyeccion==4:# PMG: Quito comillas.
    m = Basemap(projection='cyl',llcrnrlat=-90,urcrnrlat=90,llcrnrlon=-180,urcrnrlon=180,resolution='c')
    plt.title(u"Proyección Cilíndrica Equidistante")# PMG: Añado la "u" para que matplotlib no se queje de que no entiende las tildes
#----------------------------------------------

# Proyección Estereografica.
if proyeccion==5:# PMG: Quito comillas.
	if (lon2-lon1)<=-180 or (lon2-lon1)>=180:
		m = Basemap(width=19000000,height=16000000,resolution='l',projection='stere',lat_ts=50,lat_0=((lat1+lat2)/2),lon_0=((lon1+lon2)/2)-180)
		
		plt.title(u"Proyección Estereográfica")# PMG: Añado la "u" para que matplotlib no se queje de que no entiende las tildes
	else:	
		m = Basemap(width=19000000*Coef,height=16000000*Coef,resolution='l',projection='stere',lat_ts=50,lat_0=((lat1+lat2)/2),lon_0=((lon1+lon2)/2))		
		plt.title(u"Proyección Estereográfica")# PMG: Añado la "u" para que matplotlib no se queje de que no entiende las tildes
#----------------------------------------------

#Mercator
if proyeccion==1:# PMG: Quito comillas.
# Proyección de Mercator España.
    if lon2>-10 and lon2<5 and lat2>35 and lon2<45 and lon1>-10 and lon1<5 and lat1>35 and lon1<45:
        m = Basemap(projection='merc',llcrnrlat=35, urcrnrlat=45,llcrnrlon=-10,urcrnrlon=5,resolution='i')

    else:

# Proyección de Mercator mundo.
        m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180,resolution='i')
    plt.title(u"Proyección de Mercator")# PMG: Añado la "u" para que matplotlib no se queje de que no entiende las tildes

#----------------------------------------------

# Proyección ortográfica.
if proyeccion==2:# PMG: Quito comillas.
	if (lon2-lon1)<=-180 or (lon2-lon1)>=180:
		m = Basemap(projection='ortho',lon_0=((lon1+lon2)/2)-180,lat_0=((lat1+lat2)/2),resolution='i')
		plt.title(u"Proyección Ortográfica")# PMG: Añado la "u" para que matplotlib no se queje de que no entiende las tildes
	else:		
		m = Basemap(projection='ortho',lon_0=((lon1+lon2)/2),lat_0=((lat1+lat2)/2),resolution='i')
		plt.title(u"Proyección Ortográfica")# PMG: Añado la "u" para que matplotlib no se queje de que no entiende las tildes
#----------------------------------------------
#Detalles del mapa.
m.drawparallels(np.arange(-90.,91.,20.))
m.drawmeridians(np.arange(-180.,181.,20.))
m.drawmapboundary(fill_color='aqua')
m.drawcoastlines()
m.fillcontinents(color='lightgreen')
m.drawcountries()


#Dibujo de los puntos A y B.

x1,y1=m(lon1,lat1)
m.plot(x1,y1,'ro')

x2,y2=m(lon2,lat2)
m.plot(x2,y2,'go')

#----------------------------------------------

#Ortodrómica.
A=cos(lat2*pi/180)*sin(lon2*pi/180)*sin(lat1*pi/180)-cos(lat1*pi/180)*sin(lon1*pi/180)*sin(lat2*pi/180)
B=cos(lat1*pi/180)*cos(lon1*pi/180)*sin(lat2*pi/180)-cos(lat2*pi/180)*cos(lon2*pi/180)*sin(lat1*pi/180)
C=cos(lat2*pi/180)*cos(lon2*pi/180)*cos(lat1*pi/180)*sin(lon1*pi/180)-cos(lat2*pi/180)*sin(lon2*pi/180)*cos(lat1*pi/180)*cos(lon1*pi/180)

N=30
loncv=np.zeros(N+2)
latcv=np.zeros(N+2)
xc=np.zeros(N+2)
yc=np.zeros(N+2)
d=np.zeros(N+2)
thetalnorto=np.zeros(N+2)
thetaorto=np.zeros(N+2)

if fabs(lon2-lon1)<180:
    dlam=fabs(lon2-lon1)/N
    if lon2>lon1:#Si lon2>lon1 empieza en lon1 y luego va a ir sumando lambda hacia la derecha.
        latcv[0]=lat1
        loncv[0]=lon1
        latcv[N+1]=lat2
        loncv[N+1]=lon2
    else:#Si lon1>lon2 empieza en lon2 y luego va a ir sumando lambda hacia la derecha.
        latcv[0]=lat2
        loncv[0]=lon2
        latcv[N+1]=lat1
        loncv[N+1]=lon1

    alfa=acos(cos(lat1*pi/180)*cos(lon1*pi/180)*cos((lat2+dlam)*pi/180)*cos(lon2*pi/180)+cos(lat1*pi/180)*sin(lon1*pi/180)*cos(lat2*pi/180)*sin(lon2*pi/180)+sin(lat1*pi/180)*sin(lat2*pi/180))
    dalfa=alfa/N

elif (lon2-lon1)<=-180:#Si lon2-lon1<-180 Debe coger desde lon1 hacia lon2 hacia la derecha.
    dlam=(360+lon2-lon1)/N
    latcv[0]=lat1
    loncv[0]=lon1
    latcv[N+1]=lat2
    loncv[N+1]=lon2
    alfa=acos(cos(lat1*pi/180)*cos(lon1*pi/180)*cos((lat2+dlam)*pi/180)*cos(lon2*pi/180)+cos(lat1*pi/180)*sin(lon1*pi/180)*cos(lat2*pi/180)*sin(lon2*pi/180)+sin(lat1*pi/180)*sin(lat2*pi/180))
    dalfa=alfa/N
elif (lon2-lon1)>=180:#Si lon2-lon1>180 Debe coger desde lon2 hacia lon1 hacia la derecha.
    dlam=(360-lon2+lon1)/N
    latcv[0]=lat2
    loncv[0]=lon2
    latcv[N+1]=lat1
    loncv[N+1]=lon1
    alfa=acos(cos(lat1*pi/180)*cos(lon1*pi/180)*cos((lat2+dlam)*pi/180)*cos(lon2*pi/180)+cos(lat1*pi/180)*sin(lon1*pi/180)*cos(lat2*pi/180)*sin(lon2*pi/180)+sin(lat1*pi/180)*sin(lat2*pi/180))
    dalfa=alfa/N

xc[N+1],yc[N+1]=m(loncv[N+1],latcv[N+1])

for i in range(N+1):
    if fabs(lon2-lon1)<180:

        if lon2>lon1:#lon1->lon2.
            latcv[i+1]=atan((A*cos((lon1+(i+1)*dlam)*pi/180)+B*sin((lon1+(i+1)*dlam)*pi/180))/(-C))*(180/pi)
            loncv[i+1]=lon1+(i+1)*dlam
        if lon2<lon1:#lon2->lon1.
            latcv[i+1]=atan((A*cos((lon2+(i+1)*dlam)*pi/180)+B*sin((lon2+(i+1)*dlam)*pi/180))/(-C))*(180/pi)
            loncv[i+1]=lon2+(i+1)*dlam

    elif (lon2-lon1)<=-180:#lon1->lon2.

        if lon1+(i+1)*dlam<180:
            latcv[i+1]=atan((A*cos((lon1+(i+1)*dlam)*pi/180)+B*sin((lon1+(i+1)*dlam)*pi/180))/(-C))*(180/pi)
            loncv[i+1]=lon1+(i+1)*dlam
        if lon1+(i+1)*dlam>=180:
            latcv[i+1]=atan((A*cos((lon1-360+(i+1)*dlam)*pi/180)+B*sin((lon1-360+(i+1)*dlam)*pi/180))/(-C))*(180/pi)
            loncv[i+1]=lon1-360+(i+1)*dlam
    elif (lon2-lon1)>=180:#lon2->lon1.

        if lon2+(i+1)*dlam<=180:
            latcv[i+1]=atan((A*cos((lon2+(i+1)*dlam)*pi/180)+B*sin((lon2+(i+1)*dlam)*pi/180))/(-C))*(180/pi)
            loncv[i+1]=lon2+(i+1)*dlam
        if lon2+(i+1)*dlam>=180:
            latcv[i+1]=atan((A*cos((lon2-360+(i+1)*dlam)*pi/180)+B*sin((lon2-360+(i+1)*dlam)*pi/180))/(-C))*(180/pi)
            loncv[i+1]=lon2+(i+1)*dlam-360
    xc[i],yc[i]=m(loncv[i],latcv[i])
#Caso de longitudes iguales.
if lon1==lon2:
	dfi=abs(lat2-lat1)/N
	for i in range(N+1):
		loncv[i]=lon1
		if lat1<lat2:		
			latcv[i]=lat1+i*dfi
		if lat1>lat2:
			latcv[i]=lat2+i*dfi
		xc[i],yc[i]=m(loncv[i],latcv[i])
for i in range (N+2):#Distancia para las gráficas.
	d[i]=6371*dalfa*i
if lon1!=lon2:
	for i in range(N+1):#Cálculo del rumbo en cada punto en la ortodrómica para la gráfica rumbo-distancia.
		i=i+1 
	
		thetaorto[i-1]=(180/pi)*atan2(sin(loncv[i]*pi/180-loncv[i-1]*pi/180)*cos(latcv[i]*pi/180),cos(latcv[i-1]*pi/180)*sin(latcv[i]*pi/180)-sin(latcv[i-1]*pi/180)*cos(latcv[i]*pi/180)*cos(loncv[i]*pi/180-loncv[i-1]*pi/180))
	thetaorto[N+1]=(180/pi)*atan2(sin(loncv[N+1]*pi/180-loncv[N]*pi/180)*cos(latcv[N+1]*pi/180), cos(latcv[N]*pi/180)*sin(latcv[N+1]*pi/180)-sin(latcv[N]*pi/180)*cos(latcv[N+1]*pi/180)*cos(loncv[N+1]*pi/180-loncv[N]*pi/180))
if lon1==lon2:
	if lat2>lat1:
		for i in range(N+1):
			i=i+1
			thetaorto[i-1]=0
		thetaorto[N+1]=0
	if lat2<lat1:
		for i in range(N+1):
			i=i+1
			thetaorto[i-1]=180
		thetaorto[N+1]=180
for i in range(N+1):
    x180,y180=m(180,latcv[i])#Para los segmentos que por el salto de coordenadas no se dibujan. Punto en longitud 180º.
    xm180,ym180=m(-180,latcv[i])#Para los segmentos que por el salto de coordenadas no se dibujan. Punto en longitud -180º.
    i=i+1
    if loncv[i]<-100 and loncv[i-1]>160:
        m.plot([xc[i-1],x180], [yc[i-1],yc[i]],'b-')#Dibuja los puntos que faltan por el salto.
        m.plot([xc[i],xm180], [yc[i],yc[i-1]],'b-')
    elif loncv[i-1]<-100 and loncv[i]>160:
        m.plot([xc[i-1],xm180], [yc[i-1],yc[i]],'b-')#Dibuja los puntos que faltan por el salto.
        m.plot([xc[i],x180], [yc[i],yc[i+1]],'b-')
    else:
        m.plot([xc[i-1],xc[i]], [yc[i-1],yc[i]],'b-')#Dibuja todos los puntos.

#----------------------------------------------
#Este es un vector para hacer luego las gráficas lon-distancia y lat-distancia en la ortodrómica. Las gráficas están abajo del todo. Tienen que estar ahí para que aparezca la gráfica después del mapa.
loncvorto=loncv
latcvorto=latcv
#----------------------------------------------
#Loxodrómica.

#Cálculo del rumbo theta.
#Alfa es el ángulo entre ra y rb.

alfa=acos(cos(lat1*pi/180)*cos(lon1*pi/180)*cos((lat2+dlam)*pi/180)*cos(lon2*pi/180)+cos(lat1*pi/180)*sin(lon1*pi/180)*cos(lat2*pi/180)*sin(lon2*pi/180)+sin(lat1*pi/180)*sin(lat2*pi/180))
dalfa=alfa/N

if lat2!=lat1:
	if fabs(lon2-lon1)<180: #Cálculo del rumbo theta. Calculo aparte el término del logaritmo neperiano (thetaln).
		if lon2>lon1:
			thetaln=log(tan(pi/4+lat1*pi/360)/tan(pi/4+lat2*pi/360))
			theta=atan(((lon1-lon2)*pi/180)/thetaln)#lon1->lon2.
		if lon2<lon1:
			thetaln=log(tan(pi/4+lat2*pi/360)/tan(pi/4+lat1*pi/360))
			theta=atan(((lon2-lon1)*pi/180)/thetaln)#lon2->lon1.
	elif (lon2-lon1)<=-180:#lon1->lon2.
		thetaln=log(tan(pi/4+lat2*pi/360)/tan(pi/4+lat1*pi/360))
		theta=atan(((360-(lon1-lon2))*pi/180)/thetaln)
	elif (lon2-lon1)>=180:#lon2->lon1.
		thetaln=log(tan(pi/4+lat1*pi/360)/tan(pi/4+lat2*pi/360))
		theta=atan(((360-(lon2-lon1))*pi/180)/thetaln)
		
    #Calculamos los puntos intermedios C.

	loncv=np.zeros(N+2)
	latcv=np.zeros(N+2)
	xc=np.zeros(N+2)
	yc=np.zeros(N+2)

	if fabs(lon2-lon1)<180:#Pone el último punto del vector lat/lon.
		if lon2>lon1:
			latcv[N+1]=lat2
			loncv[N+1]=lon2
		if lon2<lon1:
			latcv[N+1]=lat1
			loncv[N+1]=lon1
	elif (lon2-lon1)<=-180:#lon1->lon2.
		latcv[N+1]=lat2
		loncv[N+1]=lon2
	elif (lon2-lon1)>=180:#lon2->lon1.
		latcv[N+1]=lat1
		loncv[N+1]=lon1
	xc[N+1],yc[N+1]=m(loncv[N+1],latcv[N+1])

	for i in range(N+1):
		if fabs(lon2-lon1)<180:
			if lon2<lon1:#Punto A es el punto 2.
				latcv[i]=90-(360/pi)*atan(tan(pi/4-lat2*pi/360)/exp((i*dlam*pi/180)/tan(theta)))
				loncv[i]=lon2+i*dlam
			if lon2>lon1:#Punto A es el punto 1.
				latcv[i]=90-(360/pi)*atan(tan(pi/4-lat1*pi/360)/exp((i*dlam*pi/180)/tan(theta)))
				loncv[i]=lon1+i*dlam
		elif (lon2-lon1)<=-180:#lon1->lon2 Punto A es el punto 1.
			if (lon1+i*dlam)<180:
				latcv[i]=90-(360/pi)*atan(tan(pi/4-lat1*pi/360)/exp((i*dlam*pi/180)/tan(theta)))
				loncv[i]=lon1+i*dlam
			if (lon1+i*dlam)>=180:
				latcv[i]=90-(360/pi)*atan(tan(pi/4-lat1*pi/360)/exp((i*dlam*pi/180)/tan(theta)))
				loncv[i]=lon1-360+i*dlam
       
		elif (lon2-lon1)>=180:#lon2->lon1 Punto A es el punto 2.
			if (lon2+i*dlam)<180:
				latcv[i]=90-(360/pi)*atan(tan(pi/4-lat2*pi/360)/exp((i*dlam*pi/180)/tan(theta)))
				loncv[i]=lon2+i*dlam
			if (lon2+i*dlam)>=180:
				latcv[i]=90-(360/pi)*atan(tan(pi/4-lat2*pi/360)/exp((i*dlam*pi/180)/tan(theta)))
				loncv[i]=lon2+i*dlam-360
		xc[i],yc[i]=m(loncv[i],latcv[i])

	for i in range(N+1):
		x180,y180=m(180,latcv[i])#Para los segmentos que por el salto de coordenadas no se dibujan. Punto en longitud 180º.
		xm180,ym180=m(-180,latcv[i])#Para los segmentos que por el salto de coordenadas no se dibujan. Punto en longitud -180º.
		i=i+1
		if loncv[i]<-100 and loncv[i-1]>160:
			m.plot([xc[i-1],x180], [yc[i-1],yc[i]],'m-')#Dibuja los puntos que faltan por el salto.
			m.plot([xc[i],xm180], [yc[i],yc[i-1]],'m-')

		elif loncv[i-1]<-100 and loncv[i]>160:
			m.plot([xc[i-1],xm180], [yc[i-1],yc[i]],'m-')#Dibuja los puntos que faltan por el salto.
			m.plot([xc[i],x180], [yc[i],yc[i+1]],'m-')

		else:
			m.plot([xc[i-1],xc[i]], [yc[i-1],yc[i]],'m-')#Dibuja todos los puntos.
#Caso en el que las latitudes son iguales.
if lat2==lat1:
    xc=np.zeros(N+2)
    yc=np.zeros(N+2)
    if fabs(lon2-lon1)<=180:
        if lon2<lon1:
            loncv[N+1]=lon1
        if lon2>lon1:
            loncv[N+1]=lon2
    elif (lon2-lon1)<=-180:#lon1->lon2 Punto A es el punto 1.
        loncv[N+1]=lon2
    elif (lon2-lon1)>=180:#lon2->lon1 Punto A es el punto 2.
        loncv[N+1]=lon1
   
    xc[N+1],yc[N+1]=m(loncv[N+1],lat1)
    for i in range(N+1):
        latcv[i]=lat1
        if fabs(lon2-lon1)<=180:
            if lon2<lon1:
                loncv[i]=lon2+i*dlam
            if lon2>lon1:
                loncv[i]=lon1+i*dlam
        elif (lon2-lon1)<=-180:#lon1->lon2 Punto A es el punto 1.
            if (lon1+i*dlam)<=180:
                loncv[i]=lon1+i*dlam
            if (lon1+i*dlam)>=180:
                loncv[i]=lon1-360+i*dlam
       
        elif (lon2-lon1)>=180:#lon2->lon1 Punto A es el punto 2.
            if (lon2+i*dlam)<=180:
                loncv[i]=lon2+i*dlam
            if (lon2+i*dlam)>=180:
                loncv[i]=lon2+i*dlam-360
        x180,y180=m(180,lat1)#Para los segmentos que por el salto de coordenadas no se dibujan. Punto en longitud 180º.
        xm180,ym180=m(-180,lat1)#Para los segmentos que por el salto de coordenadas no se dibujan. Punto en longitud -180º.
       
        xc[i],yc[i]=m(loncv[i],latcv[i])
    for i in range(N+1):
        i=i+1
        if loncv[i]<-100 and loncv[i-1]>150:
            m.plot([xc[i-1],x180], [yc[i-1],y180],'m-')#Dibuja los puntos que faltan por el salto.
            m.plot([xc[i],xm180], [yc[i],yc[i-1]],'m-')

        elif loncv[i-1]<-100 and loncv[i]>150:
            m.plot([xc[i-1],xm180], [yc[i-1],ym180],'m-')#Dibuja los puntos que faltan por el salto.
            m.plot([xc[i],x180], [yc[i],yc[i+1]],'m-')

        else:
            m.plot([xc[i-1],xc[i]], [yc[i-1],yc[i]],'m-')#Dibuja todos los puntos.
if lon1==lon2:
	dfi=abs(lat2-lat1)/N
	for i in range(N+1):
		loncv[i]=lon1
		if lat1<lat2:		
			latcv[i]=lat1+i*dfi
		if lat1>lat2:
			latcv[i]=lat2+i*dfi
		xc[i],yc[i]=m(loncv[i],latcv[i])
	
plt.show()
#----------------------------------------------
#Gráficas distancia-rumbo, distancia-latitud, distancia-longitud.
grafica=plt.plot(d,thetaorto, 'r-', d, loncvorto, 'g-', d, latcvorto, 'b-')
plt.title(u"Distancia (km)-Latitud (azul), longitud (verde), rumbo (rojo) (º)")# PMG: Añado la "u" para que matplotlib no se queje de que no entiende las tildes
plt.show(grafica)
#----------------------------------------------

