DEVELOPER_KEY = "AIzaSyBdWFbJYFDq-61bNwc4_YyvVi4uRVSx_c0"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(q, max_results=50,order="relevance", token=None, location=None, location_radius=None):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
    q=q,
    type="video",
    pageToken=token,
    order = order,
    part="id,snippet", # Part signifies the different types of data you want
    maxResults=max_results,
    location=location,
    locationRadius=location_radius).execute()

    title = []
    channelId = []
    channelTitle = []
    categoryId = []
    videoId = []
    viewCount = []
    likeCount = []
    dislikeCount = []
    commentCount = []
    favoriteCount = []
    category = []
    tags = []
    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            try:
                title.append(search_result['snippet']['title'])

                videoId.append(search_result['id']['videoId'])

                response = youtube.videos().list(
                    part='statistics, snippet',
                    id=search_result['id']['videoId']).execute()

                channelId.append(response['items'][0]['snippet']['channelId'])
                channelTitle.append(response['items'][0]['snippet']['channelTitle'])
                categoryId.append(response['items'][0]['snippet']['categoryId'])
                favoriteCount.append(response['items'][0]['statistics']['favoriteCount'])
                viewCount.append(response['items'][0]['statistics']['viewCount'])
                likeCount.append(response['items'][0]['statistics']['likeCount'])
                dislikeCount.append(response['items'][0]['statistics']['dislikeCount'])
            except:
                continue
        if 'commentCount' in response['items'][0]['statistics'].keys():
            commentCount.append(response['items'][0]['statistics']['commentCount'])
        else:
            commentCount.append([])

        if 'tags' in response['items'][0]['snippet'].keys():
            tags.append(response['items'][0]['snippet']['tags'])
        else:
            tags.append([])

    youtube_dict = {'tags':tags,'channelId': channelId,'channelTitle': channelTitle,'categoryId':categoryId,'title':title,'videoId':videoId,'likeCount':likeCount,'dislikeCount':dislikeCount,'commentCount':commentCount,'favoriteCount':favoriteCount}

    return youtube_dict
name='Drive'
test = youtube_search(name+' Official Trailer')
index = []
while len(index)<1:
    for i in test['title']:
        if 'Official Trailer' and '#1' in i:
            index.append(test['title'].index(i))
            break
        elif 'Official Trailer' and '#2' in i:
            index.append(test['title'].index(i))
            break
        elif 'Official Trailer' and 'HD' in i:
            index.append(test['title'].index(i))
            break
link = 'https://www.youtube.com/watch?v='+str(test['videoId'][index[0
print('the link of the chosen video for the movie',name,'is:',link)
try:
    likes = int(test['likeCount'][index[0]])
except:
    likes = 'NaN'
try:
    dis = int(test['dislikeCount'][index[0]])
except:
    dis = 'NaN'
try:
    ratio = likes/dis
except:
    ratio = 'NaN'
print('Ratio of Likes to Dislikes is:',ratio)
