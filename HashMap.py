class HashMap:
    def __init__(self):
        self.size = 10
        #   ASSIGNING NONE FOR EACH VALUE IN ARRAY
        #   USING CHAINING METHOD TO HANDLE COLLISION
        # self.arr = [None for i in range(self.size)]
        # CREATING AN ARRAY INSIDE AN ARRAY FOR STORING MORE VALUES IN ONE INDEX TO AVOID COLLISION
        self.arr = [[] for i in range(self.size)]

    def hashfunc(self,key):
        #   USING ASCII FOR THE HASH FUNCTION
        d = 0
        for character in key:
            #   ORD() GIVES THE ASCII VALUE FOR EACH CHARACTER
            #   GETTING THE SUMMATION OF EACH VALUE
            d += ord(character)
        return d%self.size

    #   def add(self,key,val):
    #   INORDER TO MAKE THE ACCESING AND ADDING ITEM AS DICTIONARY WE USED THE INBUILT OPERATOR
    #   i.e __setitem__ and __getitem__
    def __setitem__(self, key, val):
        hf_indx = self.hashfunc(key)         # hf GIVES THE INDEX WHERE TO BE STORED
        found = False
        for indx, element in enumerate(self.arr[hf_indx]):
            if element[0] == key:
                self.arr[hf_indx][indx] = (key, val)
                found = True
        if not found:
            self.arr[hf_indx].append((key, val))

    # def get(self,key):
    def __getitem__(self, key):
        hf_indx = self.hashfunc(key)
        for element in self.arr[hf_indx]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        hf_indx = self.hashfunc(key)
        # ENUMERATE GIVES DATA A COUNT
        for indx,element in enumerate(self.arr[hf_indx]):
            if element[0] == key:
                print("\nDeleting {} data".format(element[0]))
                del self.arr[hf_indx][indx]

hm = HashMap()
# hm.add("march 6", 310)
# hm.add("march 7", 340)
# hm.add("march 9", 293)
# hm.get("march 9")
#   NOW IT IS ACTING MORE LIKE A DICTIONARY
hm["march 6"] = 310
hm["march 7"] = 340
hm["march 9"] = 293
hm["march 17"] = 300
hm["march 35"] = 600
print("Hash Table : ",hm.arr)
print("\nAccesing value of march 17 : ",hm["march 17"])
print("Accesing value of march 35 : ",hm["march 35"])
print("Accesing value of march 7 : ",hm["march 7"])
del hm["march 17"]
print("Hash Table after deletion : ",hm.arr)
