import pymysql.cursors
#

#
# try:
#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT * FROM `VIS_ACTIVE_STUDENTS`"
#         cursor.execute(sql)
#         result = cursor.fetchone()
#         print(result)
# finally:
#     connection.close()
from db import create_connection
from utils import is_debug


def get_data_for_task_1(module_name: str) -> dict:
    # db = create_connection()
    # try:
    #     with db.cursor() as cursor:
    #         sql = """
    #             SELECT * FROM
    #         """
    #         result = cursor.execute(sql)
    #         return result.fetch_all()
    #
    # finally:
    #     db.close()

    return [
        {
            "moduleName": "Math",
            "type": "bachelor",
            "numberOfStudents": 60,
            "numberPerSemester": {
                "semester_1": 10,
                "semester_2": 20,
                "semester_3": 0,
                "semester_4": 5,
                "semester_5": 15,
                "semester_6": 10
            }
        },
        {
            "moduleName": "Advanced Biology",
            "type": "master",
            "numberOfStudents": 25,
            "numberPerSemester": {
                "semester_1": 15,
                "semester_2": 8,
                "semester_3": 7,
                "semester_4": 0
            }
        }
    ]


def get_curriculum() -> dict:

    if is_debug() is False:

        db = create_connection()
        try:
            with db.cursor() as cursor:
                sql = """
                    SELECT DISTINCT CURRICULUM_NR, CURRICULUM_NAME
                    FROM VIS_CURRICULUM_VERSION
                    WHERE DEGREE_NAME={}
                    GROUP BY CURRICULUM_NAME
                """

                bachelors_sql = sql.format("'Bachelor of Science'")
                cursor.execute(bachelors_sql)
                bachelors = cursor.fetchall()

                masters_sql = sql.format("'Master of Science'")
                cursor.execute(masters_sql)
                masters = cursor.fetchall()

                return {
                    "bachelors": bachelors,
                    "masters": masters
                }

        finally:
            db.close()

    else:
        return {
            "bachelors": [
                {
                    "curriculum_nr": 20,
                    "name": "Math",
                },
                {
                    "curriculum_nr": 21,
                    "name": "Physics",
                }
            ],
            "masters": [
                {
                    "curriculum_nr": 31,
                    "name": "Advanced Math",
                },
                {
                    "curriculum_nr": 32,
                    "name": "Biology",
                }
            ]
        }
