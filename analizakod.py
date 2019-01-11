import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
dane=pd.read_csv("weather.csv")


#print(dane.head(0))
#print(dane)


#ZADANIE1
#podział na miesiace danych z Auckland rok 2016
'''columns = ["city","date","year","month","day","high_temp","avg_temp","low_temp","high_dewpt","avg_dewpt","low_dewpt","high_humidity","avg_humidity","low_humidity","high_hg","avg_hg","low_hg","high_vis","avg_vis","low_vis","high_wind","avg_wind",]
df = pd.DataFrame(dane, columns=columns)
df1=df[df['city'].str.contains('Auckland', na = False)]
rok2016 =df1.loc[df1['year'] == 2016]
aucklandstyczen2016 =rok2016.loc[rok2016['month'] == 1]
aucklandluty2016 =rok2016.loc[rok2016['month'] == 2]
aucklandmarzec2016 =rok2016.loc[rok2016['month'] == 3]
aucklandkwiecień2016 =rok2016.loc[rok2016['month'] == 4]
aucklandmaj2016 =rok2016.loc[rok2016['month'] == 5]
aucklandczerwiec2016 =rok2016.loc[rok2016['month'] == 6]
aucklandlipiec2016 =rok2016.loc[rok2016['month'] == 7]
aucklandsierpien2016 =rok2016.loc[rok2016['month'] == 8]
aucklandwrzesien2016 =rok2016.loc[rok2016['month'] == 9]
aucklandpazdziernik2016 =rok2016.loc[rok2016['month'] == 10]
aucklandlistopad2016 =rok2016.loc[rok2016['month'] == 11]
aucklandgrudzien2016 =rok2016.loc[rok2016['month'] == 12]

#print(aucklandgrudzien2016)




#podział na miesiace danych z Auckland rok 2017
rok2017 =df1.loc[df1['year'] == 2017]
aucklandstyczen2017 =rok2017.loc[rok2017['month'] == 1]
aucklandluty2017 =rok2017.loc[rok2017['month'] == 2]
aucklandmarzec2017 =rok2017.loc[rok2017['month'] == 3]
aucklandkwiecień2017 =rok2017.loc[rok2017['month'] == 4]
aucklandmaj2017 =rok2017.loc[rok2017['month'] == 5]
aucklandczerwiec2017 =rok2017.loc[rok2017['month'] == 6]
aucklandlipiec2017 =rok2017.loc[rok2017['month'] == 7]
aucklandsierpien2017 =rok2017.loc[rok2017['month'] == 8]
aucklandwrzesien2017 =rok2017.loc[rok2017['month'] == 9]
aucklandpazdziernik2017 =rok2017.loc[rok2017['month'] == 10]
aucklandlistopad2017 =rok2017.loc[rok2017['month'] == 11]
aucklandgrudzien2017 =rok2017.loc[rok2017['month'] == 12]

#print(aucklandgrudzien2017)




#podział na miesiace danych z Mumbaju 2016
df2=df[df['city'].str.contains('Mumbai', na = False)]
rok2016 =df2.loc[df2['year'] == 2016]
mumbaistyczen2016 =rok2016.loc[rok2016['month'] == 1]
mumbailuty2016 =rok2016.loc[rok2016['month'] == 2]
mumbaimarzec2016 =rok2016.loc[rok2016['month'] == 3]
mumbaikwiecień2016 =rok2016.loc[rok2016['month'] == 4]
mumbaimaj2016 =rok2016.loc[rok2016['month'] == 5]
mumbaiczerwiec2016 =rok2016.loc[rok2016['month'] == 6]
mumbailipiec2016 =rok2016.loc[rok2016['month'] == 7]
mumbaisierpien2016 =rok2016.loc[rok2016['month'] == 8]
mumbaiwrzesien2016 =rok2016.loc[rok2016['month'] == 9]
mumbaipazdziernik2016 =rok2016.loc[rok2016['month'] == 10]
mumbailistopad2016 =rok2016.loc[rok2016['month'] == 11]
mumbaigrudzien2016 =rok2016.loc[rok2016['month'] == 12]

#print(mumbaigrudzien2016)


#podział na miesiace danych z Mumbaju 2017
rok2017 =df2.loc[df2['year'] == 2017]
mumbaistyczen2017 =rok2017.loc[rok2017['month'] == 1]
mumbailuty2017 =rok2017.loc[rok2017['month'] == 2]
mumbaimarzec2017 =rok2017.loc[rok2017['month'] == 3]
mumbaikwiecień2017 =rok2017.loc[rok2017['month'] == 4]
mumbaimaj2017 =rok2017.loc[rok2017['month'] == 5]
mumbaiczerwiec2017 =rok2017.loc[rok2017['month'] == 6]
mumbailipiec2017 =rok2017.loc[rok2017['month'] == 7]
mumbaisierpien2017 =rok2017.loc[rok2017['month'] == 8]
mumbaiwrzesien2017 =rok2017.loc[rok2017['month'] == 9]
mumbaipazdziernik2017 =rok2017.loc[rok2017['month'] == 10]
mumbailistopad2017 =rok2017.loc[rok2017['month'] == 11]
mumbaigrudzien2017 =rok2017.loc[rok2017['month'] == 12]

#print(mumbaigrudzien2017)


#podział na miesiące Bejing 2016
df3=df[df['city'].str.contains('Beijing', na = False)]
rok2016 =df3.loc[df3['year'] == 2016]
beijingstyczen2016 =rok2016.loc[rok2016['month'] == 1]
beijingluty2016 =rok2016.loc[rok2016['month'] == 2]
beijingmarzec2016 =rok2016.loc[rok2016['month'] == 3]
beijingkwiecień2016 =rok2016.loc[rok2016['month'] == 4]
beijingmaj2016 =rok2016.loc[rok2016['month'] == 5]
beijingczerwiec2016 =rok2016.loc[rok2016['month'] == 6]
beijinglipiec2016 =rok2016.loc[rok2016['month'] == 7]
beijingsierpien2016 =rok2016.loc[rok2016['month'] == 8]
beijingwrzesien2016 =rok2016.loc[rok2016['month'] == 9]
beijingpazdziernik2016 =rok2016.loc[rok2016['month'] == 10]
beijinglistopad2016 =rok2016.loc[rok2016['month'] == 11]
beijinggrudzien2016 =rok2016.loc[rok2016['month'] == 12]

#print(beijingmaj2016)




#podział na miesiące Bejing 2017
rok2017 =df3.loc[df3['year'] == 2017]
beijingstyczen2017 =rok2017.loc[rok2017['month'] == 1]
beijingluty2017 =rok2017.loc[rok2017['month'] == 2]
beijingmarzec2017 =rok2017.loc[rok2017['month'] == 3]
beijingkwiecień2017 =rok2017.loc[rok2017['month'] == 4]
beijingmaj2017 =rok2017.loc[rok2017['month'] == 5]
beijingczerwiec2017 =rok2017.loc[rok2017['month'] == 6]
beijinglipiec2017 =rok2017.loc[rok2017['month'] == 7]
beijingsierpien2017 =rok2017.loc[rok2017['month'] == 8]
beijingwrzesien2017 =rok2017.loc[rok2017['month'] == 9]
beijingpazdziernik2017 =rok2017.loc[rok2017['month'] == 10]
beijinglistopad2017 =rok2017.loc[rok2017['month'] == 11]
beijinggrudzien2017 =rok2017.loc[rok2017['month'] == 12]

#print(beijingmaj2017)






#podział na miesiące Chicago 2016
df4=df[df['city'].str.contains('Chicago', na = False)]
rok2016 =df4.loc[df4['year'] == 2016]
chicagostyczen2016 =rok2016.loc[rok2016['month'] == 1]
chicagoluty2016 =rok2016.loc[rok2016['month'] == 2]
chicagomarzec2016 =rok2016.loc[rok2016['month'] == 3]
chicagokwiecień2016 =rok2016.loc[rok2016['month'] == 4]
chicagomaj2016 =rok2016.loc[rok2016['month'] == 5]
chicagoczerwiec2016 =rok2016.loc[rok2016['month'] == 6]
chicagolipiec2016 =rok2016.loc[rok2016['month'] == 7]
chicagosierpien2016 =rok2016.loc[rok2016['month'] == 8]
chicagowrzesien2016 =rok2016.loc[rok2016['month'] == 9]
chicagopazdziernik2016 =rok2016.loc[rok2016['month'] == 10]
chicagolistopad2016 =rok2016.loc[rok2016['month'] == 11]
chicagogrudzien2016 =rok2016.loc[rok2016['month'] == 12]

#print(chicagogrudzien2016)




#podział na miesiące Chicago 2017
rok2017 =df4.loc[df4['year'] == 2017]
chicagostyczen2017 =rok2017.loc[rok2017['month'] == 1]
chicagoluty2017 =rok2017.loc[rok2017['month'] == 2]
chicagomarzec2017 =rok2017.loc[rok2017['month'] == 3]
chicagokwiecień2017 =rok2017.loc[rok2017['month'] == 4]
chicagomaj2017 =rok2017.loc[rok2017['month'] == 5]
chicagoczerwiec2017 =rok2017.loc[rok2017['month'] == 6]
chicagolipiec2017 =rok2017.loc[rok2017['month'] == 7]
chicagosierpien2017 =rok2017.loc[rok2017['month'] == 8]
chicagowrzesien2017 =rok2017.loc[rok2017['month'] == 9]
chicagopazdziernik2017 =rok2017.loc[rok2017['month'] == 10]
chicagolistopad2017 =rok2017.loc[rok2017['month'] == 11]
chicagogrudzien2017 =rok2017.loc[rok2017['month'] == 12]

#print(chicagogrudzien2017)




#podział na miesiące San Diego 2016
df4=df[df['city'].str.contains('San Diego', na = False)]
rok2016 =df4.loc[df4['year'] == 2016]
sandiegostyczen2016 =rok2016.loc[rok2016['month'] == 1]
sandiegoluty2016 =rok2016.loc[rok2016['month'] == 2]
sandiegomarzec2016 =rok2016.loc[rok2016['month'] == 3]
sandiegokwiecień2016 =rok2016.loc[rok2016['month'] == 4]
sandiegomaj2016 =rok2016.loc[rok2016['month'] == 5]
sandiegoczerwiec2016 =rok2016.loc[rok2016['month'] == 6]
sandiegolipiec2016 =rok2016.loc[rok2016['month'] == 7]
sandiegosierpien2016 =rok2016.loc[rok2016['month'] == 8]
sandiegowrzesien2016 =rok2016.loc[rok2016['month'] == 9]
sandiegopazdziernik2016 =rok2016.loc[rok2016['month'] == 10]
sandiegolistopad2016 =rok2016.loc[rok2016['month'] == 11]
sandiegogrudzien2016 =rok2016.loc[rok2016['month'] == 12]

#print(sandiegogrudzien2016)






#podział na miesiące San Diego 2017
rok2017 =df4.loc[df4['year'] == 2017]
sandiegostyczen2017 =rok2017.loc[rok2017['month'] == 1]
sandiegoluty2017 =rok2017.loc[rok2017['month'] == 2]
sandiegomarzec2017 =rok2017.loc[rok2017['month'] == 3]
sandiegokwiecień2017 =rok2017.loc[rok2017['month'] == 4]
sandiegomaj2017 =rok2017.loc[rok2017['month'] == 5]
sandiegoczerwiec2017 =rok2017.loc[rok2017['month'] == 6]
sandiegolipiec2017 =rok2017.loc[rok2017['month'] == 7]
sandiegosierpien2017 =rok2017.loc[rok2017['month'] == 8]
sandiegowrzesien2017 =rok2017.loc[rok2017['month'] == 9]
sandiegopazdziernik2017 =rok2017.loc[rok2017['month'] == 10]
sandiegolistopad2017 =rok2017.loc[rok2017['month'] == 11]
sandiegogrudzien2017 =rok2017.loc[rok2017['month'] == 12]

#print(sandiegogrudzien2017)'''




#urednienie danych dla miesiecyaucklandstyczen2016 =rok2016.loc[rok2016['month'] == 1]
'''print(aucklandstyczen2016.mean()) 
print(aucklandluty2016.mean()) 
print(aucklandmarzec2016.mean()) 
print(aucklandkwiecień2016.mean())  
print(aucklandmaj2016.mean())  
print(aucklandczerwiec2016.mean())  
print(aucklandlipiec2016.mean())  
print(aucklandsierpien2016.mean())  
print(aucklandwrzesien2016.mean())  
print(aucklandpazdziernik2016.mean())  
print(aucklandlistopad2016.mean())  
print(aucklandgrudzien2016.mean())'''


'''print(aucklandstyczen2017.mean()) 
print(aucklandluty2017.mean()) 
print(aucklandmarzec2017.mean()) 
print(aucklandkwiecień2017.mean())  
print(aucklandmaj2017.mean())  
print(aucklandczerwiec2017.mean())  
print(aucklandlipiec2017.mean())  
print(aucklandsierpien2017.mean())  
print(aucklandwrzesien2017.mean())  
print(aucklandpazdziernik2017.mean())  
print(aucklandlistopad2017.mean())  
print(aucklandgrudzien2017.mean())'''



'''print(mumbaistyczen2016.mean()) 
print(mumbailuty2016.mean()) 
print(mumbaimarzec2016.mean()) 
print(mumbaikwiecień2016.mean())  
print(mumbaimaj2016.mean())  
print(mumbaiczerwiec2016.mean())  
print(mumbailipiec2016.mean())  
print(mumbaisierpien2016.mean())  
print(mumbaiwrzesien2016.mean())  
print(mumbaipazdziernik2016.mean())  
print(mumbailistopad2016.mean())  
print(mumbaigrudzien2016.mean())'''



'''print(mumbaistyczen2017.mean()) 
print(mumbailuty2017.mean()) 
print(mumbaimarzec2017.mean()) 
print(mumbaikwiecień2017.mean())  
print(mumbaimaj2017.mean())  
print(mumbaiczerwiec2017.mean())  
print(mumbailipiec2017.mean())  
print(mumbaisierpien2017.mean())  
print(mumbaiwrzesien2017.mean())  
print(mumbaipazdziernik2017.mean())  
print(mumbailistopad2017.mean())  
print(mumbaigrudzien2017.mean())'''

'''
print(beijingstyczen2016.mean()) 
print(beijingluty2016.mean()) 
print(beijingmarzec2016.mean()) 
print(beijingkwiecień2016.mean())  
print(beijingmaj2016.mean())  
print(beijingczerwiec2016.mean())  
print(beijinglipiec2016.mean())  
print(beijingsierpien2016.mean())  
print(beijingwrzesien2016.mean())  
print(beijingpazdziernik2016.mean())  
print(beijinglistopad2016.mean())  
print(beijinggrudzien2016.mean())



print(beijingstyczen2017.mean()) 
print(beijingluty2017.mean()) 
print(beijingmarzec2017.mean()) 
print(beijingkwiecień2017.mean())  
print(beijingmaj2017.mean())  
print(beijingczerwiec2017.mean())  
print(beijinglipiec2017.mean())  
print(beijingsierpien2017.mean())  
print(beijingwrzesien2017.mean())  
print(beijingpazdziernik2017.mean())  
print(beijinglistopad2017.mean())  
print(beijinggrudzien2017.mean())



print(chicagostyczen2016.mean()) 
print(chicagoluty2016.mean()) 
print(chicagomarzec2016.mean()) 
print(chicagokwiecień2016.mean())  
print(chicagomaj2016.mean())  
print(chicagoczerwiec2016.mean())  
print(chicagolipiec2016.mean())  
print(chicagosierpien2016.mean())  
print(chicagowrzesien2016.mean())  
print(chicagopazdziernik2016.mean())  
print(chicagolistopad2016.mean())  
print(chicagogrudzien2016.mean())


print(chicagostyczen2017.mean()) 
print(chicagoluty2017.mean()) 
print(chicagomarzec2017.mean()) 
print(chicagokwiecień2017.mean())  
print(chicagomaj2017.mean())  
print(chicagoczerwiec2017.mean())  
print(chicagolipiec2017.mean())  
print(chicagosierpien2017.mean())  
print(chicagowrzesien2017.mean())  
print(chicagopazdziernik2017.mean())  
print(chicagolistopad2017.mean())  
print(chicagogrudzien2017.mean())




print(sandiegostyczen2016.mean()) 
print(sandiegoluty2016.mean()) 
print(sandiegomarzec2016.mean()) 
print(sandiegokwiecień2016.mean())  
print(sandiegomaj2016.mean())  
print(sandiegoczerwiec2016.mean())  
print(sandiegolipiec2016.mean())  
print(sandiegosierpien2016.mean())  
print(sandiegowrzesien2016.mean())  
print(sandiegopazdziernik2016.mean())  
print(sandiegolistopad2016.mean())  
print(sandiegogrudzien2016.mean())


print(sandiegostyczen2017.mean()) 
print(sandiegoluty2017.mean()) 
print(sandiegomarzec2017.mean()) 
print(sandiegokwiecień2017.mean())  
print(sandiegomaj2017.mean())  
print(sandiegoczerwiec2017.mean())  
print(sandiegolipiec2017.mean())  
print(sandiegosierpien2017.mean())  
print(sandiegowrzesien2017.mean())  
print(sandiegopazdziernik2017.mean())  
print(sandiegolistopad2017.mean())  
print(sandiegogrudzien2017.mean())'''





#ZADANIE 2
'''wilgotnosc = dane['avg_humidity']
print(wilgotnosc)

temperatura = dane['avg_temp']
print(temperatura)


print(st.pearsonr(wilgotnosc,temperatura))

#plt.plot(wilgotnosc, temperatura)
plt.title('Wykres wilgotnosci i temperatury')
plt.plot(wilgotnosc,label='wilgotnosc') 
plt.plot(temperatura,label='temperatura [°F]') 
plt.legend() 
plt.xlabel('Dzien') 
plt.ylabel('Wartosc') 
plt.show()'''



#ZADANIE3
#Srednia temperatura

'''columns = ["city","avg_temp","avg_vis"]
df = pd.DataFrame(dane, columns=columns)
Aucklandtemp=df[df['city'].str.contains('Auckland', na = False)]
sredniatempauckland = Aucklandtemp['avg_temp']
print(sredniatempauckland.mean())


columns = ["city","avg_temp","avg_vis"]
df = pd.DataFrame(dane, columns=columns)
Mumbaitemp=df[df['city'].str.contains('Mumbai', na = False)]
sredniatempmumbai = Mumbaitemp['avg_temp']
print(sredniatempmumbai.mean())


columns = ["city","avg_temp","avg_vis"]
df = pd.DataFrame(dane, columns=columns)
Beijingtemp=df[df['city'].str.contains('Beijing', na = False)]
sredniatempbeijing = Beijingtemp['avg_temp']
print(sredniatempbeijing.mean())


columns = ["city","avg_temp","avg_vis"]
df = pd.DataFrame(dane, columns=columns)
Chicagotemp=df[df['city'].str.contains('Chicago', na = False)]
sredniatempchicago = Chicagotemp['avg_temp']
print(sredniatempchicago.mean())



columns = ["city","avg_temp","avg_vis"]
df = pd.DataFrame(dane, columns=columns)
Sandiegotemp=df[df['city'].str.contains('San Diego', na = False)]
sredniatempsandiego = Sandiegotemp['avg_temp']
print(sredniatempsandiego.mean())

#Srednia widzialnoć
columns = ["city","avg_temp","avg_vis"]
df = pd.DataFrame(dane, columns=columns)
Aucklandvis=df[df['city'].str.contains('Auckland', na = False)]
sredniavisauckland = Aucklandvis['avg_vis']
print(sredniavisauckland.mean())


columns = ["city","avg_temp","avg_vis"]
df = pd.DataFrame(dane, columns=columns)
Mumbaitemp=df[df['city'].str.contains('Mumbai', na = False)]
sredniavismumbai = Mumbaitemp['avg_vis']
print(sredniavismumbai.mean())


columns = ["city","avg_temp","avg_vis"]
df = pd.DataFrame(dane, columns=columns)
Beijingvis=df[df['city'].str.contains('Beijing', na = False)]
sredniavisbeijing = Beijingvis['avg_vis']
print(sredniavisbeijing.mean())


columns = ["city","avg_temp","avg_vis"]
df = pd.DataFrame(dane, columns=columns)
Chicagovis=df[df['city'].str.contains('Chicago', na = False)]
sredniavischicago = Chicagovis['avg_temp']
print(sredniavischicago.mean())



columns = ["city","avg_temp","avg_vis"]
df = pd.DataFrame(dane, columns=columns)
Sandiegovis=df[df['city'].str.contains('San Diego', na = False)]
sredniavissandiego = Sandiegovis['avg_temp']
print(sredniavissandiego.mean())


n_groups = 5

average_temperature = (60.6, 80.9, 55.5, 52.7, 66.6)
#std_men = (5.9, 1.9, 4, 1, 2)

average_visibility = (5.9, 1.9, 7.3, 52.7, 66.6)
#std_women = (3, 5, 2, 3, 3)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, average_temperature, bar_width,
                alpha=opacity, color='b',
                 error_kw=error_config,
                label='Srednia temperatura [°F]')

rects2 = ax.bar(index + bar_width, average_visibility, bar_width,
                alpha=opacity, color='r',
                  error_kw=error_config,
                label='Widzialnosc')

ax.set_xlabel('Miasta')
ax.set_ylabel('Wartosci')
ax.set_title('Widzialnosc oraz temperatura w poszczegolnych miastach')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('Auckland', 'Mumbai', 'Beijing', 'Chicago', 'San_Diego'))
ax.legend()

fig.tight_layout()
plt.show()'''


#ZADANIE4
'''cisnienieatm = dane['avg_hg']
print(cisnienieatm)

miesiac = dane['month']
#print(miesiac)


plt.plot(miesiac, label ='miesiac')
plt.plot(cisnienieatm, label= "cisnienie atmosferyczne")
plt.title('Relacja cisnienia atmosferycznego i miesiąca')
plt.ylabel('cisnienie atmosferyczne')
plt.ylim(29,31)
plt.ylabel("Wartosc cisnienia atmosferycznego [Hg]")
plt.xlabel('miesiac')

plt.xlim(0.5,12.5)

plt.tight_layout()

plt.show()

#nie wiem czy ta korelacja jest tutaj poprawna raczej nie, wykres korelacji jeli jaka jest można opisać 
#z wykresu
print(st.spearmanr(miesiac,cisnienieatm))'''


#ZADANIE5
#srednia wilgotnosc w Auckland
'''columns = ["city","date","year","month","day","high_temp","avg_temp","low_temp","high_dewpt","avg_dewpt","low_dewpt","high_humidity","avg_humidity","low_humidity","high_hg","avg_hg","low_hg","high_vis","avg_vis","low_vis","high_wind","avg_wind",]
df = pd.DataFrame(dane, columns=columns)
Aucklandwilgotnosc=df[df['city'].str.contains('Auckland', na = False)]
sredniaaucklandwilgotnosc = Aucklandwilgotnosc['avg_humidity']
print(sredniaaucklandwilgotnosc.mean())

#srednia wilgotnosc w Mumbaju
columns = ["city","date","year","month","day","high_temp","avg_temp","low_temp","high_dewpt","avg_dewpt","low_dewpt","high_humidity","avg_humidity","low_humidity","high_hg","avg_hg","low_hg","high_vis","avg_vis","low_vis","high_wind","avg_wind",]
df = pd.DataFrame(dane, columns=columns)
Mumbaiwilgotnosc=df[df['city'].str.contains('Mumbai', na = False)]
sredniamumbaiwilgotnosc = Mumbaiwilgotnosc['avg_humidity']
print(sredniamumbaiwilgotnosc.mean())


print(st.ttest_ind(sredniaaucklandwilgotnosc,sredniamumbaiwilgotnosc))'''



#ZADANIE6
'''columns = ["city","date","year","month","day","high_temp","avg_temp","low_temp","high_dewpt","avg_dewpt","low_dewpt","high_humidity","avg_humidity","low_humidity","high_hg","avg_hg","low_hg","high_vis","avg_vis","low_vis","high_wind","avg_wind",]
df = pd.DataFrame(dane, columns=columns)
Chicagotemp=df[df['city'].str.contains('Chicago', na = False)]
sredniatempchicago = Chicagotemp['avg_temp']
print(sredniatempchicago.mean())


columns = ["city","date","year","month","day","high_temp","avg_temp","low_temp","high_dewpt","avg_dewpt","low_dewpt","high_humidity","avg_humidity","low_humidity","high_hg","avg_hg","low_hg","high_vis","avg_vis","low_vis","high_wind","avg_wind",]
df = pd.DataFrame(dane, columns=columns)
Sandiegotemp=df[df['city'].str.contains('San Diego', na = False)]
sredniatempsandiego = Sandiegotemp['avg_temp']
print(sredniatempsandiego.mean())

print(st.ttest_ind(sredniatempchicago,sredniatempsandiego))'''




#ZADANIE7
columns = ["city","date","year","month","day","high_temp","avg_temp","low_temp","high_dewpt","avg_dewpt","low_dewpt","high_humidity","avg_humidity","low_humidity","high_hg","avg_hg","low_hg","high_vis","avg_vis","low_vis","high_wind","avg_wind",]
df = pd.DataFrame(dane, columns=columns)
df1=df[df['city'].str.contains('Auckland', na = False)]
rok2016 =df1.loc[df1['year'] == 2016]
aucklandstyczen2016 =rok2016.loc[rok2016['month'] == 1]
aucklandluty2016 =rok2016.loc[rok2016['month'] == 2]
aucklandmarzec2016 =rok2016.loc[rok2016['month'] == 3]
aucklandkwiecień2016 =rok2016.loc[rok2016['month'] == 4]
aucklandmaj2016 =rok2016.loc[rok2016['month'] == 5]
aucklandczerwiec2016 =rok2016.loc[rok2016['month'] == 6]
aucklandlipiec2016 =rok2016.loc[rok2016['month'] == 7]
aucklandsierpien2016 =rok2016.loc[rok2016['month'] == 8]
aucklandwrzesien2016 =rok2016.loc[rok2016['month'] == 9]
aucklandpazdziernik2016 =rok2016.loc[rok2016['month'] == 10]
aucklandlistopad2016 =rok2016.loc[rok2016['month'] == 11]
aucklandgrudzien2016 =rok2016.loc[rok2016['month'] == 12]


aucklandstyczen2016sredniatemp = aucklandstyczen2016['avg_temp']
aucklandluty2016sredniatemp =aucklandluty2016['avg_temp']
aucklandmarzec2016sredniatemp =aucklandmarzec2016['avg_temp']
aucklandkwiecień2016sredniatemp =aucklandkwiecień2016['avg_temp']
aucklandmaj2016sredniatemp =aucklandmaj2016['avg_temp']
aucklandczerwiec2016sredniatemp =aucklandczerwiec2016['avg_temp']
aucklandlipiec2016sredniatemp =aucklandlipiec2016['avg_temp']
aucklandsierpien2016sredniatemp =aucklandsierpien2016['avg_temp']
aucklandwrzesien2016sredniatemp =aucklandwrzesien2016['avg_temp']
aucklandpazdziernik2016sredniatemp =aucklandpazdziernik2016['avg_temp']
aucklandlistopad2016sredniatemp =aucklandlistopad2016['avg_temp']
aucklandgrudzien2016sredniatemp =aucklandgrudzien2016['avg_temp']

print(aucklandstyczen2016sredniatemp.mean())
print(aucklandluty2016sredniatemp.mean())
print(aucklandmarzec2016sredniatemp.mean())
print(aucklandkwiecień2016sredniatemp.mean())
print(aucklandmaj2016sredniatemp.mean())
print(aucklandczerwiec2016sredniatemp.mean())
print(aucklandlipiec2016sredniatemp.mean())
print(aucklandsierpien2016sredniatemp.mean())
print(aucklandwrzesien2016sredniatemp.mean())
print(aucklandpazdziernik2016sredniatemp.mean())
print(aucklandlistopad2016sredniatemp.mean())
print(aucklandgrudzien2016sredniatemp.mean())


#kod wykresu
#1 to styczen , 12 grudzien
objects = ('1', '2', '3', '4', '5', '6','7' , '8','9', '10','11','12')
y_pos = np.arange(len(objects))
performance = [68.8,70.5,67.6,62.8,60.9,54.7,52.8,52.1,56.1,58.3,60.9,63.5]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Temperatura [°F]')
plt.title('Wykres rednich temperatur w poszczególnych miesiącach')
 
plt.show()














