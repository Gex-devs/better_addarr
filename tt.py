import RadarrApi
from dotenv import load_dotenv
import os
import json

load_dotenv()


host = os.getenv("HOST")
port = os.getenv("PORT")
apikey = os.getenv("radarr_ApiKey")


radarr = RadarrApi.RadarrApi(apikey,host,port)


j = radarr.lookup("spiderman")

for i, x in enumerate(j):
    if i < 4:
        print(x['title'])
        print(x['images'][0]['url'])
    else:
        break

    

