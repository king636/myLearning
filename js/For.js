//循环
'use strict'

var i;
for(i = 1; i < 10; i++){
    console.log('each: ' + i);
}

for(var j = 1; j < 10; j++){
    console.log('second each: ' + j);
}

console.log('i: ' + i);//10
console.log('j: ' + j);//10

//不设条件的循环，无限循环
var x = 1;
for(;;){
    console.log('third each: ' + x);
    x++;
    if(x > 10)
        break;
}

//相当于while
x = 1;
while(x <= 10){
    console.log('forth each: ' + x);
    x++;
    if(x > 10)
        break;
}

//for...in遍历属性
var person = {
    name: 'nick',
    age: 30
}

for(var key in person){
    console.log(key);//获取属性 name age
    console.log(person[key]);//获取属性对应的值 nick 30
    console.log(person.key);//undefined undefined 原因是这里的key都是字符串
}

//数组的索引即属性
var arr = [1,2,3,4,5];
for(key in arr){//key上面已经申明过，注意作用域
    console.log(key);// 0 1 2 3 4
    console.log(arr[key]);//1 2 3 4 5
}