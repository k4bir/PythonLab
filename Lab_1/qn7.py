""""You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each
of the 10 stops on the way. How long will the bus journey take? Alternatively, you could run
to university. You could jog the first mile at 7mph; then run the next two at 15mph; before
jogging the last at 7mph; then run the next two at 15mph; before jogging the last at 7mph
again. Will this be quicker or slower than the bus?"""

#for bus
bus_distance=4
bus_speed=25
bus_t=bus_distance/bus_speed
bus_stop=2*10
bus_time=(bus_t*60)+bus_stop
print(f'Total time taken by bus is {bus_time}')

#for jogging
jog_distance=2
jog_speed=7
jog_time=(jog_distance/jog_speed)*60

#for running
run_distance=2
run_speed=15
run_time=(run_distance/run_speed)*60

total_time=(jog_time+run_time)
print(f'Total time taken by running is {total_time}')

if bus_time>total_time:
    print("Taking bus is slower than running !!")
else:
    print("Taking bus is faster than running !!")