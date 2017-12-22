/**
 * 安装node后，命令行输入node进入交互模式
 * 退出输入.exit,或者两次ctrl+c
 * 这里都是在命令行不进入node交互模式，用命令node xxx.js来运行js文件
 * python也类似
 */
//基本用法
'use strict'

//数据类型与调试打印
//Number型
var a = 123;
console.log(a);//123
console.log(a + "");//123
console.log(a.toString);//[Function: toString]
console.log(`${a}`);//123
console.log(a / 0);//Infinity，表示无限大
console.log(10 / 3);//3.3333333333333335(与Python相同)
//Math.floor下退，Math.ceil上进，Math.round四舍五入
console.log(Math.floor(10 / 3));//小数转整数(Python中用地板除//)
console.log(10 % 3);//1(与Python相同)
console.log(10.5 / 3);//3.5
console.log(10.5 % 3);//1.5(与Python相同)
console.log(0 / 0);//NaN:not a number,表示无法计算
a = 0xff;//255
console.log(a);

//dec = 255, oct = 255, hex = 255
console.log('dec = %d, oct = %d, hex = %d',a,a,a)
//但是十六进制和八进制无法使用(python可以：print('dec = %d,oct = %o,hex = %x'%(a,a,a)))
//以下输出：dec = 255, oct = %o, hex = %x 255 255
console.log('dec = %d, oct = %o, hex = %x',a,a,a)
a = 1.23;
//无法正确输出：float = %f 1.23
console.log('float = %f',a);
//问题：js中如何输出十六进制与八进制，以及%f等？
//js中格式化输出，除了%d, %s,其他需要单独转换
a = "test abc";
console.log('output: %s',a);
//转换思想：实现ｃ中sprintf类似功能．
//1.jQuery插件已经实现类似功能
//待完成：寻找jQuery插件来实现，或者自己来开发jQuery插件并导入实现？？？
//注意：js语言本身没有导入外部脚本文件的功能，只能通知宿主程序来处理．浏览器就是脚本的宿主程序．所以导入jQuery文件时
//需要在html文件中处理
//2.实现类似sprintf函数，具体见spintf.js
//sprintf练习掌握正则表达式用法，sprintfWrapper为对象，init函数的使用


//比较
console.log(10 / 3 === 3.3);//false
console.log(10 / 3 == 3.3);//false
console.log(10 / 3 < 3.3333334);//true
console.log(a == '123');//true，注意a被转型成字符串类型
console.log(a === '123');//false
console.log(a == 123);//true
console.log(a === 123);//true
console.log(NaN === NaN);//false
console.log(isNaN(NaN));//true
console.log(isNaN(0 / 0));//true

//布尔值 python中：True False
a = true;
console.log(a);//true
console.log(false == 0);//true:被转型为0,所以不要使用==
console.log(false === 0);//false
console.log(1/3 === (1 - 2/3));//false
console.log(Math.abs(1/3 - (1 - 2/3)) < 0.000001);//true 浮点数比较时，使用差的绝对值，只能是很小范围
//布尔值运算　python中为:and or not
console.log(true && false);//false
console.log(true || false);//true
console.log(!true);//false

//字符串
a = '123';
console.log(a);//123
//与python不同，以下无法输出,python: print('%s'%a)
console.log('%s',a);
console.log(`${a}`);//123
console.log('多行的时候\n可以换行输出');
console.log(`多行的时候
可以换行输出`);//(ES6)
console.log("I'm ok");//I'm ok
console.log('I\'m \"ok\"');//I'm "ok"
console.log("I'm 'ok'");//I'm 'ok'
console.log('\x41');//A ASCII字符的十六进制表示\x##
console.log('\u4e2d\u6587');//中文　unicode字符\u####
a = 'nick';
console.log('你好,' + a);//你好,nick
console.log(`你好，${a}`);//你好，nick　　模板字符串(ES6)
console.log(a[0]);//n　与数组Array类似
a = "中文"
console.log(a[0]);//中
//与数组不同的是，无法给字符串的索引赋值，字符串的值是固定的
var s = 'Text';
// s[0] = 'Y';//TypeError: Cannot assign to read only property '0' of string 'Text'
console.log(s);//
console.log(s.toUpperCase());//TEXT
console.log(s.toLowerCase());//text
console.log(a.toUpperCase());//中文
console.log(a.toLowerCase());//中文
console.log(a.indexOf('文'));//1
console.log(s.substring(1,3));//ex
//string也可以直接用array的slice()方法来获取子串
console.log('string slice: ' + s.slice(1,3));//string slice: ex
//string调用array的splice()方法则不行
// console.log('string splice: ' + s.splice(0,1,'a','b'));
console.log(s.substring(2));//xt
console.log(s.substring());//Text,不给参数则为整个字符串
a = s;
console.log(a);//Text

a = 'abc';
var b = a;
a = 'def';
console.log('a =', a);//a = def 
console.log('b =', b);//b = abc 理解引用的指向，python相同

//null和undefined
//null表示空值，undefined仅在判断函数参数是否传递的情况下有用
//python中的空值：None
a = null;
console.log(a);//null
//b = 'abc';//ReferenceError: b is not defined
// console.log(b);//Error: b is not defined

//数组
a = [1,"2","hello",4,'5'];
console.log(a);//[ 1, '2', 'hello', 4, '5' ]
a = new Array("a",2,'3','hello',5);//[ 'a', 2, '3', 'hello', 5 ]
console.log(a);
console.log(a[3]);//hello

//对象
a = {
    // name: nick,//nick is not defined
    name: 'nick',
    age:30,
    money:Infinity,
    disease:null
}
console.log(a);//{ name: 'nick', age: 30, money: Infinity, disease: null }
console.log(a.name);//nick

//常量
const PI = 3.14;
// PI = 2;//TypeError: Assignment to constant variable.

