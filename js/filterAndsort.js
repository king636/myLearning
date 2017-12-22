'use strict'

//高阶函数filter和sort的用法
//filter与map用法相似，不同的是filter作用于Array每个元素后返回True/False，将False的过滤掉．
var array = [1,2,3,4,5];
//只保留偶数
console.log(array.filter(function(x){ return x % 2 === 0;}));//[ 2, 4 ]

//删除Array中的空字符串
array = ['A','b',null,undefined,'  ','c'];
console.log(array.filter(function(s){ return s && s.trim();}));//[ 'A', 'b', 'c' ]

//filter(callbackFunc())中的回调函数与map一样，实际上有３个参数：
//callbackFunc(element,index,self)分别是元素　索引　数组本身
//利用回调函数的参数特性，可以用filter来对array进行重复元素过滤
array = [1,2,'A',2,'B',null,undefined,1,'A'];
console.log(array.filter(function(ele,ind,self){
    return self.indexOf(ele) == ind;
}));//[ 1, 2, 'A', 'B', null, undefined ]

//sort排序
array = ['Google','apple','Microsoft'];
//根据首字母的accii码来派，'a'的ascii码比大写字母大
console.log(array.sort());//[ 'Google', 'Microsoft', 'apple' ]
array = [1,2,10,20];
//注意：并没有按Number排序，Array排序时元素都是先转为字符串，然后按ascii码排序．
console.log(array.sort());//[ 1, 10, 2, 20 ]

//sort也是高阶函数，可以传入函数自定义排序, 
console.log(array.sort(function(x,y){
    if(x > y)
        return 1;
    if(x < y)
        return -1;
    
    return 0;
}));//[ 1, 2, 10, 20 ]

//如果要从大到小排序，修改返回即可
console.log(array.sort(function(x,y){
    if(x > y)
        return -1;
    if(x < y)
        return 1;
    
    return 0;
}));//[ 20, 10, 2, 1 ]

//sort与map不同的地方在于：array调用sort函数后自身变了