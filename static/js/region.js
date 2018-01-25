function getUrlParam(key) {
    // 获取参数
    var url = window.location.search;
    // 正则筛选地址栏
    var reg = new RegExp("(^|&)" + key + "=([^&]*)(&|$)");
    // 匹配目标参数
    var result = url.substr(1).match(reg);
    //返回参数值
    return result ? decodeURIComponent(result[2]) : null;
}

var city = getUrlParam("cityName");
var year = getUrlParam("year");
var a =  document.getElementById("cityName");
a.value = city;
var b =  document.getElementById("year");
b.value = year;
function ParametersFunc() {
    var item = "";
    $(function () {
        var test = $.ajax({
            type: "GET",
            url: "/RegionData.json",//利用ajax请求后台的并返回值
            dataType: "json",
            data: {cityName: city,year: year},
            async: false
        });
        var data = [];
        data = test.responseJSON.results;
        for (var i = 0; i < data.length; i++) {
            item += "<tr><td>" + data[i].cityName + "</td><td>" + data[i].year + "</td><td>" + data[i].month + "</td><td>" + data[i].rainfall +
                "</td><td>" + data[i].level + "</td><td>" ;
        }
        $("#tianqi").html(item);



    })
}
ParametersFunc();
//折线图
$(function () {
            var test = $.ajax({
                type: "GET",
                url: "/RegionData.json",//利用ajax请求后台的并返回值
                dataType: "json",
                data: {cityName: city,year: year},
                async: false
            });
            var data1 = [];
            var data2 = [];
            data1 = test.responseJSON.results;
            for(var i = 0; i < data1.length; i++) {
                data2[i] = data1[i].rainfall;
            }
            var lineChartData = {
                labels : ["January","February","March","April","May","June","July","August","September","October","November","December"],
                datasets : [
                    {
                        fillColor : "rgba(151,187,205,0.5)",
                        strokeColor : "rgba(151,187,205,1)",
                        pointColor : "rgba(151,187,205,1)",
                        pointStrokeColor : "#fff",
                        data : [data2[0],data2[1],data2[2],data2[3],data2[4],data2[5],data2[6],data2[7],data2[8],data2[9],data2[10],data2[11]]
                    }
                ]

            }

            var myLine = new Chart(document.getElementById("canvas").getContext("2d")).Line(lineChartData);

})