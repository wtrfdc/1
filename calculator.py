def calculate_total(price: float, quantity: int) -> float:
    """Validate quantity and return the rounded order total."""
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")
    subtotal = price * quantity
    return round(subtotal, 2)


if __name__ == "__main__":
    total = calculate_total(120.0, 3)
    print(f"Order total: NT${total:.0f}")
