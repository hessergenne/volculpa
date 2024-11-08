from serpapi import GoogleSearch

def google_search(search_term, SERVICE_API_KEY):
    params = {
        "q": search_term,
        "SERVICE_API_KEY": SERVICE_API_KEY
    }
    search = GoogleSearch(params)
    results = search.get_json()
    return results

results = google_search("Python", "YOUR_SERVICE_API_KEY")
print(results)
