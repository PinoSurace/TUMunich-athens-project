function displayTask1(data) {
    // code from Pino and Wang
    console.log(data);
}

function task1(moduleName) {
    var request = new Promise(function (resolve, reject) {

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

    }).then(function(data) {
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
