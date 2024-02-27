#let's calculate average ages of 10 groups

averages = [
    np.mean(sample1), 
    np.mean(sample2), 
    np.mean(sample3), 
    np.mean(sample4), 
    np.mean(sample5), 
    np.mean(sample6), 
    np.mean(sample7), 
    np.mean(sample8), 
    np.mean(sample9), 
    np.mean(sample10)
]

print(averages) # [47.68, 45.13, 43.76, 43.54, 46.88, 41.8, 53.27, 45.4, 44.4, 41.38]

print(np.mean(averages)) # 45.324

print(f"Population mean: {np.mean(our_population)}") # Population mean: 44.5015
