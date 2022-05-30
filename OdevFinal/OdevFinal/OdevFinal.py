#Gerekli kutuphaneleri ekledim 
import os #baska programlari calistirabilmemizi saglayan kutuphane
from xml.dom.minidom import Element #xml dosyasini ayristirmak icin kullandim
import xmltodict#XML'i JSON'a Donusturmemizi saglayan kutuphane 
import json #json bicimli verilerle islemler yapmamizi saglayan kutuphane.

print("\n Web Aciklarinin Olup Olmadigini Gosteren Uygulama \n")

Data=[] #Data dizisi icerisinde XML'den alınan verileri tutar 

cikis_Yap ='out'#Uygulamadan Cikis Yapmak Icin Bir Degisken Tanimladim. 

while True: #Sonsuz Dongu Olusturdum Konsoldan out Yazılana Kadar Program Calisir.
 
 #Degerlerin Kullanicidan Girdirmesi Istendi
 Port = input("\n Portu Degerini Giriniz : ")#80
 address = input(" Web Sitesi Adresinin Degerini Giriniz : ")#testphp.vulnweb.com
 script = input(" Scripti Degerini Giriniz : ")#http-sql-injection

 #Girilen Degerlerin Ciktisi
 print("\n Girilen Port Degeri : "+Port)
 print(" Girilen Web Sitesi Adresinin Degeri : "+address)
 print(" Girilen Scripti Degeri : "+script)

 #Istege Göre Uygulamayi Sonlandirmak Icin Bir Kontrol Paneli Olusturdum. 
 cikis_Yap = input("\n Programdan Cikis Yapmak Istiyorsaniz 'out' Yaziniz. Devam Etmek Icin 'ENTER TUSUNA BASINIZ !!!' \n")
 if (cikis_Yap == "out"):
     print(" Programdan Cikis Yaptiniz.")
     break#Uygulamadan Cikmak Icin out yazmaniz yeterli olacaktir.
 print(" Isleminiz Yapiliyor. Lutfen Bekleyiniz....")#Eger Uygulamadan Cikmak Istemediginiz de Isleminizin Devam Ettigini Gosterir

 XML_cikti= "C:\\Windows\\Temp\\Cikti.xml"#Belirtilen Dosya Yoluna Cikti Verir
 nmapExe = "nmap " + "-p " + Port + " -oX " + XML_cikti + " --script " + script + " " + address#Kodlar Duzenlenir 
 os.system(nmapExe)#Yukarıdaki satirda belirttilen degerler Nmap.exe ile calistirilir

 dosya = open("C:\\Windows\\Temp\\Cikti.xml") #Belirtilen Dosya Yolundaki Dosyayı Acar
 xmlDosya_Icerik = dosya.read()#XML dosyasi icerigini okuma islemi yapar.
 dosya.close()#Dosya Kapatilir. Dosya artik okunmaz.
 nmapExe_cikti = xmltodict.parse(xmlDosya_Icerik)
 urls = nmapExe_cikti["nmaprun"]["host"]["ports"]["port"]["script"]["@output"].replace("/n","").replace("\n","")
 Data.append(nmapExe)
 Data.append(urls[urls.index("http")::].split("    "))
 jsonVeri = json.dumps(Data)#json'a donusturme
 newLineJson=json.loads(jsonVeri)#json dizisini ayristirdim

 print(json.dumps(newLineJson,indent=4,sort_keys=True))#Kodların düzenli gozukmesini saglar
 #Istege Göre Uygulamayi Sonlandirmak Icin Bir Kontrol Paneli Olusturdum. 
 print("\n Islem Basarili Bir Sekilde Tamamlandi.")
 cikis_Yap = input(" Programdan Cikis Yapmak Istiyorsaniz 'out' Yaziniz. Devam Etmek Icin '2 KERE ENTER TUSUNA BASINIZ !!!' \n")
 if (cikis_Yap == "out"):
  print(" Programdan Cikis Yaptiniz.")
  break#Uygulamadan Cikmak Icin out yazmaniz yeterli olacaktir.
 os.system("pause");# .exe Dosyasinin Kapanmamasi Icin Yazilan Kod
