function Parameters() {
    var item = "";
    $(function () {
        var test = $.ajax({
            type: "GET",
            url: "/TQ.json",//利用ajax请求后台的并返回值
            dataType: "json",
            async: false
        });
        var data = [];
        data = test.responseJSON.results;
        for (var i = 0; i < data.length; i++) {
            item += "<tr><td>" + data[i].cityName + "</td><td>" + data[i].tmp_min + "℃~" + data[i].tmp_max + "℃</td><td>" + data[i].cond_txt_d +
                "</td><td>" + data[i].cond_txt_n + "</td><td>" ;
        }
        $("#tianqi").html(item);

    })
}
Parameters();