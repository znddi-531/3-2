class GradeManager:
    def __init__(self):
        self.students = {}

    def add_student(self, name: str, scores: list[int]):
        if not scores:
            print(f"[경고] {name} 학생의 점수가 없습니다.")
            return
        self.students[name] = scores

    def calculate_average(self, name: str) -> float:
        scores = self.students.get(name)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)

    def print_report(self):
        print("=" * 35)
        print(" 이름     |   평균 점수   | 합격 여부")
        print("=" * 35)
        for name in self.students:
            avg = self.calculate_average(name)
            status = "PASS" if avg >= 60 else "FAIL"
            print(f" {name:<8} |   {avg:>6.2f}점   |   {status}")
        print("=" * 35)

def main():
    manager = GradeManager()
    manager.add_student("철수", [80, 95, 70])
    manager.add_student("영희", [90, 85, 92])
    manager.add_student("민수", [50, 60, 45])
    manager.print_report()

if __name__ == "__main__":
    main()