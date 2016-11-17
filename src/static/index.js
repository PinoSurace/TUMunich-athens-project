function getValuesOfObject(obj) {
    return Object.keys(obj).map(function (key) {
        return obj[key];
    });
}

$(document).ready(function () {

    task1("17 761");
    api.loadTask2("17 761");

    function displayTask1(data) {

        var task1select = $("#task-1-curriculum");
        task1select.select2();
        task1select.on("change", function (e) {
            var obj = task1select.select2("data");
            console.log("change val=" + obj[0].id);  // 0 or 1 on change
        });


        // api.loadCurrciulum().then(function(data) {console.log(data)});


        var data = [
            {
                "id": 1,
                "moduleName": "Math",
                "type": "bachelor",
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
                "id": 2,
                "moduleName": "Advanced Biology",
                "type": "master",
                "numberPerSemester": {
                    "semester_1": 15,
                    "semester_2": 8,
                    "semester_3": 7,
                    "semester_4": 0
                }
            }
        ]

        function showDiagram(module) {

            var semesters = getValuesOfObject(module.numberPerSemester)
            var computedSemesters = semesters.map(function (semester, i) {
                return semesters.slice(i).reduce(function (a, b) {
                    return a + b;
                }, 0);
            });
            var windowWidth = window.innerWidth * 0.7;
            var chart = d3.select("#d3-content-" + module.id).append("svg") // creating the svg object inside the container div
                .attr("class", "chart")
                .attr("width", windowWidth) // bar has a fixed width
                .attr("height", 20);

            var x = d3.scaleLinear() // takes the fixed width and creates the percentage from the data values
                .domain([0, d3.max(computedSemesters)])
                .range([0, windowWidth]);

            chart.selectAll("rect") // this is what actually creates the bars
                .data(computedSemesters)
                .enter().append("rect")
                .attr("width", x)
                .attr("height", 20)
                .attr("rx", 10) // rounded corners
                .attr("ry", 10);

            chart.selectAll("text") // adding the text labels to the bar
                .data(computedSemesters)
                .enter().append("text")
                .attr("x", x)
                .attr("y", 10) // y position of the text inside bar
                .attr("dx", -10) // padding-right
                .attr("dy", ".35em") // vertical-align: middle
                .attr("text-anchor", "end") // text-align: right
                .text(String);
        }


        function prepareDivsForDiagrams(modules) {

            modules.forEach(function (module) {
                var string = "<tr>" +
                    "<td>" +
                    module.moduleName +
                    "</td>" +
                    "<td>" +
                    "<div id=\"d3-content-" + module.id + "\"></div>" +
                    "</td>" +
                    "</tr>";

                $("#task-1-table tbody").append(string);

            })

        }


        prepareDivsForDiagrams(data)
        data.forEach(function (module) {
            showDiagram(module);
        })

    }

    function task1(moduleName) {
        api.loadTask1(moduleName).then(function (data) {
            displayTask1(data);
        })
    }

    task1("math");


    api.loadCurriculum().then(function (data) {

        data.result["bachelors"].forEach(function (module) {
            $("#task-1-curriculum #label-bachelors").append(
                "<option value=\"" + module.curriculum_nr + "\">" + module.name + "</option>"
            );
        });

        data.result["masters"].forEach(function (module) {
            $("#task-1-curriculum #label-masters").append(
                "<option value=\"" + module.curriculum_nr + "\">" + module.name + "</option>"
            );
        })

    });

    var data = [
        {
            "title": "Math",
            "type": "Bachelor"
        },
        {
            "title": "Advanced Math",
            "type": "Master"
        }
    ];


    $('#task-1 #all').click(function (e) {
        console.log('all');
    })

    $('#task-1 #bachelors').click(function (e) {
        console.log('bachelors');
    })

    $('#task-1 #masters').click(function (e) {
        console.log('masters');
    })

});

