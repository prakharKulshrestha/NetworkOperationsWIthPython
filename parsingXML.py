import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Prakhar</name>
  <phone type="intl">
    +1 XXX XXX XXXX
  </phone>
  <email hide="No" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

data1 = '''
<stuff>
  <persons>
    <person>
  	  <name>Prakhar</name>
  	  <phone type="intl">
       	+1 XXX XXX XXXX
  	  </phone>
  	  <email hide="No" />
    </person>
    <person>
  	  <name>Raj</name>
  	  <phone type="intl">
    	+1 XXX XXX XXXX
  	  </phone>
  	  <email hide="Yes" />
    </person>
  </persons>
</stuff>'''

tree1 = ET.fromstring(data1)
lst = tree1.findall('persons/person')
print ("Length is ",len(lst))
for item in lst:
	print("Name is ", item.find('name').text)
	print("Phone is ", item.find('phone').text)
	print("Email is ", item.find('email').get('hide'))