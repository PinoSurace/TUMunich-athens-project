var api = {

    loadTask1: function (curriculumCode) {
        return new Promise(function (resolve, reject) {

            $.ajax({
                "method": "GET",
                "url": "/api/task1/" + curriculumCode,
                "success": function (data) {
                    resolve(data);
                },
                "error": function (error) {
                    reject(error);
                }
            })

        });
    },

    loadTask2: function (curriculumCode) {
        return new Promise(function (resolve, reject) {

            $.ajax({
                "method": "GET",
                "url": "/api/task2/" + curriculumCode,
                "success": function (data) {
                    resolve(data);
                },
                "error": function (error) {
                    reject(error);
                }
            })

        });
    },
    
    loadCurriculum: function() {
        return new Promise(function (resolve, reject) {

            $.ajax({
                "method": "GET",
                "url": "/api/curriculum",
                "success": function (data) {
                    resolve(data);
                },
                "error": function (error) {
                    reject(error);
                }
            })

        });
    },

    startAnimation: function() {
        document.getElementById("loading").style.visibility = "visible"; 
    },

    stopAnimation: function() {
        document.getElementById("loading").style.visibility = "hidden";     
    }

}

