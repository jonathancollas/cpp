from random import randint

# create a new file if it does not exist:
f = open("sample.txt", "w")
f.write("price" + "\t" + "cost" + "\t" + "sell" +
        "\t" + "budget" + "\t" + "buy" + "\n")

# set price value to 1 for a start...
iPrice = 1
# ... and loop until it reaches 10
while iPrice <= 10:
    i = 0

    # create a thousand samples for each price value
    while i < 1000:
        iCost = randint(1, 10)
        iBudget = randint(1, 10)

        if iCost <= iPrice:
            bSell = True
        else:
            bSell = False

        if iBudget >= iPrice:
            bBuy = True
        else:
            bBuy = False

        # print in file (price, cost, budget, sell, buy) with tabs and return :)
        f.write(str(iPrice) + "\t" + str(iCost) + "\t" +
                str(bSell) + "\t" + str(iBudget) + "\t" + str(bBuy) + "\n")

        i += 1

    iPrice += 1

f.close()
