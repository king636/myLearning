//迭代器(ES6)
'use strict'

//Array,Map,Set均属于iterable．Map和Set无法使用索引遍历内容
//iterable使用for...of来遍历内容，python的for...in类似
var arr = [1,2,3];
var map = new Map([['name','nick'],['age',30]]);
var set = new Set([1,2,3]);

for(var key of arr){
    console.log(key);//1 2 3
}

for(key in arr){//注意for...in和for...of的区别
    console.log(key);//0 1 2
}

for(key of map){
    console.log(key);//［'name','nick'] ['age',30]
}

for(key of set){
    console.log(key);// 1 2 3
}

arr.name = 'add';
for(key in arr){
    console.log(arr[key]);//1 2 3 add
}

for(key of arr){
    console.log(key);//1 2 3
}

//更好的方式是使用forEach(ES5.1)
//关于回调函数，forEach的参数中传入的是回调函数，事实上内部已经固定了回调函数参数的先后顺序分别代表：value,key以及集合本身
//这里回调函数参数名随意写，含义都是固定的
arr.forEach(function(value,key,array){
    console.log(value);//1 2 3
    console.log(key);//0 1 2
    console.log(array);//[ 1, 2, 3, name: 'add' ] [ 1, 2, 3, name: 'add' ] [ 1, 2, 3, name: 'add' ]
});

//回调函数参数可省略
arr.forEach(function(aaa){//aaa也就是value
    console.log(aaa);//1 2 3
})

//Map的索引即属性
//Set没有索引
map.forEach(function(value,key){
    console.log(value);//nick 30
    console.log(key);//name age
})

set.forEach(function(value,key){
    console.log(value);//1 2 3
    console.log(key);//1 2 3
})