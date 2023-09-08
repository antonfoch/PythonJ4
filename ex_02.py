import requests

URL = "https://graph.microsoft.com/beta/teams/{team_id}/channels"

AUTH = 'eyJ0eXAiOiJKV1QiLCJub25jZSI6InNkalpvMXk5VEdlWmFYZjVkX2JyZlBQcHcxY2VMamw2a21iby1paEQzT0UiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC85MDFjYjRjYS1iODYyLTQwMjktOTMwNi1lNWNkMGY2ZDlmODYvIiwiaWF0IjoxNjk0MTU5MTU2LCJuYmYiOjE2OTQxNTkxNTYsImV4cCI6MTY5NDI0NTg1NiwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhVQUFBQXRUcm5TWU5IUG9PYVoxSFFsdGlvcWFVVUdLYlBoeVEzSDdZODJkRmZnb2p3NjhVV1ZKZDFDWXdOWHFwUk54QXE5SnlrUUdxSjlKRzRwbjhHRGpCNUtRejZJUzQ3cDAvRjJxV253Wks0NXU4PSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiR3JhcGggRXhwbG9yZXIiLCJhcHBpZCI6ImRlOGJjOGI1LWQ5ZjktNDhiMS1hOGFkLWI3NDhkYTcyNTA2NCIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiRm9jaCIsImdpdmVuX25hbWUiOiJBbnRvbiIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjE2My41LjIzLjM4IiwibmFtZSI6IkFudG9uIEZvY2giLCJvaWQiOiIwZjkyNGVhMy1hY2YxLTQwZTItOTNlNC0yNzM5ZTQxMzcxNjciLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMTU1MjQzNTI3Ny0xNTk2NDk1Nzk1LTMwODk2MTM3MzEtNDY1NDQiLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzIwMDFFNUQ3Mjk3RCIsInJoIjoiMC5BWFFBeXJRY2tHSzRLVUNUQnVYTkQyMmZoZ01BQUFBQUFBQUF3QUFBQUFBQUFBQjBBS3MuIiwic2NwIjoiR3JvdXAuUmVhZC5BbGwgR3JvdXAuUmVhZFdyaXRlLkFsbCBwcm9maWxlIG9wZW5pZCBlbWFpbCBVc2VyLlJlYWQiLCJzaWduaW5fc3RhdGUiOlsia21zaSJdLCJzdWIiOiJYXzJfWm1xbzM3QlVtR1BKSnVqLUFZRmt0Q2ZCTks2MjZkekV2T0pkanFRIiwidGVuYW50X3JlZ2lvbl9zY29wZSI6IkVVIiwidGlkIjoiOTAxY2I0Y2EtYjg2Mi00MDI5LTkzMDYtZTVjZDBmNmQ5Zjg2IiwidW5pcXVlX25hbWUiOiJhbnRvbi5mb2NoQGVwaXRlY2guZGlnaXRhbCIsInVwbiI6ImFudG9uLmZvY2hAZXBpdGVjaC5kaWdpdGFsIiwidXRpIjoic3F6UFNoSTRIa1dZVFIwQlhpdUpBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19jYyI6WyJDUDEiXSwieG1zX3NzbSI6IjEiLCJ4bXNfc3QiOnsic3ViIjoiaElId1hsZ1JBMVFFZ1V0Mnl4b0hhUm9sVUVCWE0tdTF3QU5EZnhsUExvYyJ9LCJ4bXNfdGNkdCI6MTQxNzgwNDg4NywieG1zX3RkYnIiOiJFVSJ9.Ra038yPrfzzwWMxoWysZ3PrhOYm80c0a1Y6IaCXvL_pyTwEP8uahZY8QuNyrcdFyAc1zbayYdnlh9cH9GMaTQftsBmSvvV4QB2NRW722JBpIhQimVme7bd4DGqHyXXM4inM_0OUHr0IgGxi4MkDUzYc5Yt56KgCUS2zOCln7h4Y62RZsNK6T_8X17c-YdJSAlwd9LeEWxcHgt_-HoxYuf-adbulVyNNcfhSxsjHNzwumtLstvxtHI4Quslk_POwpoXcBrUdQuYv0AWb3tTESfATslOVy9U189gSnTkrikFyRDgwLbl6reJmGQbqOrTX-158125zjfpoiqOO-qBtkJQ'


def member_of(item_id):

    headers = {"Authorization": f"Bearer {AUTH}"}
    response = requests.get(url=URL, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Error")
        print(response.text)
        return {}

    
teams = member_of("001015a4-1498-431e-8687-372b23df2806")
