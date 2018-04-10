from pprint import pprint
##prices = {
##'ACME': 45.23,
##'AAPL': 612.78,
##'IBM': 205.55,
##'HPQ': 37.20,
##'FB': 10.75
##}
##
##min_price = min(zip(prices.values(), prices.keys()))
##max_price = max(zip(prices.values(), prices.keys()))
##
##print('max is: %f:[%s], min is : %f[%s]' % (max_price[0], max_price[1],
##                                           min_price[0], min_price[1]))
##
##prices_sorted = sorted(zip(prices.values(), prices.keys()), reverse=True)
##pprint(prices_sorted, indent=4, width=40)
##a = {
##'x' : 1,
##'y' : 2,
##'z' : 3
##}
##
##b = {
##'w' : 10,
##'x' : 11,
##'y' : 2
##}
##
##print(a.keys() & b.keys())
##print(a.keys() - b.keys())
##print(a.items() & b.items())
##
##c = {key:a[key] for key in a.keys() - {'z', 'w'}}
##print(c)
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))
