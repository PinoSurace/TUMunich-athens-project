import datetime

from math import ceil

import pymysql.cursors


def get_last_node_id(db, cursor):
    sql = """
    SELECT NODE_ID
    FROM VIS_MODULE_NODE
    ORDER BY NODE_ID DESC
    LIMIT 1
    """
    cursor.execute(sql)
    data = cursor.fetchone()
    return data["NODE_ID"]


def create_calc_module(db, cursor):
    calc_module_drop = """
        DROP TABLE `VIS_CALC_MODULE`;
        """

    calc_module_create = """
        CREATE table `VIS_CALC_MODULE` AS
        SELECT mn.NODE_ID, mn.NODE_TITLE, cv.DEGREE_NAME, cv.CURRICULUM_NAME, cv.CURRICULUM_CODE, mn.SEMESTER_TYPE_ID
        FROM VIS_MODULE_NODE mn
        JOIN VIS_CURRICULUM_VERSION cv ON cv.CURRICULUM_NR=mn.CURRICULUM_NR;
    """

    print("CALC MODULE: dropping starts....")
    cursor.execute(calc_module_drop)
    print("CALC MODULE: dropping ends....")

    print("CALC MODULE: creating starts....")
    cursor.execute(calc_module_create)
    print("CALC MODULE: creating ends....")


def create_calc_semester(db, cursor):
    calc_semester_drop = """
        DROP TABLE `VIS_CALC_SEMESTER`;
    """

    calc_semester_create = """
        CREATE TABLE `VIS_CALC_SEMESTER` AS
        SELECT ns.NODE_ID, ns.SEMESTER_VALUE, COUNT(ns.ST_STUDIES_NR) AS SUCCESSFUL_STUDENTS
        FROM VIS_NODE_SEMESTER ns
        GROUP BY ns.NODE_ID;
    """

    print("CALC SEMESTER: dropping starts....")
    cursor.execute(calc_semester_drop)
    print("CALC SEMESTER: dropping ends....")

    print("CALC SEMESTER: creating starts....")
    cursor.execute(calc_semester_create)
    print("CALC SEMESTER: creating ends....")


def create_task_1(db, cursor):
    calc_task_1_drop = """
        DROP TABLE `VIS_CALC_TASK_1`;
        """

    calc_task_1_create = """
        CREATE TABLE `VIS_CALC_TASK_1` (
          `NODE_ID` INT(11) DEFAULT NULL,
          `NODE_TITLE` VARCHAR(256) DEFAULT NULL,
          `DEGREE_NAME` VARCHAR(200) DEFAULT NULL,
          `CURRICULUM_NAME` VARCHAR(100) DEFAULT NULL,
          `CURRICULUM_CODE` VARCHAR(100) DEFAULT NULL,
          `SEMESTER_VALUE` INT(11) DEFAULT NULL,
          `SUCCESSFUL_STUDENTS` BIGINT(21) NOT NULL DEFAULT '0'
        );
        """

    calc_task_1_insert = """
        INSERT INTO `VIS_CALC_TASK_1`
        SELECT DISTINCT cm.NODE_ID, cm.NODE_TITLE, cm.DEGREE_NAME, cm.CURRICULUM_NAME, cm.CURRICULUM_CODE, cs.SEMESTER_VALUE, cs.SUCCESSFUL_STUDENTS
        FROM VIS_CALC_MODULE cm
        JOIN (SELECT * FROM VIS_CALC_SEMESTER WHERE {lower_bound}<=NODE_ID AND NODE_ID<={upper_bound}) cs ON cm.NODE_ID=cs.NODE_ID
        WHERE {lower_bound}<=cm.NODE_ID AND cm.NODE_ID<={upper_bound};
        """

    print("CALC TASK_1: dropping starts....")
    cursor.execute(calc_task_1_drop)
    print("CALC TASK_1: dropping ends....")

    print("CALC TASK_1: creating starts....")
    cursor.execute(calc_task_1_create)
    print("CALC TASK_1: creating ends....")

    print("CALC TASK_1: inserting starts....")
    node_id = get_last_node_id(db=None, cursor=cursor)
    part = 5000
    iteration = ceil(node_id / part)
    for i in range(iteration):
        print("iteration: {} \tdone: {} %".format(i, (i / iteration) * 100))
        lower_bound = i * 5000
        upper_bound = (i + 1) * 5000
        sql = calc_task_1_insert.format(lower_bound=lower_bound, upper_bound=upper_bound)
        cursor.execute(sql)
        db.commit()

    print("CALC TASK_1: inserting ends....")


def create_task_2(db, cursor):
    calc_task_2_drop = """
    DROP TABLE VIS_CALC_TASK_2;
    """
    calc_task_2_create = """
    CREATE TABLE `VIS_CALC_TASK_2` (
      `NODE_ID` int(11) DEFAULT NULL,
      `NODE_TITLE` varchar(256) DEFAULT NULL,
      `CURRICULUM_CODE` varchar(17) DEFAULT NULL,
      `SEMESTER_TYPE_ID` int(11) DEFAULT NULL,
      `MEDIAN_SEMESTER` int(11) DEFAULT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """

    calc_task_2_insert = """
    INSERT INTO `VIS_CALC_TASK_2`
    SELECT mn.NODE_ID, mn.NODE_TITLE, mn.CURRICULUM_CODE, mn.SEMESTER_TYPE_ID, nsm.MEDIAN_SEMESTER
    FROM VIS_NODE_SEM_MEDIAN nsm
    JOIN (SELECT NODE_ID, NODE_TITLE, CURRICULUM_CODE, SEMESTER_TYPE_ID  FROM  VIS_CALC_MODULE WHERE {lower_bound}<=NODE_ID AND NODE_ID<={upper_bound}) mn ON mn.NODE_ID = nsm.NODE_ID
    WHERE {lower_bound}<=mn.NODE_ID AND mn.NODE_ID<={upper_bound}
    GROUP BY mn.NODE_TITLE;
     """

    print("CALC TASK_2: dropping starts....")
    cursor.execute(calc_task_2_drop)
    print("CALC TASK_2: dropping ends....")

    print("CALC TASK_2: creating starts....")
    cursor.execute(calc_task_2_create)
    print("CALC TASK_2: creating ends....")

    print("CALC TASK_2: inserting starts....")
    node_id = get_last_node_id(db=None, cursor=cursor)
    part = 5000
    iteration = ceil(node_id / part)
    for i in range(iteration):
        print("iteration: {} \tdone: {} %".format(i, (i / iteration) * 100))
        lower_bound = i * part
        upper_bound = (i + 1) * part
        sql = calc_task_2_insert.format(lower_bound=lower_bound, upper_bound=upper_bound)
        cursor.execute(sql)
        db.commit()

    print("CALC TASK_2: inserting ends....")


# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             port=8889,
                             user='root',
                             password='root',
                             db='ATHENS15',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        start = datetime.datetime.now()
        print(start)

        # create_calc_module(db=connection, cursor=cursor)
        # create_calc_semester(db=connection, cursor=cursor)
        # create_task_1(db=connection, cursor=cursor)

        create_task_2(db=connection, cursor=cursor)

        

        end = datetime.datetime.now()
        print(end)
        print("time: {}".format(end - start))

except Exception as e:
    print(e)

finally:
    connection.close()
