# import pymysql.cursors
#
# # Connect to the database
# connection = pymysql.connect(host='127.0.0.1',
#                              port=8889,
#                              user='root',
#                              password='root',
#                              db='ATHENS15',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)
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


def get_data_for_task_1(module_name: str) -> dict:
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
