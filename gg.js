'use strict';
var gg = {m: function(g) 
{
var o = 1;
switch (g){
case 1117:
case 1445:
case 3211:
case 107:
case 774:
case 1659:
case 2131:
case 289:
case 968:
case 888:
case 1210:
case 83:
case 1199:
o = 0; break;
}
return o;
},
s: function(h) { var m = /(..)(.)$/.exec(h); return parseInt(m[2]+m[1], 16).toString(10); },
b: '1678262402/'
};

console.log(gg.m(1117)); // 0
console.log(gg.m(1234)); // 1