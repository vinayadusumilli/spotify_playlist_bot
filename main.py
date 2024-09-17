from web_data_manager import WebDataManager

requested_date = input("Which year do you want to be playlist created(YYYY-MM-YY): ")
URL = f"https://www.billboard.com/charts/hot-100/{requested_date}/"

web_data = WebDataManager(URL)
print(web_data.get_songs())