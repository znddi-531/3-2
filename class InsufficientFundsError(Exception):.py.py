class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("입금액은 0원보다 커야 합니다.")
        self.balance += amount
        print(f"[입금] {amount:,}원 | 잔액: {self.balance:,}원")

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise InsufficientFundsError(f"잔액 부족 (현재 잔액: {self.balance:,}원)")
        self.balance -= amount
        print(f"[출금] {amount:,}원 | 잔액: {self.balance:,}원")

def main():
    account = BankAccount("홍길동", 10000)
    account.deposit(5000)

    try:
        account.withdraw(8000)
        account.withdraw(10000)
    except InsufficientFundsError as e:
        print(f"[오류] {e}")

if __name__ == "__main__":
    main()