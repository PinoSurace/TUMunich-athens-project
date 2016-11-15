$(document).ready(function () {

    function displayTask1(data) {
        // code from Pino and Wang
        console.log(data);
    }

    function task1(moduleName) {
        new Promise(function (resolve, reject) {

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

        }).then(function (data) {
            displayTask1(data);
        })
    }

    task1("math");


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

