def classify_order(
    amount,
    age,
    item_count,
    payment_approved,
    premium_client,
    address_confirmed,
):
    if payment_approved != "yes":
        return "BLOCKED", "payment not approved"
    elif age < 18:
        return "BLOCKED", "underage client"
    elif address_confirmed != "yes":
        return "BLOCKED", "address not confirmed"
    elif amount > 1000:
        return "UNDER REVIEW", "order amount above 1000"
    elif item_count >= 10:
        return "UNDER REVIEW", "high item count"
    elif premium_client != "yes" and amount > 500:
        return "UNDER REVIEW", "non-premium client with order above 500"
    else:
        return "APPROVED", "order within normal rules"
