var parsePass = function(t) {
        var e = {
			hostname: "i.snssdk.com",
			pathname: "/video/urls/v/1/toutiao/mp4/v022f4090000bj3sfokuatl8f7vim9dg",
        };
        var n = function() {
            for (var t = 0, e = new Array(256), n = 0; 256 !== n; ++n)
                t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = n) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1,
                e[n] = t;
            return "undefined" != typeof Int32Array ? new Int32Array(e) : e
        }()
          , r = e.pathname + "?r=" + Math.random().toString(10).substring(2);
        "/" !== r[0] && (r = "/" + r);
        var i = function(t) {
            for (var e, r, i = -1, o = 0, a = t.length; o < a; )
                (e = t.charCodeAt(o++)) < 128 ? i = i >>> 8 ^ n[255 & (i ^ e)] : e < 2048 ? i = (i = i >>> 8 ^ n[255 & (i ^ (192 | e >> 6 & 31))]) >>> 8 ^ n[255 & (i ^ (128 | 63 & e))] : e >= 55296 && e < 57344 ? (e = 64 + (1023 & e),
                r = 1023 & t.charCodeAt(o++),
                i = (i = (i = (i = i >>> 8 ^ n[255 & (i ^ (240 | e >> 8 & 7))]) >>> 8 ^ n[255 & (i ^ (128 | e >> 2 & 63))]) >>> 8 ^ n[255 & (i ^ (128 | r >> 6 & 15 | (3 & e) << 4))]) >>> 8 ^ n[255 & (i ^ (128 | 63 & r))]) : i = (i = (i = i >>> 8 ^ n[255 & (i ^ (224 | e >> 12 & 15))]) >>> 8 ^ n[255 & (i ^ (128 | e >> 6 & 63))]) >>> 8 ^ n[255 & (i ^ (128 | 63 & e))];
            return -1 ^ i
        }(r) >>> 0;
        console.log((["http:", e.hostname]).join("//") + r + "&s=" + i + "&aid=1364")
        return (["http:", e.hostname]).join("//") + r + "&s=" + i + "&aid=1364"

    }
    url = parsePass("//i.snssdk.com/video/urls/v/1/toutiao/mp4/v022f4090000bj3sfokuatl8f7vim9dg");
parsePass("v022f4090000bj3sfokuatl8f7vim9dg")