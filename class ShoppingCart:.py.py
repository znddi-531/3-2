class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, price: int, quantity: int = 1):
        if name in self.items:
            self.items[name]["qty"] += quantity
        else:
            self.items[name] = {"price": price, "qty": quantity}
        print(f"[추가] {name} {quantity}개 담김")

    def get_total(self) -> int:
        return sum(item["price"] * item["qty"] for item in self.items.values())

    def print_receipt(self):
        print("\n--- 영수증 ---")
        for name, data in self.items.items():
            subtotal = data["price"] * data["qty"]
            print(f"{name:<6} x{data['qty']} : {subtotal:,}원")
        print(f"총 결제액: {self.get_total():,}원\n")

cart = ShoppingCart()
cart.add_item("사과", 1500, 3)
cart.add_item("우유", 2500, 1)
cart.add_item("사과", 1500, 2)
cart.print_receipt()