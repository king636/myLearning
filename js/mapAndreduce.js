'use strict'
/**
 * map and reduce 都是高阶函数
 */
//map把函数作用在Array的每一个元素并把结果生成一个新的Array．
//调用map函数的array本身没有变
var fn = function(x){
    return x * x;
}

var array = [1,2,3,4,5];
console.log(array);//[ 1, 2, 3, 4, 5 ]
console.log(array.map(fn));//[ 1, 4, 9, 16, 25 ]

console.log(array.map(String));//[ '1', '2', '3', '4', '5' ]
console.log(String(10));//String是内置函数？

//reduce也是把函数作用在Array的每一个元素上，但是这个函数必须接收两个参数，表示把结果继续和Array的下一个元素做累积计算
function sum(x,y){
    return x + y;
}

console.log(array.reduce(sum));//15

//把Array转换成Number
function toNumber(x,y){
    return x * 10 + y;
}
console.log(array.reduce(toNumber));//12345

//练习1：错误输出分析原因：
//参考map()和parseInt()的函数说明：
/**
 * parseInt():http://www.w3school.com.cn/jsref/jsref_parseInt.asp
 * parseInt(string, radix)：radix代表基数(2~36)，默认为０，0或者10都代表基数10.　0x或者0X则代表基数为16
 */
console.log(parseInt('11'));//11
console.log(parseInt('11',2));//3
console.log(parseInt('1f',16));//31
/**
 * map():https://www.cnblogs.com/marfzy/archive/2013/04/06/3003147.html
 * map(callbackfn[, thisArg]) :map中的函数callbackfn参数有要求
 * callbackfn(element, index, self) 分别是元素　索引　数组本身
 * 所以这里传入parseInt导致第二个参数冲突，使用了０，导致结果第一个刚好是索引0转换正确，后面的为NaN
 */
console.log(['4','2','3'].map(parseInt));//[ 4, NaN, NaN ]
//正确的写法，要么parseInt重新定义，要么使用Number()方法
//1. 重新定义parseInt
var oldParseInt = parseInt;
parseInt = function(){
    return oldParseInt(arguments[0]);
}
console.log(['4','2','3'].map(parseInt));//[4,2,3]

//2.使用Number()方法
/**
 * Number方法说明：http://www.w3school.com.cn/jsref/jsref_number.asp
 * Number(object)，只有一个参数，所以不会冲突
 */
console.log(['4','2','3'].map(Number));//[ 4, 2, 3 ]

//所以使用map尽量自定义函数，除非确切知道内置函数的参数

//练习２：把不规范的英文单词变为首字母大写，其他小写的规范单词
//这里参数验证等省略
array = ['niCk','CaTHY','abBiE'];
var correct = function(x){
    let y = x.toLowerCase();
    return y.slice(0,1).toUpperCase() + y.slice(1);
}
console.log(array.map(correct));//[ 'Nick', 'Cathy', 'Abbie' ]
console.log(array);//[ 'niCk', 'CaTHY', 'abBiE' ]，array本身并没有改变

//练习３：把一个字符串变为Array,再转换成Number
var str = '13254';
array = str.split('');
console.log(array);//[ '1', '3', '2', '5', '4' ]
console.log(array.reduce(function(x,y){ return x + y;}));//13254