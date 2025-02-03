from reservation_bot import CampgroundReserver
from datetime import date

# Let's just go ahead and skip to July since who wants to camp in the cold?
SKIP_TO_DATE = date(2025, 7, 1)

# Find reservation for Holland Lake
# TODO make this a user inputted campsite or better yet, have this run through multiple campgrounds!
holland_lake_reserver = CampgroundReserver("https://www.recreation.gov/camping/campgrounds/234486")

# Monday = 0,  Friday = 4
holland_lake_reserver.find_reservation(day_name="Friday", specific_date=None, skip_to_date=SKIP_TO_DATE)
# holland_lake_reserver.find_reservation(day_name= None, specific_date=date(2025,7,9), skip_to_date=SKIP_TO_DATE)

# If a reservation was found, reserve the campsite!
if holland_lake_reserver.not_reservable is True:
        print("No available campsites. Try again tomorrow.")
# Otherwise, we found a campsite and now we can reserve it!
else:
        holland_lake_reserver.reserve_campsite()



