from Juggling import Pattern


def find_transactions(siteswap1, siteswap2):
    transaction_to = __find_one_way_transaction(siteswap1, siteswap2)
    transaction_from = __find_one_way_transaction(siteswap2, siteswap1)
    return siteswap1 + transaction_to + transaction_from


def __find_one_way_transaction(siteswap1, siteswap2):

