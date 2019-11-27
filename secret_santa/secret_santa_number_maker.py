import numpy as np
import matplotlib.pyplot as plt
import copy

names = ["Mads", "Willie",
         "Patrick", "Jennnnnnnnnnnnnnnnnnnn",
         "Andrea", "Fireman Dan",
         "Sir Dan Smith",
         "Kenzie", "Maybe Ted",
         "Don Jr.", "Jill"]

xs = []
ys = []

verbose = True
total_trails = 1
for ntrails in range(total_trails):

    worked = False
    names_giver = copy.deepcopy(names)
    names_taker = copy.deepcopy(names)
    while not(worked):    
        np.random.shuffle(names_giver)
        np.random.shuffle(names_taker)

        if(verbose):
            print(names_giver)
            print(names_taker)
    
        # See if it worked.
        worked = True
        for i in range(len(names_giver)):
            if(names_giver[i] == names_taker[i]):
                if(verbose):
                    print names_giver[i], "got themselves."
                    print ""
                worked = False
                break
            
        if not(worked):
            continue
        
        # Now check pairs. SOs can't get each other and Don / Willie can't get each other.
        worked = True
        for i in range(len(names_giver)):
            # Madison and Willie
            if((names_giver[i] == "Mads" and names_taker[i] == "Willie") or
               (names_taker[i] == "Mads" and names_giver[i] == "Willie")):
                if(verbose):
                    print names_giver[i], "got SO ", names_taker[i]
                    print ""
                worked = False
                break
            
            # Kenzie and Maybe Ted
            if((names_giver[i] == "Kenzie" and names_taker[i] == "Maybe Ted") or
               (names_taker[i] == "Kenzie" and names_giver[i] == "Maybe Ted")):
                if(verbose):
                    print names_giver[i], "got SO ", names_taker[i]
                    print ""
                worked = False
                break
            
            # Patrick and Jennnnnnnnnnnnnnnnnnnn
            if((names_giver[i] == "Patrick" and names_taker[i] == "Jennnnnnnnnnnnnnnnnnnn") or
               (names_taker[i] == "Patrick" and names_giver[i] == "Jennnnnnnnnnnnnnnnnnnn")):
                if(verbose):
                    print names_giver[i], "got SO ", names_taker[i]
                    print ""
                worked = False
                break
            
            # Don Jr. and Jill
            if((names_giver[i] == "Don Jr." and names_taker[i] == "Jill") or
               (names_taker[i] == "Don Jr." and names_giver[i] == "Jill")):
                if(verbose):
                    print names_giver[i], "got SO ", names_taker[i]
                    print ""
                worked = False
                break

            # Andrea and Fireman Dan
            if((names_giver[i] == "Andrea" and names_taker[i] == "Fireman Dan") or
               (names_taker[i] == "Andrea" and names_giver[i] == "Fireman Dan")):
                if(verbose):
                    print names_giver[i], "got SO ", names_taker[i]
                    print ""
                worked = False
                break
            
            # Don Jr. and Willie
            if((names_giver[i] == "Don Jr." and names_taker[i] == "Willie") or
               (names_taker[i] == "Don Jr." and names_giver[i] == "Willie")):
                if(verbose):
                    print names_giver[i], "got SO ", names_taker[i]
                    print ""
                worked = False
                break

    if(verbose):
        secret_numbers = np.random.uniform(0.0, np.power(2, 12), len(names_giver)).astype("int").tolist()

        print "var names_giver =", names_giver
        print "var names_taker =", names_taker
        print "var secret_numbers =", secret_numbers

        print ""
        print ""
        
        for i in range(len(names_giver)):
            print names_giver[i], secret_numbers[i]
        
    for i in range(len(names_giver)):
        xs += [names.index(names_giver[i])]
        ys += [names.index(names_taker[i])]
        if(verbose):
            print(names_giver[i], names_taker[i])
            
h = plt.hist2d(xs, ys, weights = np.ones(len(xs)) / float(total_trails), range=((0.0, 11.0), (0.0, 11.0)), bins=(11, 11))
plt.colorbar(label="Probablity of Match")
plt.clim(0.0, 0.2)

plt.axes().set_xticks(np.array(range(11)) + 0.5)
plt.axes().set_yticks(np.array(range(11)) + 0.5)
plt.axes().set_xticklabels(names)
plt.axes().set_yticklabels(names)
plt.show()
