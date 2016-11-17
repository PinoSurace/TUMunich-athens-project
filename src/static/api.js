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
            startAnimation();
            sleep(1000000);
            $.ajax({
                "method": "GET",
                "url": "/api/curriculum",
                "success": function (data) {
                    stopAnimation();
                    resolve(data);
                },
                "error": function (error) {
                    stopAnimation();
                    reject(error);
                }
            })

        });
    },

    startAnimation: function() {
        console.log("Start animation");
        document.getElementById("loading").style.visibility = "visible"; 
    },

    stopAnimation: function() {
        console.log("Stop animation");
        document.getElementById("loading").style.visibility = "hidden";     
    }

}

