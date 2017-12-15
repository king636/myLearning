//数组
'use strict'

var arr = [1,2,3,'hello'];
console.log(arr);//[ 1, 2, 3, 'hello' ]
console.log(arr.length);//4
console.log(arr.indexOf(3));//2
console.log(arr.indexOf('3'));//-1 不存在则返回-1
arr[5] = 5;//超过范围，导致arr的长度变大
console.log(arr);//[ 1, 2, 3, 'hello', , 5 ]
console.log(arr[4]);//undefined
console.log(arr.length);//6

//slice(划分，切片),相对于字符串的substring,返回子数组
console.log(arr.slice(1,3));//[ 2, 3 ]
console.log(arr.slice(3));//[ 'hello', , 5 ]
console.log(arr.slice());//[ 1, 2, 3, 'hello', , 5 ]
var b = arr;//引用，指向同一个对象
console.log(b);//[ 1, 2, 3, 'hello', , 5 ]
arr[0] = 'change';
console.log(arr);//[ 'change', 2, 3, 'hello', , 5 ]
console.log(b);//[ 'change', 2, 3, 'hello', , 5 ]
console.log(arr === b);//true

//拷贝数组，指向不同对象
arr[0] = 1;
b = arr.slice();//不带参数，则拷贝整个数组
console.log(b);//[ 1, 2, 3, 'hello', , 5 ]
arr[0] = 'change';
console.log(arr);//[ 'change', 2, 3, 'hello', , 5 ]
console.log(b);//[ 1, 2, 3, 'hello', , 5 ]
console.log(arr === b);//false

//push和pop
//push:数组尾部添加元素
//pop:尾部删除元素
arr.push('add');
console.log(arr);//[ 'change', 2, 3, 'hello', , 5, 'add' ]
console.log(arr.pop());//add
console.log(arr);//[ 'change', 2, 3, 'hello', , 5 ]
arr.pop();
console.log(arr);//[ 'change', 2, 3, 'hello',  ]
console.log(arr[arr.length]);//undefined
arr.pop();
arr.pop();
arr.pop();
arr.pop();
console.log(arr.pop());//change
console.log(arr.pop());//undefined
console.log(arr);//[]

//unshift和shift
//unshift:数组头部添加元素
//shift(换档，去掉):头部删除元素
arr = [1,2,3,4,5];
arr.unshift(0);
console.log(arr);//[ 0, 1, 2, 3, 4, 5 ]
arr.shift();
console.log(arr.shift());//1
console.log(arr);//[ 2, 3, 4, 5 ]
arr.shift();
arr.shift();
arr.shift();
arr.shift();
console.log(arr.shift());//undefined
console.log(arr);//[]

//sort排序
arr = ['B', 'C', 'A'];
arr.sort();
console.log(arr);//[ 'A', 'B', 'C' ]

//自定义排序，待扩展

//reverse反转
arr.reverse();
console.log(arr);//[ 'C', 'B', 'A' ]

//splice(胶接)：从指定的索引开始删除若干元素，则添加若干元素
arr = [1,2,3,4,5,6];
console.log(arr.splice(1,3,'a','b'));//返回删除的元素:[2,3,4]
console.log(arr);[1,'a','b',5,6];
//只删除不添加
console.log(arr.splice(2,2));['b',5]
console.log(arr);//[1,'a',6]
//只添加不删除
console.log(arr.splice(1,0,'x','y'));//[]
console.log(arr);//[1,'x','y','a',6]

//concat(合并)：连接数组，返回一个新的数组
arr = [1,2,3];
var arrConcat = arr.concat(['a','b']);
console.log(arr);//[1,2,3]
console.log(arrConcat);//[1,2,3,'a','b']
arrConcat = arr.concat(1,2,[3,4]);//自动拆开拼接的数组
console.log(arrConcat);//[1,2,3,1,2,3,4]

//join对数组元素进行连接，返回字符串
arr = ['A','B','C'];
var arrJoin = arr.join('-xx');
console.log(arr);//['A','B','C']
console.log(arrJoin);//A-xxB-xxC

//多维数组
arr = [[1,2,3],[['a','b'],4,5]];
console.log(arr[1][0][0]);//a