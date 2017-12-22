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
// 注意：python的dict解构时，只能解构到list或tuple里面去
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

//对象的方法：对象中绑定的函数
var nick = {
    name:'nick',
    birth:1990,
    age:function(){
        let year = new Date().getFullYear();
        return year - this.birth;
    }
}

console.log(nick.age);//[Function: age]
console.log(nick.age());//27

//js坑太多，注意age的方法里面this的用法，调用nick.age()时this指向当前对象nick,所以没有问题．
//修改下：
var getAge = nick.age;
//报错：TypeError: Cannot read property 'birth' of undefined．因为this指向了undefined
// console.log(getAge());

//使用apply改变this的指向,参数为空
console.log(getAge.apply(nick,[]));//27
//或者使用call,这里参数省略
console.log(getAge.call(nick));//27

//如果对age函数重构，也会有坑
// var bob = {
//     name:'bob',
//     birth:1990,
//     age:function(){
//         function getAgeFromBirth(){
//             let year = new Date().getFullYear();
//             return year - this.birth;
//         }
//         return getAgeFromBirth();
//     }
// }

//报错：TypeError: Cannot read property 'birth' of undefined
//age内部的函数this也指向了undefined
// console.log(bob.age());

//所以要进一步修改,先保存this的指向
var cathy = {
    name:'cathy',
    birth:1990,
    age:function(){
        var that = this;
        function getAgeFromBirth(){
            let year = new Date().getFullYear();
            return year - that.birth;
        }
        return getAgeFromBirth();
    }
}

console.log(cathy.age());//27

//apply和call,区别在于参数，apply的参数是Array,而call不需要
//普通函数不需要指向对象，让this指向null即可，指向对象也不会有问题
console.log(Math.max.apply(null,[2,5,3,1]));//5
console.log(Math.max.call(null,2,5,3,1));//5
console.log(Math.max.call(cathy,2,5,3,1));//5

//使用apply()改变函数行为,叫做装饰器
//比如用计算调用了几次paseInt()方法，可以改写方法
var oldParseInt = parseInt;
// console.log(oldParseInt('10'));//10
// parseInt = function(x){
//     return oldParseInt(x);
// }
// console.log(parseInt('20'));//20

//以下这种写法会返回NaN
// parseInt = function(){
//     for(let arg of arguments)
//         console.log(arg);//20
//     // return oldParseInt(arguments);//NaN，因为arguments是一个数组，原来的parseInt函数接收数组就会返回NaN.除非传入arguments[0]
//     return oldParseInt(arguments[0]);//20
// }
// console.log(parseInt('20'));//20

var count = 0;
parseInt = function(){
    count++;
    return oldParseInt.apply(null,arguments);
    //这里如果写成 oldParseInt(arguments) 将返回NaN
    //如果apply改成call也将返回NaN,因为arguments对应的是Array
    //用call,除非这样
    // return oldParseInt.call(null,arguments[0]);
}

console.log(parseInt('10'));//10
console.log(parseInt('20'));//20
console.log(parseInt('30'));//30

console.log('count:' + count);//count:3

//高阶函数
//一个函数的参数接收另外一个函数，这个函数就称为高阶函数
function fn(x,y,z){
    return z(x) + z(y);
}

console.log(fn(-1,3,Math.abs));//4