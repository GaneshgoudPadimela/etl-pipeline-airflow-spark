from src.transform import aggregate_by_product
def test_aggregate_and_dedupe():
    rows=[{'order_id':'1','product_id':'p1','quantity':'2','amount':'10.0'},{'order_id':'1','product_id':'p1','quantity':'2','amount':'10.0'},{'order_id':'2','product_id':'p1','quantity':'1','amount':'5.0'}]
    out=aggregate_by_product(rows); assert out['p1']['quantity']==3; assert out['p1']['amount']==15.0
