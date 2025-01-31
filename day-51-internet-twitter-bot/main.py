from internet_api import InternetSpeedTwitterBot

# Instantiate Driver
print("Create Driver....")
my_bot = InternetSpeedTwitterBot()
# Get internet speed from speedtest.net
print("Now get internet speeds")
my_bot.get_internet_speed()
print("After internet speeds")
