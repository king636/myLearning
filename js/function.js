//函数
'use strict'

//内置函数，Math.abs() python的是abs()
console.log(Math.abs(-20));//20
//python的abs()参数超过１个会报错，js不会
console.log(Math.abs(-20,1,2));//20
//参数类型不对，返回NaN
console.log(Math.abs('a'));//NaN
console.log(Math.max(1,8,3,5))//8

function add(x){
    return x + 1;
}

function add1(x){
    x + 1;
}

var add2 = function(x){
    return x + 1;
};

console.log(add(1));//2
console.log(add())//NaN --因为参数收到的是undefined,所以计算结果为NaN
console.log(add(1,2,3,4))//2

console.log(add1(1));//undefined
console.log(add2(1));//2

//对参数进行检查
var add3 = function(x){
    if(typeof x !== 'number')
        throw('not a number');

    return x + 1;
}
// console.log(add3());

//python中判断x的类型: isinstance(x,(int,float))
var my_abs_extend = function(x){
    if(typeof x !== 'number')
        throw('bad operand type');//python抛异常：raise TypeError('bad operand type')

    if(x >= 0)
        return x;
    else
        return -x;
}

//console.log('my_abs_extend ' + my_abs_extend('a'));//异常：bad operand type
console.log('my_abs_extend ' + my_abs_extend(-20));//my_abs_extend 20
console.log('my_abs_extend ' + my_abs_extend(3.14));//my_abs_extend 3.14

//arguments
//arguments类似Array,但不是Array.怎么理解？
var fun = function(x){
    for(var i = 0; i < arguments.length; i++){
        console.log('arg' + i + '=' + arguments[i]);
    }
}

fun(10,20,30);//arg0=10 arg1=20 arg2=30

//rest参数(ES6).返回Array
var fun2 = function(a,b,...rest){
    console.log(rest);
}

fun2(1,2,3,4,5);//[3,4,5]
fun2();//[]

//作用域
//全局的window对象(只在浏览器使用)
var course = 'javascript';
console.log(course);//javascript
// console.log(window.course);

//名字空间(比如jQuery就是使用$来引用属性和方法)
var $ = {};
$.fun2 = fun2;
$.fun2(1,2,7,7,7);//[7,7,7]

//块级作用域：let(ES6)
function foo() {
    var sum = 0;
    // for(var i = 0; i < 100; i++)//var i,在函数内都可以访问
    for(let i = 0; i < 100; i++) {//let只在语句块生效
        sum += i;
    }
    // SyntaxError:
    i += 1;
}

//常量const(ES6)
const PI = 3.14;
// PI = 3;//TypeError: Assignment to constant variable.

//解构赋值(ES6),把数组的元素分别赋值给几个变量
let [x,y,z] = ['a',2,'c'];//这里用let或者var应该是一样的
console.log('x:' + x + ',y:' + y + ',z:' + z);//x:a,y:2,z:c
let [a,[b,c]] = [1,[2,3]];//结构要保持一致
console.log('a:' + a + ',b:' + b + ',c:' + c);//a:1,b:2,c:3
//可以忽略某些元素
let [,,x1] = [1,2,3];
console.log('x1:' + x1);//x1:3
//变量定义和解构赋值分开
let m,n;
[m,n] = ['a',2];
console.log('m: ' + m + ', n: ' + n);//m: a, n: 2

//从对象中解构，变量名必须要和对象的属性名保持一致;如果不一致，要进行转换;还可以设置默认值
var person = {
    name:'nick',
    age:30,
    address:{
        city:'Xiamen',
        country:'China'
    }
}
var {name,address:{city,country:motherland},gender,single = true} = person;
console.log('name: ' + name + ', address city: ' + city);//name: nick, address city: Xiamen
//不存在为undefined
console.log('gender: ' + gender);//gender: undefined
//转换的变量
console.log('country: ' + motherland);//country: China
//为定义的属性，变量为默认值
console.log('single: ' + single);//single: true
//变量定义和结构赋值分开需要注意：js把{}当成语句块执行，不能直接赋值，要用()括起来
var n1,a1;
({n1,a1} = {name:'小明',n1:123,a1:'abc'});
console.log('n1: ' + n1 + ', a1: ' + a1);//n1: 123, a1: abc

//使用解构赋值可以减少代码量
//不需要中间变量，实现交换变量的值
x = 3;
y = 5;
[x,y] = [y,x];
console.log('x: ' + x + ', y: ' + y);//x: 5, y: 3
//函数传入对象时，可以将对象属性与变量绑定
function buildDate({year,month,day,hour = 0,minute = 0,second = 0}){
    return new Date(year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second);
}

console.log(buildDate({year:2017, month:12, day:7}));//2017-12-06T16:00:00.000Z

//高阶函数