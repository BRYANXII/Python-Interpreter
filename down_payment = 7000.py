down_payment = 7000
mechanical_warranty = 4800
ally_monthly = 551
mobility_monthly = 473
Ally_OG_Balance = 32048
Mobility_OG_Balance = 25360
Real_Starting_Balance = Ally_OG_Balance - mechanical_warranty
print(f"Real Starting Balance: {Real_Starting_Balance}")

spent_at_ally = Real_Starting_Balance - Mobility_OG_Balance
print(f"Spent at Ally: {spent_at_ally}")

spent_at_mobility_so_far = mobility_monthly*10 
print(f"Spent at Mobility So far: {spent_at_mobility_so_far}")

remaining_balance = Mobility_OG_Balance - spent_at_mobility_so_far

cost_to_me = spent_at_mobility_so_far + spent_at_ally + down_payment

DP_plus_mobility = down_payment + spent_at_mobility_so_far


print(f"The cost to me is: {cost_to_me}")

print(f"Downpayment + Spent at Mobility so far: {DP_plus_mobility}")

difference = cost_to_me - DP_plus_mobility

print(f"Difference between total cost and cost at mobility only: {difference}")

print(f"Remaining Balance: {remaining_balance}")