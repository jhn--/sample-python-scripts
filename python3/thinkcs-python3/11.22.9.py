'''
11.22.9
Describe the relationship between " ".join(song.split()) and song in the fragment of code below. Are they the same for all strings assigned to song? When would they be different?
'''

def aweg():
    song = "The rain in Spain..."
    print(song.split())
    print(" ".join(song.split()))

aweg()