import csv, io
SAMPLE = 'order_id,product_id,quantity,amount,order_date\n1,p-100,2,49.99,2026-10-01\n2,p-100,1,24.99,2026-10-01\n3,p-200,3,89.97,2026-10-02\n'
def extract_orders():
    return list(csv.DictReader(io.StringIO(SAMPLE)))
if __name__ == '__main__': print(extract_orders())
