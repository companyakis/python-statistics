# let's look at correlation b/w tip & total_bill

# positive relationship

print(data_tips[["total_bill", "tip"]].corr())

"""
            total_bill       tip
total_bill    1.000000  0.675734
tip           0.675734  1.000000
"""
