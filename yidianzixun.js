var k = function() {

    "use strict";
    var n = "/home/q/news_list_for_channel?channel_id=m1532050&cstart=0&cend=10&infinite=true&refresh=1&__from__=pc&multi=5", 
    e = "m1532050", 
    i = 0,
    t = 10
    var t;
    var m;
    var a;
    t = function(n, e, i) {
        m = function(n, e, i) {
    
            for (var o = "sptoken", a = "", c = 1; c < arguments.length; c++)
                o += arguments[c];
            for (var c = 0; c < o.length; c++) {
                
                var r = 10 ^ o.charCodeAt(c);
                a += String.fromCharCode(r)
                console.log(a)
            }
        }()
    }()
}

console.log(k())