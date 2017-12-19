//Map和Set（ES6）
'use strict'

//对象的key只能是字符串,用Map则无限制
var map = new Map([['name','nick'],[2,222],['age',30]]);
console.log(map.get('name'));//nick
console.log(map.get(2));//222
console.log(map);//Map { 'name' => 'nick', 2 => 222, 'age' => 30 }
//修改map,添加多余元素，如下，对map没有影响，忽略多余元素：
map = new Map([['name','nick','abc',1234],[2,222],['age',30]]);
console.log(map.get('name'));//nick
console.log(map);//Map { 'name' => 'nick', 2 => 222, 'age' => 30 }
//如果将key改为其他类型会怎样？
map = new Map([[[1,2],'nick'],['age',30]]);
console.log(map);//Map { [ 1, 2 ] => 'nick', 'age' => 30 }
console.log(map.get([1,2]));//undefined
console.log(map.get('[1,2]'));//undefined
//上面的数组用变量替代
var arr = [1,2];
map = new Map([[arr,'nick'],['age',30]]);
console.log(map);//Map { [ 1, 2 ] => 'nick', 'age' => 30 }
console.log(map.get(arr));//nick
arr[0] = 3;
//就是说map的key是支持可变的
console.log(map);//Map { [ 3, 2 ] => 'nick', 'age' => 30 }
console.log(map.get(arr));//nick
arr[3] = 6;
/**
 * arr动态改变，map对应也改变
 */
console.log(map);//Map { [ 3, 2, , 6 ] => 'nick', 'age' => 30 }
var arr2 = [4,5,6];
console.log(typeof arr);//object
arr = arr2.slice();
console.log(typeof arr);//object
/**
 * arr已经改变了，为什么map里面没有对应改变呢？
 * 从上面打印typeof可知，arr类型也并没有变化，为什么map就不改变了呢
 * 就是说通过arr = arr2.slice()后，arr与map已经失去联系
 * 推测原因：map中通过arr保存的其实是arr指向的堆内存对象，而不是arr这个变量．当通过索引对arr元素进行修改时，对应的堆内存对象也被修改，
 * 所以map的key也就改变了．而通过slice()操作后，arr是重新指向了一个新的堆内存对象，而原来的堆内存对象就没有变量再指向它
 * 了，map也就和arr失去了联系．
 * ！！！这点要特别注意，虽然现在还不知道什么时候map中的key需要用变量，也就是map对比对象，到底什么时候需要？
 */
console.log(arr);//[ 4, 5, 6 ]
console.log(map);//Map { [ 3, 2, , 6 ] => 'nick', 'age' => 30 }


var m2 = new Map();
m2.set('name','Bob');
m2.set(3,333);
m2.set('name','Bob Chen');//key是唯一的，所以会覆盖
console.log(m2.get('name'));//Bob　Chen
console.log(m2.get(3));//333
console.log(m2);//Map { 'name' => 'Bob Chen', 3 => 333 }
m2.delete(3);
console.log(m2);//Map { 'name' => 'Bob Chen'}

//Set只存储key,不存储value
var set = new Set([1,2,3]);
var s2 = new Set();
s2.add(1);
s2.add('name');
s2.add(1);//重复则忽略
s2.add(2);
console.log(set);//Set {1,2,3}
console.log(s2);//Set {1,'name',2}
s2.delete('name');
console.log(s2);//Set {1,2}
//与map类似，set的key也可以是变量,注意变化
arr = [4,5,6];
set = new Set([arr,2,3]);
console.log(set);//Set { [ 4, 5, 6 ], 2, 3 }
arr[0] = 1;
console.log(set);//Set { [ 1, 5, 6 ], 2, 3 }
arr = arr2.slice();
console.log(arr);//[ 4, 5, 6 ]
console.log(set);//Set { [ 1, 5, 6 ], 2, 3 }

/**
 * 问题还是到底什么时候对象不能满足使用map或者set的需求？
 */

// ## python的dict和set,就和js的Object,Map以及Set很类似．
// ## python的set与js的Set用法基本相同，区别在于两个地方：
// # 1. js中，var set = new Set([1,2,3]); 而python是　s = set([1,2,3])
// # 2. 删除key时，python用remove(key);而js用delete(key)
// # 3. python的dict和set的key都不能是list;而js中key可以是数组

// ####### python对比js,python使用dict和set;而js使用了对象，Map和Set,目前暂不知道什么情况要用Map而对象不满足？
// ####### js更灵活，但不容易掌握；python严格，但容易理解