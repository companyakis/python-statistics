import numpy as np

#create an unreal city population -> ages: 0 to 90, # of people 10000

#integer ages:) keep it simple:)

our_population = np.random.randint(0, 90, 10000)

#let's look at first 15 ages

print(our_population[:15]) #[22 12 87  5 59 50 22 63 61  2 57 11 79 79  7]
