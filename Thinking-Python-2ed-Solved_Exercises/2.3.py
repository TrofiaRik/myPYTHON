#My Leaving Time, to be converted in secs from hh:mm:ss
leaving_hh=6
leaving_mm=52
leaving_ss_secs=0
print("This morning I left home at exactly",leaving_hh,":",leaving_mm,":",leaving_ss_secs)
leaving_hh_secs=leaving_hh*60*60
leaving_mm_secs=leaving_mm*60
leaving_T_secs=leaving_hh_secs+leaving_mm_secs+leaving_ss_secs
print("(Which in seconds is:",leaving_T_secs,")","\n")

#Easy Pace average TIME per MILE
easy_pace_hh=0
easy_pace_mm=8
easy_pace_ss_secs=15
print("To walk ONE MILE at an EASY PACE, I usually need an average of",easy_pace_hh,"hours",easy_pace_mm,"minutes, and",easy_pace_ss_secs,"seconds")
easy_pace_hh_secs=easy_pace_hh*60*60
easy_pace_mm_secs=easy_pace_mm*60
easy_pace_T_secs_for_1_mile=easy_pace_hh_secs+easy_pace_mm_secs+easy_pace_ss_secs
print("and therefore, to cover 1 mile at an EASY PACE I usually need",easy_pace_T_secs_for_1_mile,"seconds")

#Fast Pace, average TIME per MILE
fast_pace_hh=0
fast_pace_mm=7
fast_pace_ss_secs=12
print("While to cover ONE MILE at my FAST PACE, I usually take an average of",fast_pace_hh,"hours",fast_pace_mm,"minutes, and",fast_pace_ss_secs,"seconds")
fast_pace_hh_secs=fast_pace_hh*60*60
fast_pace_mm_secs=fast_pace_mm*60
fast_pace_T_secs_for_1_mile=fast_pace_hh_secs+fast_pace_mm_secs+fast_pace_ss_secs
print("and therefore, to cover 1 mile at a FAST PACE I usually need",fast_pace_T_secs_for_1_mile,"seconds \n")


#Distances in MILES
t_distance=5
distance_covered_at_easy_pace=2
distance_covered_at_fast_pace=3

#Calculation of time in secs and h:m:s needed to walk the distance covered this morning
print("So, this morning I covered a total of",t_distance,"miles, of which, if I am not wrong,",distance_covered_at_easy_pace,"miles were covered at an EASY PACE,while the remaining",distance_covered_at_fast_pace,"miles have been covered at a FAST PACE")
time_to_walk_2miles_secs=distance_covered_at_easy_pace*easy_pace_T_secs_for_1_mile
time_to_walk_3miles_secs=distance_covered_at_fast_pace*fast_pace_T_secs_for_1_mile
time_to_walk_5miles_secs=time_to_walk_2miles_secs+time_to_walk_3miles_secs
print("Secs to walk 2 miles",time_to_walk_2miles_secs)
print("Secs to walk 3 miles",time_to_walk_3miles_secs)
print("Secs to walk 5 miles",time_to_walk_5miles_secs)


#Arrival Time, sum time_to_walk_5miles_secs to leaving_T_secs and convert back to h:m:s
arrival_time_secs=leaving_T_secs+time_to_walk_5miles_secs
print("Arrival time in secs is",arrival_time_secs)

arrival_hh=arrival_time_secs//3600
arrival_mm=(arrival_time_secs%3600)//60
arrival_ss=(arrival_time_secs%3600)%60
print("Arrived at H",arrival_hh)
print("minutes",arrival_mm)
print("and seconds",arrival_ss)
