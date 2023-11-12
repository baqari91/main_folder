def change(b,c,d):
    def a(x):
        return b(c(d(x)))
    return a
def wami2wuti(dist):
    return dist*60
def wuti2saati(dist):
    return dist * 24
transform = change(wami2wuti,wami2wuti,wuti2saati)
e=transform(0.5)
print(e)