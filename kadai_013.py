def total_price(price, tax):
    total_price = price + tax
    
    tax = price * 0.1
    print(f"{price}円(税込：{total_price}円)")