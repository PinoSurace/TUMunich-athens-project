$(document).ready(function () {

    // task1("17 761");
    // api.loadTask2("17 761");

    function loadSelect() {
        api.loadCurriculum().then(function (data) {

            data.result["bachelors"].forEach(function (curriculum) {
                $("#task-1-curriculum #label-bachelors").append(
                    "<option value=\"" + curriculum.curriculumCode + "\">" + curriculum.curriculumName + "</option>"
                );
            });

            data.result["masters"].forEach(function (curriculum) {
                $("#task-1-curriculum #label-masters").append(
                    "<option value=\"" + curriculum.curriculumCode + "\">" + curriculum.curriculumName + "</option>"
                );
            })

            var task1select = $("#task-1-curriculum");
            task1select.select2();
            task1select.on("change", function (e) {
                var obj = task1select.select2("data");
                console.log("change val=" + obj[0].id);  // 0 or 1 on change
                var curriculumCode = obj[0].id
                task1(curriculumCode)

            });

        });
    }


    function task1(curriculumCode) {

        function showDiagram(module) {

            var semesters = getValuesOfObject(module.numberPerSemester)
            var computedSemesters = semesters.map(function (semester, i) {
                return semesters.slice(i).reduce(function (a, b) {
                    return a + b;
                }, 0);
            });
            var windowWidth = window.innerWidth * 0.7;
            var chart = d3.select("#d3-content-" + module.moduleId).append("svg") // creating the svg object inside the container div
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
                console.log(module)
                var string = "<tr>" +
                    "<td>" +
                    module.moduleName +
                    "</td>" +
                    "<td>" +
                    "<div id=\"d3-content-" + module.moduleId + "\"></div>" +
                    "</td>" +
                    "</tr>";

                $("#task-1-table tbody").append(string);

            })

        }

        api.loadTask1(curriculumCode).then(function (data) {

            prepareDivsForDiagrams(data.result);
            data.result.forEach(function (module) {
                showDiagram(module);
            })

        })
    }


    loadSelect();
    task1();


});

