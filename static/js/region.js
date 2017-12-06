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
function ParametersFunc() {
    var item = "";
    $(function () {
        var test = $.ajax({
            type: "GET",
            url: "/RegionData.json",//利用ajax请求后台的并返回值
            dataType: "json",
            data: {cityName: city},
            async: false
        });
        var data = [];
        data = test.responseJSON.results;
        for (var i = 0; i < data.length; i++) {
            item += "<tr><td>" + data[i].cityName + "</td><td>" + data[i].year + "</td><td>" + data[i].month + "</td><td>" + data[i].rainfall +
                "</td><td>" + data[i].level + "</td><td>" ;
        }
        $("#da").html(item);
    })
}
ParametersFunc();
