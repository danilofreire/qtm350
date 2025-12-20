class GradeCalculator:
    """
    A class to calculate final grades based on assignments, quizzes, and a final project,
    following a predefined grading scale and weights.
    """

    def __init__(self):
        # Grading scale (percentage-based)
        self.grading_scale = [
            (93.0, 100.0, "A"),
            (90.0, 92.9, "A-"),
            (87.0, 89.9, "B+"),
            (83.0, 86.9, "B"),
            (80.0, 82.9, "B-"),
            (77.0, 79.9, "C+"),
            (73.0, 76.9, "C"),
            (70.0, 72.9, "C-"),
            (67.0, 69.9, "D+"),
            (60.0, 66.9, "D"),
            (0.0, 59.9, "F"),
        ]

    def calculate_weighted_grade(self, assignments, quizzes, final_project):
        """
        Calculates the weighted grade based on the provided grades.

        Args:
            assignments (list): List of assignment grades (0–10).
            quizzes (list): List of quiz grades (0–10).
            final_project (float): Grade for the final project (0–10).

        Returns:
            float: Weighted grade as a percentage (0–10 scale).
        """
        # Calculate averages
        assignment_avg = sum(assignments) / len(assignments) if assignments else 0
        quiz_avg = sum(quizzes) / len(quizzes) if quizzes else 0

        # Calculate weighted grade
        weighted_grade = (
            (assignment_avg * 0.5) + (quiz_avg * 0.3) + (final_project * 0.2)
        )
        return round(weighted_grade, 2)

    def map_to_letter_grade(self, percentage_grade):
        """
        Maps a percentage grade to a letter grade based on the grading scale.

        Args:
            percentage_grade (float): Percentage grade (0–10 scale).

        Returns:
            str: Corresponding letter grade.
        """
        for lower_bound, upper_bound, letter_grade in self.grading_scale:
            if lower_bound <= percentage_grade <= upper_bound:
                return letter_grade
        return "F"  # Default to F if no match (shouldn't happen)

    def calculate_final_grade(self, assignments, quizzes, final_project):
        """
        Calculates the final grade and maps it to a letter grade.

        Args:
            assignments (list): List of assignment grades (0–10).
            quizzes (list): List of quiz grades (0–10).
            final_project (float): Grade for the final project (0–10).

        Returns:
            dict: Dictionary containing the percentage grade and letter grade.
        """
        # Validate inputs
        if not all(0 <= grade <= 10 for grade in assignments + quizzes + [final_project]):
            raise ValueError("All grades must be between 0 and 10.")

        # Calculate weighted grade (0-10 scale)
        weighted_grade = self.calculate_weighted_grade(assignments, quizzes, final_project)
        
        # Convert to percentage (0-100 scale) for letter grade mapping
        percentage_grade = weighted_grade * 10

        # Map to letter grade
        letter_grade = self.map_to_letter_grade(percentage_grade)

        return {
            "percentage_grade": weighted_grade,  # Keep original 0-10 scale for consistency
            "letter_grade": letter_grade,
        }

# Example usage

# assignments = [8.5, 9.0, 7.0, 8.0, 10.0, 9.5, 8.8, 9.2, 7.5, 8.5]
# quizzes = [7.8, 8.5, 9.0, 6.0, 8.8]
# final_project = 9.3

# calculator = GradeCalculator()
# result = calculator.calculate_final_grade(assignments, quizzes, final_project)

# print(result)