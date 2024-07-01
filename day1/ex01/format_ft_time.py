from datetime import datetime
from datetime import date
import time

fromTimestamp = datetime.today()
print("Seconds since January 1, 1970:", "{:,}".format(round(fromTimestamp.timestamp(), 4)), "or", "{:.2e}".format(fromTimestamp.timestamp()) ,"in scentific notation" )
print(fromTimestamp.strftime("%b %d %Y"))