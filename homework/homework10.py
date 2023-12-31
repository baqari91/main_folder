from random import randint
def list_generator(n):
    random_li = []
    for _ in range(n):
        random_li.append(randint(1,100))
    return random_li

arr = list_generator(20)
print(len(arr))
def heapify(arr, n, i): 
    largest = i  # ცვლალი რომელსაც სამეულის შედარებებისგან ქვევით მიენიჭება ყველაზე მაღალი მნიშვნელობა (დედა)
    left = 2 * i + 1 # 2*i+1 ფორმულა განსაზღვრავს მარცხენა შვილის მდებარეობას.(მარცხენა შვილი)
    right = 2 * i + 2 # 2*i+2 left-ის შემდეგი წევრი რომელიც იქნება (მარჯვენა შვილი) 
    # თუ მარცხენა შვილი ნაკლებია მასივის სიგრძეზე და ამავდროულად მარცხენა ინდექსის მნიშვნელობა მეტია მოცემულ ლარჯესტზე რომელსაც მინიჭებული აქვს i დან მიღებული არგუმენტი, მაშინ ეს მნიშვნელობა გახდეს ლარჯესტი(დედა) 
    if left < n and arr[left] > arr[largest]:
        largest = left
        
    # ----- და თუ მარჯვენა მხარე მეტია ლარჯესტზე რომელსაც მინიჭებული ექნება ახალი მნიშვნელობა თუ მარცხენა შვილი მეტი იყო პირველ მნიშვნელობაზე თუ არა ესეიგი i იყო უფრო მაღალი
    if right < n and arr[right] > arr[largest]:
        largest = right

    # შევცვალოთ დედა თუ საჭიროა
    if largest != i: # თუ ლარჯესტი ისევ იგივეა როცა i დან მიენიჭა მნიშვნელობა ესეიგი ყველაფერი კარგადაა და ქვედა კოდი არ გაეშვება, ხოლო თუ ლარჯესტი შეიცვალა და ინდექსები არ ემთხვევა ერთმანეთს მაშინ მოხდეს გადანაცვლება
        # ეს პირობა (largest != i)  ასევე აჩერებს რეკურსიას. იმ შემთხვევაში თუ არაის სიგრძე არ ყოფნის 
        arr[i], arr[largest] = arr[largest], arr[i]  # არაის i ინდექსის მნიშვნელობა და ლარჯესტის მნიშვნელობამ შეცვალონ ადგილები
        heapify(arr, n, largest) # აქ ლარჯესტი არის ინდექსი რომლიდანაც გადავიდა მაღალი ციფრი i ინდექსზე, რადგან ამ ინდექსზე არის უკვე დაბალი რიცხვი რეკურსია დაიწყებს ამ რიცხვის შედარებას და გადანაცვლებას იგივე ფორმულირებით


def heap_sort(arr):
    n = len(arr)     #არაის სიგრძე

    # ეს ლუპი აშენებს პირამიდას, დასრულების შემდეგ ყველა სამეულის (დედა) იქნება სამეულში ყველაზე მაღალი და მთლიანი პირამიდის თავში იქნება ყველაზე მაღალი მნიშვნელობა მთლიანი ლისტიდან
    for i in range(n // 2 - 1, -1, -1): # i დარბის მასივის შუის ბოლო ინდექსიდან დასაწყისისკენ, უკუსვლით. ყოველ ჯერზე ეშვება ფუნქცია სადაც i ხდება ლარჯესტი 
        heapify(arr, n, i) 

    # დასორტირება მთლიანად. დაიწყებს დიდი პირამიდის წვეტს გადაიტანს ბოლოში, შემდეგ იპოვის ახალ პირამიდის წევრს და იმასაც გადაიტანს ბოლოში, სანამ მთლიანად არ დასორტირდება
    for i in range(n - 1, 0, -1):  # i დარბის არაის სიგრძეში ბოლოდან დასაწყისამდე, i იღებს ინდექსის ნომერს ყოველ შემდეგ ჯერზე პატარავდება 1-ით
        arr[i], arr[0] = arr[0], arr[i]  # პირამიდის წვეტი და არაის ბოლო წევრი წვლიან ადგილებს
        heapify(arr, i, 0) # აქ i არგუმენტი გადაეცემა heapify ფუნქციის n პარამეტრს და ამის საშუალებით ფუნქცია ყოველ შემდეგ ჯერზე სორტირებას აკეთებს გადანაცვლებულ ინდექსამდე.  

#რეთურნი აღარ არის საჭირო რადგან პირდაპირ აკეთებს არაის ცვლილებას
heap_sort(arr)
print(arr)