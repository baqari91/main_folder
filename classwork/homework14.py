#დავალება
#ლექსიკონების დახმარებით შექმენი პითონში პროგრამა, რომელიც წარგიდგენს რესტორნის მენიუს. მიიღებს შეკვეთას.
# შექმნის ფაილს და ჩაწერს შეკვეთასა და მის ღირებულებას. პროგრამა გადააქციე exe ფაილად და დაუყენე რესტორნის სურათი (აიქონი ico გაფართოების უნდა იყოს).





#shutil_ის მაგალითები


#1 ფაილების კოპირება საქაღალდიდან სხვა ლოკაციაზე ახალ საქაღალდეში
# import shutil
# src = "C:/Users/Nika/Desktop/source_files"
# dst = "C:/Users/Nika/Desktop/destination_files/everything"
#
# shutil.copytree(src=src, dst=dst)




#2 ცალკეული დოკუმენტის კოპირება არსებულ საქაღალდეში
# src = "C:/Users/Nika/Desktop/source_files"
# dst = "C:/Users/Nika/Desktop/destination_files"
#
# shutil.copy(src=src + "/alphabet.jpg", dst=dst)


#3 დოკუმენტის დაკოპირება და ახალი სახელით შენახვა მითითებულ ლოკაციაზე
# src = "C:/Users/Nika/Desktop/source_files"
# dst = "C:/Users/Nika/Desktop/destination_files"
#
# shutil.copyfile(src=src + "/alphabet.jpg", dst=dst + "/alphabet1.jpg")

#14.10 ფაილის გადატანა (დაუკოპირებლად)
# src = "C:/Users/Nika/Desktop/source_files"
# dst = "C:/Users/Nika/Desktop/destination_files"
# shutil.move(src=src + "/alphabet.jpg", dst=dst)

#14.11 საქაღალდის წაშლა
# src = "C:/Users/Nika/Desktop/source_files"
# shutil.rmtree(src + "/folder1")

#14.12 ფაილის წაშლა os მოდულის დახმარებით
# import os
# src = "C:/Users/Nika/Desktop/source_files"
# os.remove(src + "/alphabet.jpg")



#საკლასო პროექტი
# import shutil
# while True:
#     choice = input("""
#                 Choose:
#                 1 _ copy all files and folder in new folder
#                 2 _ remove folder
#                 3 _ end
#                 """)
#     if choice == "3":
#         print("Task Ended")
#         break
#
#     elif choice == "1":
#         src = input("Enter Source:")
#         dst = input("Enter Destination:") + "/just_created"
#         try:
#             shutil.copytree(src=src, dst=dst)
#         except:
#             print("Try was not successful...")
#
#     elif choice == "2":
#         src = input("Enter Path of File to Delete:")
#         try:
#             shutil.rmtree(src=src)
#         except:
#             print("Try was not successful...")

#exe ფაილად კოდის შენახვის საფეხურები
# pip install pyinstaller
# pyinstaller files.py --onefile
# pyinstaller -F -i "icon.ico" files.py