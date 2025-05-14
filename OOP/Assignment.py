class Pupil:

    def __init__(self, name, attendance):
        self.name = name
        self.scores = {}
        self.attendance = attendance

    def add_subject(self, subject, score):
        if 0 <= score <= 100:
            self.scores[subject] = score
        else:
            print("Subject must be between 0 and 100")

    def update_score(self, subject, score):
        if subject in self.scores:
            print(self.scores)
            if 0 <= score <= 100:
                self.scores[subject] = score
            else:
                print("Subject must be between 0 and 100")
        else:
            print("Subject not found")

    def calculate_average(self):
        if self.scores:
            return sum(self.scores.values()) / len(self.scores)
        else:
            return 0

    def calculate_percentage(self):
        stud_marks = sum(self.scores.values())
        total_marks = len(self.scores) * 100
        if total_marks > 0:
            return (stud_marks / total_marks) * 100
        else:
            return 0

    def student_status(self):
        if self.calculate_average() >= 50 and self.attendance >= 75:
            return f"{self.name} passed"
        else:
            return f"{self.name} failed"

    def view_details(self):
        print(f"Student name: {self.name}")
        print(f"Subjects and Scores: {self.scores}")
        print(f"Attendance: {self.attendance}")
        print(f"Average Score: {self.calculate_average():.2f}")
        print(f"Overall Percentage: {self.calculate_percentage():.0f}%")
        print(f"Promotion Status: {self.student_status()}")

# Uploading Students
pupil1 = Pupil("Ahmad", 100)
pupil1.add_subject("Maths", 100)
pupil1.add_subject("English", 100)
pupil1.add_subject("Physics", 100)
pupil1.add_subject("Chemistry", 100)
pupil1.add_subject("Biology", 100)

pupil2 = Pupil("John", 83)
pupil2.add_subject("Maths", 58)
pupil2.add_subject("English", 80)
pupil2.add_subject("Physics", 77)
pupil2.add_subject("Chemistry", 54)
pupil2.add_subject("Biology", 67)

pupil3 = Pupil("Lisa", 45)
pupil3.add_subject("Maths", 62)
pupil3.add_subject("English", 49)
pupil3.add_subject("Physics", 55)
pupil3.add_subject("Chemistry", 42)
pupil3.add_subject("Biology", 67)

pupil4 = Pupil("Mary", 100)
pupil4.add_subject("Maths", 56)
pupil4.add_subject("English", 75)
pupil4.add_subject("Physics", 82)
pupil4.add_subject("Chemistry", 84)
pupil4.add_subject("Biology", 60)

pupil5 = Pupil("Sodo", 100)
pupil5.add_subject("Maths", 92)
pupil5.add_subject("English", 60)
pupil5.add_subject("Physics", 43)
pupil5.add_subject("Chemistry", 87)
pupil5.add_subject("Biology", 67)


# Displaying Pupils
pupils = [pupil1, pupil2, pupil3, pupil4, pupil5]
for pupil in pupils:
    pupil.view_details()
    print()
