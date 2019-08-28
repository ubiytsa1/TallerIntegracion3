import urllib2

pagina = urllib2.urlopen("http://opendata.camara.cl/wscamaradiputados.asmx/getLegislaturas")
html = pagina.read()

file_name = 'legislaturas.xml'
f = open(file_name, 'w+')
f.write(html)
f.close()