chapter = "### CHAPTER 1 - INTRODUCTION ###"
title = "### PROBLEM 01 ###"
c01_p01_tx = """Imagine that you have trained your St. Bernard, Bernie, to carry a box of three 8-mm tapes instead of a flask of brandy. (When your disk fills up, you consider that an emergency.)\nThese tapes each contain 7 gigabytes. The dog can travel to your side, wherever you may be, at 18 km/hour.\n\nFor what range of distances does Bernie have a higher data rate than a transmission line whose data rate (excluding overhead) is 150 Mbps?\n\nHow does your answer change if\n(i) Bernie\'s speed is doubled;\n(ii) each tape capacity is doubled;\n(iii) the data rate of the trasmission line is doubled."""

print("###############################################################")    
print(chapter)
print("###############################################################")    
print(title) 
print("###############################################################")
print(c01_p01_tx)
print("###############################################################\n")
r = 0
while True:
    if r == 0 :
        print("\n*** SOLUTION ***\n")
        print("Here follows the solution! First, confirm the problem default values (enter), or insert your custom ones!\n")
        tape = input("Insert a tape size in GB (enter=7.00): \n")
        if not tape : tape = 7.00
        else : tape = float(tape)
        qty = input("Insert a how many tapes Ber can carry (enter=3): \n")
        if not qty : qty = 3
        else : qty = int(qty)
        speed = input("Insert Ber speed (enter=18.00): \n")
        if not speed : speed = 18.00
        else : speed = float(speed)
        speed_u_n = "km"
        speed_u_d = "h"
        line_dr = input("Insert the Line Data Rate in Mega bits per second (enter=150.00): \n")
        if not line_dr : line_dr = 150.00
        else : line_dr = float(line_dr)
        line_dr_u_n = "Mb"
        line_dr_u_d = "ps"

        print(f'Thanks! We are going to solve with:\nTape size: {tape:.2f}GB\nNumber of tapes: {qty}\nBar speed: {speed:.2f}km/h\nLine data rate: {line_dr:.2f}Mbps\n\n')

        nex = ""
        while nex != "y" and nex != "n":
            nex = input("Would you like to dive in and try to build the solution of this problem (y or n)? ")
            if nex == "n":
                print("Ok, bye bye then, and see you soon!")
            elif nex == "y":
                print("\nLet's proceed then\n")
            else:
                print("You must enter y or n, please retry.")
        print("###############################################################")    
        print("### 1st step ### CONVERT BER\'S TOTAL AMOUNT OF DATA TO bits ###")
        print("###############################################################\n")    
        print("a) First thing to do is to determine the total amount of data carried by Ber:")
        print(f'--> Tape\'s size x Nr. of tapes = Total Amount of Data')
        tqty=tape*qty
        print(f'--> {tape:,}GB * {qty} = {tqty:,}GB\n')
        print('b) Now, let\'s convert GB to bits')
        print('First, we should consider 1GB = 2^30 bytes (1,073,741,824), rather than the decimal approximation of 10^9 bytes (1,000,000,000 bytes), a well estabilished convention for expressing the quantity of data contained in a phisical storage medium.')
        tqty_bytes = tqty*1073741824
        print(f'If 1 GB = 1*2^30 bytes, {tqty:.2f} GB = {tqty:.2f}*2^30 bytes = {tqty:.2f}*1,073,741,824 bytes = {tqty_bytes:,.2f} bytes\n')
        print('c) And finally, considering that 1 byte = 8 bits, Total bits = Total bytes * 8')
        tqty_bits = tqty_bytes*8
        print(f'--> {tqty_bytes:,.2f}*8 bits = {tqty_bits:,.2f} bits\n')
        s = input('\n\n...press enter to continue...\n\n')
        print("####################################################################")    
        print("### 2nd step ### FIND BER\'S DATARATE IN FUNCTION OF THE DISTANCE ###")
        print("####################################################################\n")
        print('---------------------------------------------------------------------------')
        print('a) First of all let\'s consider how data rate is generally defined and why:')
        print('---------------------------------------------------------------------------')
        print('Data Rate = Data Amount / Time\nFor example, our 150Mbps line can be expressed as: Line Data Rate = 150Mbit (data amount) / 1 second (time)')
        print('This is the standard way to express data rates in real-world applications for two main reasons:\n')
        print('1. Continuous vs. Instantaneous Transfer & Latency.')
        print('* Data rate typically refers to a continuous stream of data, not a single burst.')
        print('* For instance, a 1 Gbps connection means data flows at 1 Gbit per second continuously, rather than a single 1 Gbit packet sent in one second.')
        print('* In such a continuous stream, there is an initial delay called latency, which is the time required for the first bit to travel through the medium before data starts flowing at the expected rate.')
        print('A useful analogy is to think of a pipeline carrying water: when you turn on the tap, there is a short delay before water reaches the end because it takes time for the first drops to travel through the pipe. Once the pipe is full, water flows continuously at a constant rate.')
        print('Similarly, in a network, the first bit of data must travel the full distance before the receiver gets anything, but once data starts arriving, it continues at the full data rate.')
        print('This is why, in most cases, latency is treated separately from data rate — it affects the initial delay but does not change the rate at which data flows once transmission begins.')
        s = input('\n\n...press enter to continue...\n\n')
        print('2. High Transmission Speeds Minimize Distance Effects.')
        print("""In modern communication systems (e.g., fiber optics, radio waves), data propagates at extremely high speeds (close to the speed of light).\nBecause of this, we don’t usually need to explicitly include distance (d) in the data rate formula — it is assumed that transmission is fast enough that distance effects are negligible.\nHowever, in certain cases, where data is physically transported (e.g., our dog Ber carrying data tapes), we must rethink this approach. In such a scenario, data rate must also be expressed as a function of distance, since the velocity of the carrier (Ber) directly impacts the effective transmission rate.\n""")
        s = input('\n\n...press enter to continue...\n\n')
        print('--------------------------------------')   
        print('b) Now, let\'s determine Ber datarate!')
        print('--------------------------------------')
        print('If in a normal scenario Data Rate = Data Amount / Time')
        print(f'In our scenario we must translate time as a function of distance, so we can consider\n\n  t = s/v, or t = d/v\n\n  t(hours) = d/{speed:,.2f}\n\n  t(seconds) = (d/{speed:,.2f})*3600\n\n  with the idea of substituting velocity with Ber velocity while keeping d as the unknown variable\n')
        t_d_secs=3600/speed
        print(f'  Our value of \'t\' is: {t_d_secs:,.2f}d')   
        s = input('\n\n...press enter to continue...\n\n')
        print(f'Therefore, substituting \'t\'\n\n  BDR = {tqty_bits:,.2f} / {t_d_secs:,.2f}d\n') 
        bdr = tqty_bits / t_d_secs
        print(f'  BDR = {bdr:,.2f} / d\n\n')
        s = input('\n\n...press enter to continue...\n\n')
        print("################################################################################################")    
        print("### 3nd step ### FIND FOR WHAT RANGE OF DISTANCES BER HAVE AN HIGHER DR THAN THE 150 Mbps TL ###")
        print("################################################################################################\n")
        print("\nWe need to confront BDR(d) to TLDR\n")
        line_dr_raw = line_dr*1000000
        print(f'TLDR = {line_dr:,.2f}Mbps, which is a raw value of {line_dr_raw:,.2f} bits per second\n\n')
        print('Let\'s build our equation as follows, keeping into consideration that our d value shall be expressed in km:\n\n')
        print(f'  {bdr:,.2f} / d > {line_dr_raw:,.2f}\n\n')
        print(f'  {bdr:,.2f} / {line_dr_raw:,.2f} > d\n\n')
        rdr = bdr / line_dr_raw
        print(f'  d < {rdr:,.2f} km')
        r += 1
        continue    
    elif r == 1 :
        s = input('\n\nShould we proceed with the optional questions? y or n:\n\n')
        if s == 'y' :
            print("\n\n*** SOLUTION i - BER SPEED DOUBLED ***\n\n")
            tape = 7.00
            qty = 3
            speed = 36.00
            speed_u_n = "km"
            speed_u_d = "h"
            line_dr = 150.00
            line_dr_u_n = "Mb"
            line_dr_u_d = "ps"
            print(f'Thanks! We are going to solve with:\nTape size: {tape:.2f}GB\nNumber of tapes: {qty}\nBar speed: {speed:.2f}km/h\nLine data rate: {line_dr:.2f}Mbps\n\n')
            nex = ""
            print("###############################################################")    
            print("### 1st step ### CONVERT BER\'S TOTAL AMOUNT OF DATA TO bits ###")
            print("###############################################################\n")    
            print("a) First thing to do is to determine the total amount of data carried by Ber:")
            tqty=tape*qty
            print(f'--> {tape:,}GB * {qty} = {tqty:,}GB\n')
            print('b) Now, let\'s convert GB to bits')
            tqty_bytes = tqty*1073741824
            tqty_bits = tqty_bytes*8
            print(f'--> {tqty_bytes:,.2f}*8 bits = {tqty_bits:,.2f} bits\n')
            print("####################################################################")    
            print("### 2nd step ### FIND BER\'S DATARATE IN FUNCTION OF THE DISTANCE ###")
            print("####################################################################\n")
            print(f'Let\'s consider\n\n  t = s/v, or t = d/v\n\n  t(hours) = d/{speed:,.2f}\n\n  t(seconds) = (d/{speed:,.2f})*3600\n\n')
            t_d_secs=3600/speed
            print(f'  Our value of \'t\' is: {t_d_secs:,.2f}d')   
            print(f'Therefore, substituting \'t\'\n\n  BDR = {tqty_bits:,.2f} / {t_d_secs:,.2f}d\n') 
            bdr = tqty_bits / t_d_secs
            print(f'  BDR = {bdr:,.2f} / d\n\n')
            print("################################################################################################")    
            print("### 3nd step ### FIND FOR WHAT RANGE OF DISTANCES BER HAVE AN HIGHER DR THAN THE 150 Mbps TL ###")
            print("################################################################################################\n")
            print("\nWe need to confront BDR(d) to TLDR\n")
            line_dr_raw = line_dr*1000000
            print(f'TLDR = {line_dr:,.2f}Mbps, which is a raw value of {line_dr_raw:,.2f} bits per second\n\n')
            print('Let\'s build our equation as follows, keeping into consideration that our d value shall be expressed in km:\n\n')
            print(f'  {bdr:,.2f} / d > {line_dr_raw:,.2f}\n\n')
            print(f'  {bdr:,.2f} / {line_dr_raw:,.2f} > d\n\n')
            rdr = bdr / line_dr_raw
            print(f'  d < {rdr:,.2f} km')
            nx = input('\n\n...return to proceed with ii...\n\n')
            print("\n\n*** SOLUTION ii - TAPES CAPACITY DOUBLED ***\n\n")
            tape = 14.00
            qty = 3
            speed = 18.00
            speed_u_n = "km"
            speed_u_d = "h"
            line_dr = 150.00
            line_dr_u_n = "Mb"
            line_dr_u_d = "ps"
            print(f'Thanks! We are going to solve with:\nTape size: {tape:.2f}GB\nNumber of tapes: {qty}\nBar speed: {speed:.2f}km/h\nLine data rate: {line_dr:.2f}Mbps\n\n')
            nex = ""
            print("###############################################################")    
            print("### 1st step ### CONVERT BER\'S TOTAL AMOUNT OF DATA TO bits ###")
            print("###############################################################\n")    
            print("a) First thing to do is to determine the total amount of data carried by Ber:")
            tqty=tape*qty
            print(f'--> {tape:,}GB * {qty} = {tqty:,}GB\n')
            print('b) Now, let\'s convert GB to bits')
            tqty_bytes = tqty*1073741824
            tqty_bits = tqty_bytes*8
            print(f'--> {tqty_bytes:,.2f}*8 bits = {tqty_bits:,.2f} bits\n')
            print("####################################################################")    
            print("### 2nd step ### FIND BER\'S DATARATE IN FUNCTION OF THE DISTANCE ###")
            print("####################################################################\n")
            print(f'Let\'s consider\n\n  t = s/v, or t = d/v\n\n  t(hours) = d/{speed:,.2f}\n\n  t(seconds) = (d/{speed:,.2f})*3600\n\n')
            t_d_secs=3600/speed
            print(f'  Our value of \'t\' is: {t_d_secs:,.2f}d')   
            print(f'Therefore, substituting \'t\'\n\n  BDR = {tqty_bits:,.2f} / {t_d_secs:,.2f}d\n') 
            bdr = tqty_bits / t_d_secs
            print(f'  BDR = {bdr:,.2f} / d\n\n')
            print("################################################################################################")    
            print("### 3nd step ### FIND FOR WHAT RANGE OF DISTANCES BER HAVE AN HIGHER DR THAN THE 150 Mbps TL ###")
            print("################################################################################################\n")
            print("\nWe need to confront BDR(d) to TLDR\n")
            line_dr_raw = line_dr*1000000
            print(f'TLDR = {line_dr:,.2f}Mbps, which is a raw value of {line_dr_raw:,.2f} bits per second\n\n')
            print('Let\'s build our equation as follows, keeping into consideration that our d value shall be expressed in km:\n\n')
            print(f'  {bdr:,.2f} / d > {line_dr_raw:,.2f}\n\n')
            print(f'  {bdr:,.2f} / {line_dr_raw:,.2f} > d\n\n')
            rdr = bdr / line_dr_raw
            print(f'  d < {rdr:,.2f} km')
            
            nx = input('\n\n...return to proceed with iii...\n\n')
            print("\n\n*** SOLUTION iii - DATA LINE SPEED DOUBLED ***\n\n")
            tape = 7.00
            qty = 3
            speed = 18.00
            speed_u_n = "km"
            speed_u_d = "h"
            line_dr = 300.00
            line_dr_u_n = "Mb"
            line_dr_u_d = "ps"
            print(f'Tape size: {tape:.2f}GB\nNumber of tapes: {qty}\nBar speed: {speed:.2f}km/h\nLine data rate: {line_dr:.2f}Mbps')
            print("### 1st step ### CONVERT BER\'S TOTAL AMOUNT OF DATA TO bits ###")
            print("###############################################################\n")    
            tqty=tape*qty
            print(f'--> {tape:,}GB * {qty} = {tqty:,}GB\n')
            tqty_bytes = tqty*1073741824
            tqty_bits = tqty_bytes*8
            print(f'--> {tqty_bytes:,.2f}*8 bits = {tqty_bits:,.2f} bits\n')   
            print("### 2nd step ### FIND BER\'S DATARATE IN FUNCTION OF THE DISTANCE ###")
            print("####################################################################\n")
            print(f'Let\'s consider\n\n  t = s/v, or t = d/v\n\n  t(hours) = d/{speed:,.2f}\n\n  t(seconds) = (d/{speed:,.2f})*3600\n\n')
            t_d_secs=3600/speed
            print(f'  Our value of \'t\' is: {t_d_secs:,.2f}d')   
            print(f'Therefore, substituting \'t\'\n\n  BDR = {tqty_bits:,.2f} / {t_d_secs:,.2f}d\n') 
            bdr = tqty_bits / t_d_secs
            print(f'  BDR = {bdr:,.2f} / d\n\n')
            print("### 3nd step ### FIND FOR WHAT RANGE OF DISTANCES BER HAVE AN HIGHER DR THAN THE 150 Mbps TL ###")
            print("################################################################################################\n")
            print("\nWe need to confront BDR(d) to TLDR\n")
            line_dr_raw = line_dr*1000000
            print(f'TLDR = {line_dr:,.2f}Mbps, which is a raw value of {line_dr_raw:,.2f} bits per second\n\n')
            print('Let\'s build our equation as follows, keeping into consideration that our d value shall be expressed in km:\n\n')
            print(f'  {bdr:,.2f} / d > {line_dr_raw:,.2f}\n\n')
            print(f'  {bdr:,.2f} / {line_dr_raw:,.2f} > d\n\n')
            rdr = bdr / line_dr_raw
            print(f'  d < {rdr:,.2f} km')
        elif s == 'n' : break
        else : continue
    exi_t = input('\n\nWould you like to restart from the beginning? y or n:\n\n')
    if exi_t == 'y' : 
        r=0
        continue
    else :
        break
    #break
