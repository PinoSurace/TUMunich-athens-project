import functools
from itertools import groupby

from db import create_connection
from utils import is_debug


def get_data_for_task_1(curriculum_code: str) -> dict:
    if is_debug() is False:
        db = create_connection()
        try:
            with db.cursor() as cursor:
                sql = """
                    SELECT * FROM VIS_CALC_TASK_1 WHERE CURRICULUM_CODE={}
                """.format("'" + curriculum_code + "'")
                cursor.execute(sql)
                data = cursor.fetchall()

                modules = []
                data_sorted = list(sorted(data, key=lambda x: x["NODE_TITLE"]))
                for k, g in groupby(data_sorted, lambda x: x["NODE_TITLE"]):
                    modules.append(list(g))

                def convert_semesters(same_semesters):
                    return {
                        "module_id": same_semesters[0]["NODE_ID"],
                        "module_name": same_semesters[0]["NODE_TITLE"],
                        "type": ("master" if same_semesters[0]["DEGREE_NAME"] == "Master of Science" else "bachelor"),
                        "numberPerSemester": functools.reduce(lambda s, m: {**s, **{
                            "Semester " + str(m["SEMESTER_VALUE"]): m["SUCCESSFUL_STUDENTS"]}},
                                                              same_semesters, {})
                    }

                return list(map(convert_semesters, modules))

        finally:
            db.close()

    else:
        return [
            {
                "moduleId": 1,
                "moduleName": "Math",
                "type": "bachelor",
                "numberOfStudents": 60,
                "numberPerSemester": {
                    "Semester 1": 10,
                    "Semester 2": 20,
                    "Semester 3": 0,
                    "Semester 4": 5,
                    "Semester 5": 15,
                    "Semester 6": 10
                }
            },
            {
                "moduleId": 2,
                "moduleName": "Advanced Biology",
                "type": "master",
                "numberOfStudents": 25,
                "numberPerSemester": {
                    "Semester 1": 15,
                    "Semester 2": 8,
                    "Semester 3": 7,
                    "Semester 4": 0
                }
            }
        ]


def get_curriculum() -> dict:
    if is_debug() is False:

        db = create_connection()
        try:
            with db.cursor() as cursor:
                sql = """
                    SELECT DISTINCT curriculum_code, curriculum_name
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
                    "curriculum_code": 20,
                    "curriculum_name": "Math",
                },
                {
                    "curriculum_code": 21,
                    "curriculum_name": "Physics",
                }
            ],
            "masters": [
                {
                    "curriculum_code": 31,
                    "curriculum_name": "Advanced Math",
                },
                {
                    "curriculum_code": 32,
                    "curriculum_name": "Biology",
                }
            ]
        }


def get_data_for_task_2(curriculum_code: str) -> list:
    if is_debug() is False:

        db = create_connection()
        try:
            with db.cursor() as cursor:
                sql = """
                    SELECT NODE_TITLE as moduleName, MEDIAN_SEMESTER as medianSemester, SEMESTER_TYPE_ID as recommendedSemester
                    FROM VIS_CALC_TASK_2
                    WHERE CURRICULUM_CODE={} AND SEMESTER_TYPE_ID < 20;
                    """.format("'" + curriculum_code + "'")

                cursor.execute(sql)
                data = cursor.fetchall()

                return data

        finally:
            db.close()

    else:
        return [
            {
                "moduleName": "Math",
                "medianSemester": 1,
                "recommendedSemester": 1
            },
            {
                "moduleName": "Advanced Math",
                "medianSemester": 2,
                "recommendedSemester": 3
            },
            {
                "moduleName": "Biology",
                "medianSemester": 3,
                "recommendedSemester": 2
            },
        ]
