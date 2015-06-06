my_dict = {
	"Name": "John Hoe",
	"Age":	32,
	"Alive": True
}

print my_dict
print my_dict.items()
print my_dict.keys()
print my_dict.values()

for key in my_dict:
	print key, my_dict[key]