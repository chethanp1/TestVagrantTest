basket = [
    {"product": "Leather wallet", "unitprice": 1100, "GST": 18, "quantity": 1},
    {"product": "Umbrella", "unitprice": 900, "GST": 12, "quantity": 4},
    {"product": "Cigarette", "unitprice": 200, "GST": 28, "quantity": 3},
    {"product": "Honey", "unitprice": 100, "GST": 0, "quantity": 2},
]

total_amount = 0

max_gst_product = None
max_gst_amount = 0

for item in basket:
    unit_price = item["unitprice"]
    gst_percentage = item["GST"]
    quantity = item["quantity"]

    # Calculate the GST amount for the product
    gst_amount = (unit_price * gst_percentage / 100) * quantity

    # Calculate the total amount for the product after discount
    total_price = (unit_price * quantity) - (0.05 * unit_price * quantity)  # 5% discount applied

    # Add the total price to the overall total amount
    total_amount += total_price

    if gst_amount > max_gst_amount:
        max_gst_amount = gst_amount
        max_gst_product = item["product"]

# Print the results
print("Product with maximum GST amount:", max_gst_product)
print("Total amount to be paid to the shopkeeper:", total_amount)

