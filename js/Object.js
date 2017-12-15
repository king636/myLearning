//对象
// 'use strict'

var person = {
    name:'nick',
    age:30
}

console.log(person.name);//nick
console.log(person['name'])//nick
console.log(person.address);//undefined
console.log(person.toString);//[Function:toString] 继承而来
console.log('toString' in person);//true
console.log(person.hasOwnProperty('name'));//true
console.log(person.hasOwnProperty('toString'));//false

//动态添加属性
person.country = 'China';
console.log(person.hasOwnProperty('country'));//true

person['address'] = 'Xiamen';
console.log(person.hasOwnProperty('address'));//true

//属性为非有效变量
var student = {
    'name':'steven'
}
console.log(student.name);//steven
console.log(student['name']);//steven

//对象的方法
var xiaoming = {
    name:'xiaoming',
    birth:1990,
    age:function(){
        let y = new Date().getFullYear();
        return y - this.birth;//注意this的用法，指向当前对象
    }
}
console.log(xiaoming.age());//27
/**
 * this的用法，只有使用xiaoming.age()时this才是指向xiaoming,否则会未知
 */
function getAge(){
    let y = new Date().getFullYear();
    return y - this.birth;//strict模式下会报错(this指向了undefined).TypeError: Cannot read property 'birth' of undefined
}

xiaoming = {
    birth:1990,
    age:getAge
};
console.log(xiaoming.age());//27
console.log(getAge());//这个时候，this指向了window(浏览器中)．NaN（非strict模式下，如果是strict模式报错如上）

var fn = xiaoming.age;
console.log(fn());//NaN，this也是指向window.

//重构
xiaoming = {
    name:'xiaoming',
    birth:1990,
    age:function(){
        function getAge(){
            let y = new Date().getFullYear();
            return y - this.birth;//这时this不是指向xiaoming,而是指向window(非strict模式)/undefined(strict模式)
        }
        return getAge();
    }
}
console.log(xiaoming.age());//NaN

//改写为：
xiaoming = {
    name:'xiaoming',
    birth:1990,
    age:function(){
        var that = this;
        function getAge(){
            let y = new Date().getFullYear();
            return y - that.birth;//that指向xiaoming
        }
        return getAge();
    }
}
console.log(xiaoming.age());//27

//使用apply()或者call()改写
console.log(getAge.apply(xiaoming,[]));//27
console.log(getAge.apply(xiaoming));//27
console.log(getAge.call(xiaoming));//27

//apply与call的区别在于参数,apply参数为数组，call参数按顺序．
//这里不绑定对象，用null即可
console.log(Math.max.apply(null,[3,5,4]));//5
console.log(Math.max.call(null,3,5,4));//5

//使用apply动态改变函数行为
//*************************复制以下代码到浏览器的console中执行 */
var oldParseInt = window.parseInt;//window在浏览器中使用
var count = 0;

window.parseInt = function(){
    count++;
    return oldParseInt.apply(null,arguments);
}
console.log(parseInt('10'));//10
console.log(parseInt('20'));//20
console.log(count);//2
//********************************************************* */