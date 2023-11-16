
class Human:
    height = 170
    weight = 70
    def __init__(self, name):
        self.name = name
        #print('init')

    def sleep(self):
        print('Self is sleeping')



class Georgian(Human):
    location = 'Kavkasia'

    def tamadoba(self):
        print('Sadgegrdzelo')


geo = Georgian('Dato')
geo.tamadoba()
Human.sleep(geo)