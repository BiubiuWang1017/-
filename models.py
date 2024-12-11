class College:
    def __init__(self, college_id, name, description):
        self.college_id = college_id
        self.name = name
        self.description = description

class Discipline:
    def __init__(self, discipline_id, college_id, name, description):
        self.discipline_id = discipline_id
        self.college_id = college_id
        self.name = name
        self.description = description

class SecondaryDiscipline:
    def __init__(self, discipline_id, primary_discipline_id, name, description):
        self.discipline_id = discipline_id
        self.primary_discipline_id = primary_discipline_id
        self.name = name
        self.description = description

class Instructor:
    def __init__(self, instructor_id, name, title, photo, bio, email, phone, secondary_discipline_id):
        self.instructor_id = instructor_id
        self.name = name
        self.title = title
        self.photo = photo
        self.bio = bio
        self.email = email
        self.phone = phone
        self.secondary_discipline_id = secondary_discipline_id

class EnrollmentCatalog:
    def __init__(self, catalog_id, college_id, primary_discipline_id, secondary_discipline_id, instructor_id, admission_subjects, re_exam_subjects, annual_quota, additional_quota, year, instructor_type, has_enrollment_qualification):
        self.catalog_id = catalog_id
        self.college_id = college_id
        self.primary_discipline_id = primary_discipline_id
        self.secondary_discipline_id = secondary_discipline_id
        self.instructor_id = instructor_id
        self.admission_subjects = admission_subjects
        self.re_exam_subjects = re_exam_subjects
        self.annual_quota = annual_quota
        self.additional_quota = additional_quota
        self.year = year
        self.instructor_type = instructor_type
        self.has_enrollment_qualification = has_enrollment_qualification
