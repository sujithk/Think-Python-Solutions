bookcost=24
numbooks=60
def cost(numbooks):
	bulkbookcost=((bookcost*60)*numbooks)
	shipcost=(3.0+(0.75*(numbooks-1)))
	totalcost=bulkbookcost+shipcost
	return totalcost

print cost(numbooks)
