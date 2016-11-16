function getValuesOfObject(obj) {
  return Object.keys(obj).map(function (key) {
    return obj[key];
  });
}

$(document).ready(function () {

    function displayTask1(data) {
        // code from Pino and Wang
        console.log(data);
    }

    function task1(moduleName) {
        api.loadTask1(moduleName).then(function (data) {
            displayTask1(data);
        })
    }

    task1("math");
    api.loadCurrciulum().then(function(data) {console.log(data)});


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

