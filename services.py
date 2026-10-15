# services.py
from typing import List, Dict, Any
from config import (
    GRADE_A_THRESHOLD, GRADE_B_THRESHOLD, GRADE_C_THRESHOLD, GRADE_D_THRESHOLD,
    GRADE_A, GRADE_B, GRADE_C, GRADE_D, GRADE_F
)

def calculate_grade(score: float) -> str:
    """
    Tələbənin balına əsasən Grade (A, B, C, D, F) hesablayır.
    """
    if score >= GRADE_A_THRESHOLD:
        return GRADE_A
    elif score >= GRADE_B_THRESHOLD:
        return GRADE_B
    elif score >= GRADE_C_THRESHOLD:
        return GRADE_C
    elif score >= GRADE_D_THRESHOLD:
        return GRADE_D
    else:
        return GRADE_F

def calculate_statistics(students: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Tələbələrin siyahısına əsasən ümumi statistikaları hesablayır.
    """
    if not students:
        return {
            "total_students": 0,
            "average_score": 0.0,
            "highest_score": 0.0,
            "lowest_score": 0.0
        }

    scores = [student["score"] for student in students]
    total_students = len(scores)
    average_score = round(sum(scores) / total_students, 1)
    highest_score = max(scores)
    lowest_score = min(scores)

    return {
        "total_students": total_students,
        "average_score": average_score,
        "highest_score": highest_score,
        "lowest_score": lowest_score
    }