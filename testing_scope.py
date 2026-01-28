#testing_scope,py
m=17
def enclose():
    m=13
    def testing():
        print("m lokal: ",m)
    testing()

enclose()
print("m global: ",m)