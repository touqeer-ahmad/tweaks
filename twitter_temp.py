import os
import sys
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

cmd = '/opt/vc/bin/vcgencmd measure_temp'  
line = os.popen(cmd).readline().strip()  
temp = line.split('=')[1].split("'")[0]

message = "Your RPI temp is "+ temp
twitter.update_status(status=message)
print("Tweeted: %s" % message)
