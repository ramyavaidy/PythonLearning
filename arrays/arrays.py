exp=[2200,2350,2600,2130,2190]

extra_dollars_in_Feb = exp[1]-exp[0]
print("Extra dollars spent in February compared to January:", extra_dollars_in_Feb)

first_three_months_exp = exp[0:3]
total_exp_first_three_months = sum(first_three_months_exp)
print("Total expenses for the first three months:", total_exp_first_three_months)

for i in range(len(exp)):
    if exp[i] == 2000:
        print("Expenses were exactly $2000 in month", i+1)
        break

exp.append(1980)
print("Expenses after adding June:", exp)

exp[3] = exp[3] + 200
print("Expenses after adding $200 to April:", exp)