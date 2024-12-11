import pyodbc
from database_config import connection_string
from models import College, Discipline, SecondaryDiscipline, Instructor, EnrollmentCatalog


class BaseDao:
    def __init__(self, conn_str):
        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.conn.commit()

class CollegeDao(BaseDao):
    def __init__(self, conn_str):
        super().__init__(conn_str)

    def add_college(self, college):
        query = "INSERT INTO [dbo].[学院] ([学院ID], [学院名称], [学院概述]) VALUES (?, ?, ?)"
        self.execute_query(query, (college.college_id, college.name, college.description))

    def get_college_by_id(self, college_id):
        query = "SELECT * FROM [dbo].[学院] WHERE [学院ID] = ?"
        self.cursor.execute(query, (college_id,))
        return self.cursor.fetchone()

    def delete_college(self, college_id):
        query = "DELETE FROM [dbo].[学院] WHERE [学院ID] = ?"
        self.execute_query(query, (college_id,))

    def update_college(self, college):
        query = "UPDATE [dbo].[学院] SET [学院名称] = ?, [学院概述] = ? WHERE [学院ID] = ?"
        self.execute_query(query, (college.name, college.description, college.college_id))

class DisciplineDao(BaseDao):
    def __init__(self, conn_str):
        super().__init__(conn_str)

    def add_discipline(self, discipline):
        query = "INSERT INTO [dbo].[一级学科] ([学科ID], [学院ID], [学科名称], [学科概述]) VALUES (?, ?, ?, ?)"
        self.execute_query(query, (discipline.discipline_id, discipline.college_id, discipline.name, discipline.description))

    def get_discipline_by_id(self, discipline_id):
        query = "SELECT * FROM [dbo].[一级学科] WHERE [学科ID] = ?"
        self.cursor.execute(query, (discipline_id,))
        return self.cursor.fetchone()

    def delete_discipline(self, discipline_id):
        query = "DELETE FROM [dbo].[一级学科] WHERE [学科ID] = ?"
        self.execute_query(query, (discipline_id,))

    def update_discipline(self, discipline):
        query = "UPDATE [dbo].[一级学科] SET [学科名称] = ?, [学科概述] = ? WHERE [学科ID] = ?"
        self.execute_query(query, (discipline.name, discipline.description, discipline.discipline_id))

class SecondaryDisciplineDao(BaseDao):
        def __init__(self, conn_str):
            super().__init__(conn_str)

        def add_secondary_discipline(self, secondary_discipline):
            query = "INSERT INTO [dbo].[二级学科] ([学科ID], [一级学科ID], [学科名称], [学科概述]) VALUES (?, ?, ?, ?)"
            self.execute_query(query, (
            secondary_discipline.discipline_id, secondary_discipline.primary_discipline_id, secondary_discipline.name,
            secondary_discipline.description))

        def get_secondary_discipline_by_id(self, discipline_id):
            query = "SELECT * FROM [dbo].[二级学科] WHERE [学科ID] = ?"
            self.cursor.execute(query, (discipline_id,))
            return self.cursor.fetchone()

        def delete_secondary_discipline(self, discipline_id):
            query = "DELETE FROM [dbo].[二级学科] WHERE [学科ID] = ?"
            self.execute_query(query, (discipline_id,))

        def update_secondary_discipline(self, secondary_discipline):
            query = "UPDATE [dbo].[二级学科] SET [学科名称] = ?, [学科概述] = ? WHERE [学科ID] = ?"
            self.execute_query(query, (
            secondary_discipline.name, secondary_discipline.description, secondary_discipline.discipline_id))

class InstructorDao(BaseDao):
        def __init__(self, conn_str):
            super().__init__(conn_str)

        def add_instructor(self, instructor):
            query = """
            INSERT INTO [dbo].[导师] ([导师ID], [导师姓名], [导师职称], [导师照片], [导师简介], [导师邮箱], [导师电话], [所在二级学科ID])
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            self.execute_query(query, (
                instructor.instructor_id, instructor.name, instructor.title, instructor.photo,
                instructor.bio, instructor.email, instructor.phone, instructor.secondary_discipline_id))

        def get_instructor_by_id(self, instructor_id):
            query = "SELECT * FROM [dbo].[导师] WHERE [导师ID] = ?"
            self.cursor.execute(query, (instructor_id,))
            return self.cursor.fetchone()

        def delete_instructor(self, instructor_id):
            query = "DELETE FROM [dbo].[导师] WHERE [导师ID] = ?"
            self.execute_query(query, (instructor_id,))

        def update_instructor(self, instructor):
            query = """
            UPDATE [dbo].[导师]
            SET [导师姓名] = ?, [导师职称] = ?, [导师照片] = ?, [导师简介] = ?, [导师邮箱] = ?, [导师电话] = ?, [所在二级学科ID] = ?
            WHERE [导师ID] = ?
            """
            self.execute_query(query, (
                instructor.name, instructor.title, instructor.photo, instructor.bio,
                instructor.email, instructor.phone, instructor.secondary_discipline_id, instructor.instructor_id))

class EnrollmentCatalogDao(BaseDao):
        def __init__(self, conn_str):
            super().__init(conn_str)

        def add_enrollment_catalog(self, catalog):
            query = """
            INSERT INTO [dbo].[招生目录] ([目录ID], [学院ID], [一级学科ID], [二级学科ID], [导师ID], [初试科目], [复试科目], [年度总指标], [补充指标], [年度], [导师身份], [是否具有招生资格]) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            self.execute_query(query, (
            catalog.catalog_id, catalog.college_id, catalog.primary_discipline_id, catalog.secondary_discipline_id,
            catalog.instructor_id, catalog.admission_subjects, catalog.re_exam_subjects, catalog.annual_quota,
            catalog.additional_quota, catalog.year, catalog.instructor_type, catalog.has_enrollment_qualification))

        def get_enrollment_catalog_by_id(self, catalog_id):
            query = "SELECT * FROM [dbo].[招生目录] WHERE [目录ID] = ?"
            self.cursor.execute(query, (catalog_id,))
            return self.cursor.fetchone()

        def delete_enrollment_catalog(self, catalog_id):
            query = "DELETE FROM [dbo].[招生目录] WHERE [目录ID] = ?"
            self.execute_query(query, (catalog_id,))

        def update_enrollment_catalog(self, catalog):
            query = """
            UPDATE [dbo].[招生目录] SET [学院ID] = ?, [一级学科ID] = ?, [二级学科ID] = ?, [导师ID] = ?, [初试科目] = ?, [复试科目] = ?, [年度总指标] = ?, [补充指标] = ?, [年度] = ?, [导师身份] = ?, [是否具有招生资格] = ? WHERE [目录ID] = ?
            """
            self.execute_query(query, (
            catalog.college_id, catalog.primary_discipline_id, catalog.secondary_discipline_id, catalog.instructor_id,
            catalog.admission_subjects, catalog.re_exam_subjects, catalog.annual_quota, catalog.additional_quota,
            catalog.year, catalog.instructor_type, catalog.has_enrollment_qualification, catalog.catalog_id))
