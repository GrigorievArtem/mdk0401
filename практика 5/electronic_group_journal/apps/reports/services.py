from django.db.models import Avg, Count
from apps.clients.models import StudyGroup, Student
from apps.orders.models import Grade, Attendance

def get_journal_stats():
    return {
        "groups_count": StudyGroup.objects.count(),
        "students_count": Student.objects.count(),
        "grades_count": Grade.objects.count(),
        "average_grade": Grade.objects.aggregate(value=Avg("value"))["value"] or 0,
        "absences_count": Attendance.objects.filter(status="absent").count(),
    }

def group_performance():
    result = []
    for group in StudyGroup.objects.all():
        student_ids = Student.objects.filter(group=group).values_list("id", flat=True)
        avg = Grade.objects.filter(student_id__in=student_ids).aggregate(value=Avg("value"))["value"]
        result.append({"group": group.name, "students": len(student_ids),
                       "average": round(avg, 2) if avg is not None else 0})
    return result
