//正则表达式用法
'use strict'

//三种写法，等价
//第一种: /正则表达式/
//这里正则表达式代表带区号的电话号码，解析：^匹配开头，$匹配结束，\d{3}匹配３个数字，\d{3,8}匹配３－８个数字
var reg1 = /^\d{3}-\d{3,8}$/;//这里-或者\-都可以
//第二种：new RegExp('正则表达式字符串')创建对象,注意字符串转义
var reg2 = new RegExp('^\\d{3}\\-\\d{3,8}$');
//第三种: new RegExp(正则表达式),括号内与第一种写法一样
var reg21 = new RegExp(/^\d{3}-\d{3,8}$/);

//判断是否匹配,使用test()方法 -- python用re模块来匹配
console.log(reg1.test('021-34556'));//true
console.log(reg2.test('021-34556'));//true
console.log(reg21.test('021-34556'));//true

console.log(reg1.test('0212-34556'));//false
console.log(reg2.test('021 34556'));//false
console.log(reg21.test('021 34556'));//false

/**
 * 含义说明(与python一样)：
 * \d 匹配数字
 * \w 匹配字母或者数字
 * \s 匹配空格
 * . 匹配任意字符
 * * 匹配任意个字符(包括０个)
 * ? 匹配０个或１个字符
 * + 匹配至少一个字符
 * {n} 匹配n个字符
 * {n,m} 匹配n-m个字符
 * 举例:\d{3}\s+\d{3,8},表示用任意个空格隔开的带区号电话号码
 */

 /**
  * 精确匹配，使用[]表示范围
  * [0-9a-zA-Z\_] 匹配一个数字，字母或者下划线
  * [0-9a-zA-Z\_]+ 匹配至少由一个数字，字母或者下划线组成的字符串
  * [a-zA-Z\_\$][0-9a-zA-Z\_\$]* 匹配任意个由字母，下划线或$开头，后接数字，字母或者下划线组成的字符串，即变量名
　＊ [a-zA-Z\_\$][0-9a-zA-Z\_\$]{0, 19} 限制变量名长度1-20个字符.
  * A|B　匹配A或B
  * ^ 表示行的开头
  * $ 表示行的结束
  */

//接上面的例子，如何匹配 '010 -   12345'这样的电话号码？[\s]* 来匹配任意个空格
var reg3 = /^\d{3}[\s]*\-[\s]*\d{3,8}$/; 
console.log(reg3.test('010 -    12345'));//true
console.log(reg3.test('010-12345'));//true
console.log(reg3.test('010　　 -12345'));//true

//切分字符串，可以识别连续的空格;等
console.log('a b    c'.split(/\s+/));//[ 'a', 'b', 'c' ]
//空格或者逗号切分
console.log('a,b, c  d,,e'.split(/[\s\,]+/));//[ 'a', 'b', 'c', 'd', 'e' ]

//使用分组提取子串
var reg4 = /(\d{2})-(\d{3,5})$/;
//这里和python不同，python匹配将失败．js的匹配应该更强大些，语义上应该是要匹配的，010当然包括\d{2}
var arr = reg4.exec('010-12345');//匹配成功返回arr,元素如下：匹配到的字符串以及子串等
console.log(arr);//[ '10-12345', '10', '12345', index: 1, input: '010-12345' ]
arr = reg4.exec('010 12345');//不匹配则返回null
console.log(arr);//null

//使用分组识别合法时间，不合法返回null
var re = /^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$/;
arr = re.exec('19:05:30');
console.log(arr);//[ '19:05:30', '19', '05', '30', index: 0, input: '19:05:30' ]

//贪婪匹配与非贪婪匹配
//默认为贪婪匹配，如下匹配不到０
var reg5 = /^(\d+)(0*)$/;
arr = reg5.exec('102300');
console.log(arr);//[ '102300', '102300', '', index: 0, input: '102300' ]
//用？改为非贪婪匹配(尽可能少的匹配)，可以匹配出后面的０
var reg6 = /^(\d+?)(0*)$/;
arr = reg6.exec('102300');
console.log(arr);//[ '102300', '1023', '00', index: 0, input: '102300' ]

//全局匹配g，类似搜索，多次执行exec，每次的索引值后移
//全局匹配时不要使用/^...$/，否则只执行一次
var s = 'JavaScript,VBScript,JScript and ECMAScript';
var reg7 = /[a-zA-Z]+Script/g;
reg7 = new RegExp('[a-zA-Z]+Script','g');//reg7的两种写法
console.log(reg7.lastIndex);//0
console.log(reg7.exec(s));//[ 'JavaScript',index: 0,input: 'JavaScript,VBScript,JScript and ECMAScript' ]
console.log(reg7.lastIndex);//10 (0+10)
console.log(reg7.exec(s));//[ 'VBScript',index: 11,input: 'JavaScript,VBScript,JScript and ECMAScript' ]
console.log(reg7.lastIndex);//19 (11+8)
console.log(reg7.exec(s));//[ 'JScript',index: 20,input: 'JavaScript,VBScript,JScript and ECMAScript' ]
console.log(reg7.lastIndex);//27 (20+7)
console.log(reg7.exec(s));//[ 'ECMAScript',index: 32,input: 'JavaScript,VBScript,JScript and ECMAScript' ]
console.log(reg7.lastIndex);//42 (32+10)
console.log(reg7.exec(s));//null
console.log(reg7.lastIndex);//0

//结合sprintf.js例子，分析复杂的全局匹配
var exp = new RegExp(/(%([%]|(\-)?(\+|\x20)?(0)?(\d+)?(\.(\d)?)?([bcdfosxX])))/g);
var match = exp.exec('%f');
console.log(match);
//匹配的结果看分组的情况:
// 1.匹配到%f
// 2.第一组:(%...),匹配到%f
// 3.第二组:([%]|...),匹配到f
// 4.第三组:(\-)?,匹配到undefined
// 5.第四组:(\+|\x20)?,匹配到undefined
// 6.第五组:(0)?,匹配到undefined
// 7.第六组:(\d+)?,匹配到undefined
// 8.第七组:(\.(\d)?)?,匹配到undefined
// 9.第八组:(\d)?,匹配到undefined
// 10.第九组:([bcdfosxX]),匹配到f
// 所以，结果如下：
// [ '%f',
// '%f',
// 'f',
// undefined,
// undefined,
// undefined,
// undefined,
// undefined,
// undefined,
// 'f',
// index: 0,
// input: '%f' ]

//注意：直接打印match,如上所示，调用tostring()打印不一样：
//%f,%f,f,,,,,,,f
console.log(match.toString());
//当打印的时候加上别的字符串，自动转成match.toString()打印：
//match: %f,%f,f,,,,,,,f
console.log('match: ' + match.toString());

