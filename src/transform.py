from collections import defaultdict
from src.extract import extract_orders
def aggregate_by_product(rows):
    totals = defaultdict(lambda: {'quantity': 0, 'amount': 0.0})
    seen = set()
    for r in rows:
        if r['order_id'] in seen: continue
        seen.add(r['order_id'])
        t = totals[r['product_id']]; t['quantity'] += int(r['quantity']); t['amount'] += float(r['amount'])
    return dict(totals)
if __name__ == '__main__': print(aggregate_by_product(extract_orders()))
