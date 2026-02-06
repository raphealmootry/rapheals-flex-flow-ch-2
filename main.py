import random

class RealEstateQuiz:
    def __init__(self):
        self.score = 0
        # Data based on Unit 5: Forms of Real Estate Ownership (9th Ed)
        self.questions = [
            {
                "question": "Which form of ownership involves a single individual or entity holding title?",
                "options": ["A. Tenancy in Common", "B. Joint Tenancy", "C. Ownership in Severalty", "D. Community Property"],
                "answer": "C"
            },
            {
                "question": "The 'Right of Survivorship' is a key characteristic of which ownership type?",
                "options": ["A. Tenancy in Common", "B. Joint Tenancy", "C. Leasehold Estate", "D. Determinable Fee"],
                "answer": "B"
            },
            {
                "question": "Which of the following is NOT one of the 'Four Unities' (PITT) required for Joint Tenancy?",
                "options": ["A. Possession", "B. Interest", "C. Trust", "D. Title"],
                "answer": "C"
            },
            {
                "question": "In a Condominium, what type of interest does an owner hold in the common elements?",
                "options": ["A. Severalty", "B. Undivided interest as tenants in common", "C. Proprietary lease", "D. Joint tenancy"],
                "answer": "B"
            }
        ]

    def run_quiz(self):
        print("🏠 Starting Unit 5: Real Estate Ownership Quiz 🏠")
        print("-----------------------------------------------")
        random.shuffle(self.questions)
        
        for i, q in enumerate(self.questions):
            print(f"\nQuestion {i+1}: {q['question']}")
            for option in q['options']:
                print(option)
            
            guess = input("Your Answer (A, B, C, or D): ").upper()
            
            if guess == q['answer']:
                print("✅ Correct! You're crushing it.")
                self.score += 1
            else:
                print(f"❌ Not quite. The correct answer was {q['answer']}.")

        print("-----------------------------------------------")
        print(f"Final Score: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    quiz = RealEstateQuiz()
    quiz.run_quiz()
