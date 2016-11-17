import functools
from itertools import groupby

from db import create_connection
from utils import is_debug


def get_curriculum() -> dict:
    if is_debug() is False:

        db = create_connection()
        try:
            with db.cursor() as cursor:
                sql = """
                    SELECT DISTINCT curriculum_code as curriculumCode, curriculum_name as curriculumName
                    FROM VIS_CURRICULUM_VERSION
                    WHERE DEGREE_NAME={}
                    GROUP BY curriculumName
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
                    "curriculumName": "Math",
                },
                {
                    "curriculum_code": 21,
                    "curriculumName": "Physics",
                }
            ],
            "masters": [
                {
                    "curriculum_code": 31,
                    "curriculumName": "Advanced Math",
                },
                {
                    "curriculum_code": 32,
                    "curriculumName": "Biology",
                }
            ]
        }


def get_data_for_task_1(curriculum_code: str) -> dict:
    if is_debug() is False:
        db = create_connection()
        try:
            with db.cursor() as cursor:
                sql = """
                    SELECT * FROM VIS_CALC_TASK_1 WHERE curriculum_code={} and SEMESTER_VALUE <= 6 AND NODE_TITLE!=""
                """.format("'" + curriculum_code + "'")
                cursor.execute(sql)
                data = cursor.fetchall()

                modules = []
                data_sorted = list(sorted(data, key=lambda x: x["NODE_TITLE"]))
                for k, g in groupby(data_sorted, lambda x: x["NODE_TITLE"]):
                    modules.append(list(g))

                def convert_semesters(same_semesters):
                    module = {
                        "moduleId": same_semesters[0]["NODE_ID"],
                        "moduleName": same_semesters[0]["NODE_TITLE"],
                        "type": ("master" if same_semesters[0]["DEGREE_NAME"] == "Master of Science" else "bachelor"),
                        "numberPerSemester": {
                            "Semester 1": 0,
                            "Semester 2": 0,
                            "Semester 3": 0,
                            "Semester 4": 0
                        } if same_semesters[0]["DEGREE_NAME"] == "Master of Science" else {
                            "Semester 1": 0,
                            "Semester 2": 0,
                            "Semester 3": 0,
                            "Semester 4": 0,
                            "Semester 5": 0,
                            "Semester 6": 0
                        }
                    }

                    for m in same_semesters:
                        module["numberPerSemester"][("Semester " + str(m["SEMESTER_VALUE"]))] = m["SUCCESSFUL_STUDENTS"]

                    return module

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


def get_data_for_task_2(curriculum_code: str) -> list:
    if is_debug() is False:

        alphabet_splitter = [("A", "K"), ("K", "Z")]

        db = create_connection()
        try:
            with db.cursor() as cursor:
                sql = """
                    SELECT NODE_TITLE as moduleName, MEDIAN_SEMESTER as medianSemester, SEMESTER_TYPE_ID as recommendedSemester
                    FROM VIS_CALC_TASK_2
                    WHERE curriculum_code={} AND SEMESTER_TYPE_ID <= 6 AND MEDIAN_SEMESTER <= 6;
                    """.format("'" + curriculum_code + "'")

                cursor.execute(sql)
                data = cursor.fetchall()

                semesters = []
                data_sorted = list(sorted(data, key=lambda x: x["medianSemester"]))
                for k1, g1 in groupby(data_sorted, lambda x: x["medianSemester"]):
                    modules_parts = []
                    for start_spell, end_spell in alphabet_splitter:
                        modules = []
                        s_e_filtered = list(filter(lambda x: start_spell <= x["moduleName"][0] <= end_spell, g1))
                        for x in s_e_filtered:
                            modules.append({
                                "moduleName": x["moduleName"],
                                "recommendedSemester": x["recommendedSemester"]
                            })

                        modules_part = {
                            "name": "{}-{}".format(start_spell, end_spell),
                            "children": modules
                        }
                        modules_parts.append(modules_part)

                    semester = {
                        "medianSemester": k1,
                        "children": modules_parts
                    }
                    semesters.append(semester)

                return semesters

        finally:
            db.close()

    else:
        return [
            {
                "medianSemester": 1,
                "children": [
                    {
                        "name": "A-K",
                        "children": [
                            {
                                "moduleName": "Math",
                                "recommendedSemester": 1
                            },
                            {
                                "moduleName": "Biology",
                                "recommendedSemester": 2
                            }
                        ]
                    }
                ]
            },
            {
                "medianSemester": 2,
                "children": [
                    {
                        "name": "A-K",
                        "children": [
                            {
                                "moduleName": "Advanced Math",
                                "recommendedSemester": 1
                            },
                            {
                                "moduleName": "Advanced Biology",
                                "recommendedSemester": 2
                            }
                        ]
                    }
                ]
            }
        ]

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


def get_data_for_task_3() -> list:
    if is_debug() is False:

        db = create_connection()
        try:
            with db.cursor() as cursor:
                sql = """
                    SELECT *
                    FROM VIS_CALC_TASK_3;
                    """

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
