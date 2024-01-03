import time
import concurrent.futures
import requests

# # დავალება 1

# def find_odd():
#     odd_numbers = []
#     for i in range(30, 51):
#         if i % 2 == 0:
#             odd_numbers.append(i)
#     return f"odd numbers: {odd_numbers}"
#
#
#
# def find_even():
#     even_numbers = []
#     for i in range(30, 51):
#         if i % 2 == 1:
#             even_numbers.append(i)
#     return f"even numbers: {even_numbers}"
#
#
# start = time.time()
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(find_odd)
#     f2 = executor.submit(find_even)
#     print(f1.result())
#     print(f2.result())
# end = time.time()
#
# print(f"\nFinished in {end - start} seconds...")

# დავალება 2

mp3_url = [
    'https://dl.vgmdownloads.com/soundtracks/geometry-dash/nqcdvyhoys/1-01.%20Main%20Menu.mp3',
    'https://dl.vgmdownloads.com/soundtracks/geometry-dash/deruvmukzk/1-02.%20Stereo%20Madness.mp3',
    'https://dl.vgmdownloads.com/soundtracks/geometry-dash/eejwddhnzf/1-03.%20Back%20On%20Track.mp3',
    'https://dl.vgmdownloads.com/soundtracks/geometry-dash/urgquwlmhi/1-04.%20Polargeist.mp3',
    'https://dl.vgmdownloads.com/soundtracks/geometry-dash/xcndggntbg/1-05.%20Dry%20Out.mp3'
]


def download(url):
    mp3_bytes = requests.get(url).content
    mp3_name = url.split('%')[-1]
    with open(mp3_name, 'wb') as mp3_file:
        mp3_file.write(mp3_bytes)
        print(mp3_name, 'downloaded')


start = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download, mp3_url)
end = time.time()
print(f"\nFinished in {end - start} seconds...")

# #მულტიპროცესინგისთვის დასატესტად
# if __name__ == '__main__':
#     start = time.time()
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         executor.map(download, mp3_url)
#     end = time.time()
#     print(f"\nFinished in {end - start} seconds...")
