from operator import itemgetter
import plotly.express as px
import requests

#Make an API call and check the response

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"status code: {r.status_code}")

#process information about each submission

submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:5]:
    #make new API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?ud={submission_id}",
        'comments': response_dict['descendants']
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse = True)

"""
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
"""

titles = [item['title'] for item in submission_dicts]
comments = [item['comments'] for item in submission_dicts]


fig = px.bar(titles, comments)
fig.show()
