def difference(start_time,stop_time):
    min_diff=0
    sec_diff=0
    ms_diff=0
    if int(start_time[0])>int(stop_time[0]):
        print("Invalid time")
    else:
        min_diff=int(stop_time[0])-int(start_time[0])
    if int(start_time[1])>int(stop_time[1]):
        sec_diff=(60-int(start_time[1]))+int(stop_time[1])
    else:
        sec_diff=int(stop_time[1])-int(start_time[1])
    if int(start_time[2])>int(stop_time[2]):
        ms_diff=(1000-int(start_time[2]))+int(stop_time[2])
    else:
        ms_diff=int(stop_time[2])-int(start_time[2])
    
    print(f"The elapsed time is {min_diff} Minutes {sec_diff} Seconds {ms_diff} Milliseconds")

start_time=input("Enter the start time(MM:SS:MSMS):")
stop_time=input("Enter the stop time(MM:SS:MSMS):")

start_time=list(start_time.split(":"))
stop_time=list(stop_time.split(":"))
print(start_time)
print(stop_time)
difference(start_time,stop_time)
