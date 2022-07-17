import datetime
def epoch_to_utc(epoch_time):
    return datetime.datetime.utcfromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')

def epoch_to_local(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    print(epoch_to_utc(1347517370))
    print(epoch_to_local(1347517370))