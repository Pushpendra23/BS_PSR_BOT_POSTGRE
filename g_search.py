from googleapiclient.discovery import build

my_api_key = "API KEY"
my_cse_id = "CSE ID"

#Function to trigger Custom Google Search and return raw data
def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def get_search(message):
    in_cmd = message.content
    results = google_search(message.content[7:], my_api_key, my_cse_id, num=5)
    return results
