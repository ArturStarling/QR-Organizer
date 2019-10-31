from kivy.storage.jsonstore import JsonStore
import cv2
store = JsonStore('hello.json')

# put some values
store.put('tito', name='Mathieu', org='kivy', age=30, height=1.80, estate='São Paulo', country='Brasil')
store.put('tshirtman', name='Gabriel', age=27)
store.put('resistor', armario='armário 1', gaveta='gaveta 4', lugar='do lado da caixa laranja', imagem='miseravel.jpg')

# using the same index key erases all previously added key-value pairs
#store.put('tito', name='Adriel', age=10)

# get a value using a index key and key
#print('tito is', store.get('tito')['name'])
#print('tito is', store.get('tito')['org'])
#print('tito is', store.get('tito')['age'])
#print('tito is', store.get('tito')['height'])
#print('tito is', store.get('tito')['estate'])
#print('tito is', store.get('tito')['country'])
print('o objeto está no', store.get('resistor')['armario'], store.get('resistor')['gaveta'], store.get('resistor')['lugar'])
image = cv2.imread(store.get('resistor')['imagem'])
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# or guess the key/entry for a part of the key
#for item in store.find(name='Gabriel'):
    #print('tshirtmans index key is', item[0])
    #print('his key value pairs are', str(item[1]))

#for item in store.find(name='Mathieu'):
    #print('tshirtmans index key is', item[0])
    #print('his key value pairs are', str(item[1]))
