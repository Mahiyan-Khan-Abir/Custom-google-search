#Please Avoid requerying the same data.
#For example avoid using the same search term/search query again and again as
#it can lead to "quota exceeded" Error.If found, Please change the API and try again.


from googleapiclient.discovery import build

#api = "AIzaSyC1z_K-AAJ84KQw2xZJQaW0R52uVqGyDGA"        #API_KEY_01
api = "AIzaSyCqZTlxV2R3jEiMXxdJ9Eb8JT-RF3R2Pps"         #API_KEY_02
cse = "9290b219a1130f1c4"                               #search-engine-ID

def google_search(search_term, api, cse, **kwargs):
    service = build("customsearch", "v1", developerKey=api)
    res = service.cse().list(q=search_term, cx=cse, **kwargs).execute()
    return res['items']


results = google_search(input("Enter query: "), api, cse, num=4)      #num = Number of results to catch

for result in results:

      L = [result.get('link')]
      T = [result.get('title')]
      TXT = [(result.get('snippet'))]
      ML = [L,T,TXT]
     
      print(ML)
      # print(ML[0])
      # print(ML[1])
      # print(ML[2])