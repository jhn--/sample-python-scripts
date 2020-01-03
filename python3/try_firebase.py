from firebase import firebase
firebase = firebase.FirebaseApplication('https://prologue.firebaseio.com', None)
result = firebase.get('/bookmarks', None)
#print(result)

#data = {'Systems Performance: Enterprise and the Cloud: Brendan Gregg: 9780133390094: Amazoncom: Books': "http://www.amazon.com/gp/product/0133390098/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=0133390098&linkCode=as2&tag=deirdrestraug-20"}
#data = {'hello': "world"}

#result = firebase.post('/bookmarks', data)
#result = firebase.get('/bookmarks', None)
result = firebase.delete('/bookmarks/', '-JsJnm7ww58SLOSufX_e')
print(result)