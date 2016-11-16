var api = {

    loadTask1: function (moduleName) {
        return new Promise(function (resolve, reject) {

            $.ajax({
                "method": "GET",
                "url": "/api/task1/" + moduleName,
                "success": function (data) {
                    resolve(data);
                },
                "error": function (error) {
                    reject(error);
                }
            })

        });
    },
    
    loadCurrciulum: function() {
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
    }

}

