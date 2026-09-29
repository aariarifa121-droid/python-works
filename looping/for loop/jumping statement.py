 # Jumbing statement


##the statements whihc we used to alter the flow of loop

#break >> the break statement completely terminates the current loop,

#used to alter the flow of loop


#continue >> statement skips the rest of the current iteration and jumps to the next cycle.

#pass

#break
#for i in range(1, 100):

    #if i == 10:

        #break

    #print(i)



# continue>>


for i in range(1,50):

    if i % 3 == 0:

        print("skip this iteration using continue")

        continue

    print(f"{i}")