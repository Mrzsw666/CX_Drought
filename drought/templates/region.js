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

var  city = getUrlParam("cityName");
var obj = "";
function ParametersFunc() {
    $.ajax({
        type: "GET",
        url: "../views.py",//利用ajax请求后台的并返回值
        dataType: "json",
        data:{ cityName:'city' },
        async:true,
        success: function (json) {//result为后台返回的值,是json字符串的形式
            alert(json);//解析json字符串为json对象形式

        },
        error: function (error) {
            alert( "1"+error);
        }
    });
}
ParametersFunc();
