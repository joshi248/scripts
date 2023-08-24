import requests

year = int(input("Enter the year: "))
orbitClass = input("Enter the orbit class: ").lower()
# print(orbitClass)
response = requests.get('https://jsonmock.hackerrank.com/api/asteroids/search?=' + orbitClass + '&page=1').json()


total_pages = response['total_pages']
per_page = response['per_page']

ans = []

for i in range(1, total_pages + 1):
    temp_response = requests.get('https://jsonmock.hackerrank.com/api/asteroids/search?orbit_class=' + orbitClass + '&page='+ str(i)).json()

    temp_ans = []
    for j in range(per_page):
        try:
            temp_ans.append(temp_response['data'][j])

        except:
            pass

    data = sorted(temp_ans, key=lambda x: (float(x.get('period_yr', '1')), x['designation']))
    n = len(data)
    for k in range(n):
        if int(data[k]['discovery_date'][0:4]) == year:
            ans.append(data[k]['designation'])

m = len(ans)
for i in range(m):
    print(ans[i])

