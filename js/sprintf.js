'use strict'
/**
*
*  Javascript sprintf
*  http://www.webtoolkit.info/
*
*
**/
var sprintfWrapper = {
    init : function () {
      if (typeof arguments == "undefined") { return null; }
      if (arguments.length < 1) { return null; }
      if (typeof arguments[0] != "string") { return null; }
      //RegExp是js的对象，代表正则表达式,这里加判断是防止对象被修改？思考：什么时候会去修改RegExp对象呢？
      if (typeof RegExp == "undefined") { return null; } 
      var string = arguments[0];
      //正则表达式用法，详细见regexp.js
      var exp = new RegExp(/(%([%]|(\-)?(\+|\x20)?(0)?(\d+)?(\.(\d)?)?([bcdfosxX])))/g);
      var matches = new Array();
      var strings = new Array();
      var convCount = 0;
      var stringPosStart = 0;
      var stringPosEnd = 0;
      var matchPosEnd = 0;
      var newString = '';
      var match = null;
      var substitution = null;
      while (match = exp.exec(string)) {
        if (match[9]) { convCount += 1; }
        stringPosStart = matchPosEnd;
        stringPosEnd = exp.lastIndex - match[0].length;
        strings[strings.length] = string.substring(stringPosStart, stringPosEnd);
        matchPosEnd = exp.lastIndex;
        matches[matches.length] = {
          match: match[0],
          left: match[3] ? true : false,
          sign: match[4] || '',
          pad: match[5] || ' ',
          min: match[6] || 0,
          precision: match[8],
          code: match[9] || '%',
          negative: parseInt(arguments[convCount]) < 0 ? true : false,
          argument: String(arguments[convCount])
        };
      }
      strings[strings.length] = string.substring(matchPosEnd);
      if (matches.length == 0) { return string; }
      if ((arguments.length - 1) < convCount) { return null; }
      var code = null;
      var match = null;
      var i = null;
      for (i=0; i<matches.length; i++) {
        if (matches[i].code == '%') { substitution = '%' }
        else if (matches[i].code == 'b') {
          matches[i].argument = String(Math.abs(parseInt(matches[i].argument)).toString(2));
          substitution = sprintfWrapper.convert(matches[i], true);
        }
        else if (matches[i].code == 'c') {
          matches[i].argument = String(String.fromCharCode(parseInt(Math.abs(parseInt(matches[i].argument)))));
          substitution = sprintfWrapper.convert(matches[i], true);
        }
        else if (matches[i].code == 'd') {
          matches[i].argument = String(Math.abs(parseInt(matches[i].argument)));
          substitution = sprintfWrapper.convert(matches[i]);
        }
        else if (matches[i].code == 'f') {
          matches[i].argument = String(Math.abs(parseFloat(matches[i].argument)).toFixed(matches[i].precision ? matches[i].precision : 6));
          substitution = sprintfWrapper.convert(matches[i]);
        }
        else if (matches[i].code == 'o') {
          matches[i].argument = String(Math.abs(parseInt(matches[i].argument)).toString(8));
          substitution = sprintfWrapper.convert(matches[i]);
        }
        else if (matches[i].code == 's') {
          matches[i].argument = matches[i].argument.substring(0, matches[i].precision ? matches[i].precision : matches[i].argument.length)
          substitution = sprintfWrapper.convert(matches[i], true);
        }
        else if (matches[i].code == 'x') {
          matches[i].argument = String(Math.abs(parseInt(matches[i].argument)).toString(16));
          substitution = sprintfWrapper.convert(matches[i]);
        }
        else if (matches[i].code == 'X') {
          matches[i].argument = String(Math.abs(parseInt(matches[i].argument)).toString(16));
          substitution = sprintfWrapper.convert(matches[i]).toUpperCase();
        }
        else {
          substitution = matches[i].match;
        }
        newString += strings[i];
        newString += substitution;
      }
      newString += strings[i];
      return newString;
    },
    convert : function(match, nosign){
      if (nosign) {
        match.sign = '';
      } else {
        match.sign = match.negative ? '-' : match.sign;
      }
      var l = match.min - match.argument.length + 1 - match.sign.length;
      var pad = new Array(l < 0 ? 0 : l).join(match.pad);
      if (!match.left) {
        if (match.pad == "0" || nosign) {
          return match.sign + pad + match.argument;
        } else {
          return pad + match.sign + match.argument;
        }
      } else {
        if (match.pad == "0" || nosign) {
          return match.sign + match.argument + pad.replace(/0/g, ' ');
        } else {
          return match.sign + match.argument + pad;
        }
      }
    }
  }
  var sprintf = sprintfWrapper.init;

  console.log(sprintf('%f',3.14));//3.140000,与python一样，默认小数点后６位
  var a = 10;
  console.log(sprintf('dec=%d oct=%o hexLowerCase=%x hexUpCase=%X',a,a,a,a));//dec=10 oct=12 hexLowerCase=a hexUpCase=A
  console.log(sprintf());//null

  console.log(sprintf('%.3f',3.14));//3.140

  //RegExp修改后，new RegExp报错：TypeError: RegExp is not a constructor
//   RegExp = null;
//   console.log(sprintf('hello RegExp'));

