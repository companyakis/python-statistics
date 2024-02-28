# let's look at covariance b/w tip & total_bill

print(data_tips[["total_bill", "tip"]].cov())

"""
            total_bill       tip
total_bill   79.252939  8.323502
tip           8.323502  1.914455
"""
