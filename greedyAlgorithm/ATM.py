def ATM(coin_list=[], cost=0, __actual_run=1):
    coin_list = sorted(coin_list, reverse=True)

    # List of coins that will be returned
    coins_list_final = []

    # Base case: when cost == 0
    if cost > 0:
        # Error
        if cost != 0 and len(coin_list) == 0:
            raise BaseException('It\'s not possible to get that cost with the actual coin_list')

        # Biggest coin <= actual cost
        if coin_list[0] <= cost:
            coins_list_final.append(coin_list[0])
            cost -= coin_list[0]

            new_coins = ATM(coin_list, cost, __actual_run + 1)
            coins_list_final.extend(new_coins)
            cost -= sum(new_coins)
        else:
            coin_list.pop(0)

            new_coins = ATM(coin_list, cost, __actual_run + 1)
            coins_list_final.extend(new_coins)
            cost -= sum(new_coins)

    # Error
    if (cost < 0):
        raise BaseException('It\'s not possible to get that cost with the actual coin_list')

    return coins_list_final


if __name__ == '__main__':
    print(ATM([1, 10, 2, 5, 20, 0.5], 57.5))
