/**
 * Created by oldboy on 2018/5/31.
 */
// 编写代码，将当前日期按“2017-12-27 11:11 星期三”格式输出。
const WEEKMAP = {
    0: "星期日",
    1: "星期一",
    2: "星期二",
    3: "星期三",
    4: "星期四",
    5: "星期五",
    6: "星期六",
};


function showTime() {
    var d1 = new Date();
    var year = d1.getFullYear();
    var month = d1.getMonth() + 1;
    var day = d1.getDate();
    var hour = d1.getHours();
    var minute = d1.getMinutes() < 10 ? "0"+d1.getMinutes() :d1.getMinutes();

    var week = WEEKMAP[d1.getDay()];  // 0~6的星期

    var dateStr = `
        ${year}-${month}-${day} ${hour}:${minute} ${week}
    `;
    console.log(dateStr)
}

showTime();