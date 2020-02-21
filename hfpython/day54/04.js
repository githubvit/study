/**
 * Created by oldboy on 2018/5/31.
 */


function f1() {
    alert(123);
}

function clear() {
    var t = setInterval(f1, 3000);
    function inner() {
        clearInterval(t);
    }
    setTimeout(inner, 9000)
}

clear();