import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df = students.merge(subjects, how="cross")
    counts = examinations.groupby(["student_id", "subject_name"]).size().reset_index(name="attended_exams")
    result = df.merge(counts, on=["student_id", "subject_name"], how="left")
    result["attended_exams"] = result["attended_exams"].fillna(0).astype(int)
    return result.sort_values(["student_id", "subject_name"])