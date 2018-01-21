from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())

## result:
b'<html>\n<head>\n<title>A Useful Page</title>\n</head>\n<body>\n<h1>An Interesting Title</h1>\n<div>\nLorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n</div>\n</body>\n</html>\n'

## b''表示bytes,每个字符占一个字节，如果有中文呢？
html = urlopen('http://www.520lovershouse.com/Amap/')
print('\n\n')
print(html.read())

## 遇到中文这里是以utf-8编码显示，如：<title>\xe7\x83\xad\xe5\x8a\x9b\xe5\x9b\xbe</title>
b'\n<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta charset="utf-8">\n<meta http-equiv="X-UA-Compatible" content="IE=edge">\n<meta name="viewport"\n\tcontent="initial-scale=1.0, user-scalable=no, width=device-width">\n<meta name="viewport" content="initial-scale=1.0, user-scalable=no">\n<title>\xe7\x83\xad\xe5\x8a\x9b\xe5\x9b\xbe</title>\n<link rel="stylesheet"\n\thref="http://cache.amap.com/lbs/static/main1119.css" />\n<script\n\tsrc="http://webapi.amap.com/maps?v=1.3&key=12e4f0c4eab3ca523627f048891e07c5"></script>\n<script type="text/javascript"\n\tsrc="http://cache.amap.com/lbs/static/addToolbar.js"></script>\n<script type="text/javascript"\n\tsrc="http://a.amap.com/jsapi_demos/static/resource/heatmapData.js"></script>\n</head>\n<body>\n\t<div id="container"></div>\n\t<div class="button-group">\n\t\t<input type="button" class="button"value="\xe6\x98\xbe\xe7\xa4\xba\xe7\x83\xad\xe5\x8a\x9b\xe5\x9b\xbe"\n\t\t\tonclick="heatmap.show()" /> <input type="button" class="button"\n\t\t\tvalue="\xe5\x85\xb3\xe9\x97\xad\xe7\x83\xad\xe5\x8a\x9b\xe5\x9b\xbe" onclick="heatmap.hide()" />\n\t</div>\n\t<script>\n\t\t//\xe5\x9d\x90\xe6\xa0\x87\xe7\x82\xb9, \xe6\xa8\xa1\xe6\x8b\x9f\xe7\x83\xad\xe5\x8a\x9b\xe5\x9b\xbe\xe6\x95\xb0\xe6\x8d\xae\xe6\xba\x90\n\t\tvar points = [ {\n\t\t\t"lng" : 118.1850385666,\n\t\t\t"lat" : 24.4757439011,\n\t\t\t"count" : 100\n\t\t}, {\n\t\t\t"lng" : 118.1861972809,\n\t\t\t"lat" : 24.4850786157,\n\t\t\t"count" : 60\n\t\t}, {\n\t\t\t"lng" : 118.1649112701,\n\t\t\t"lat" : 24.4796497236,\n\t\t\t"count" : 200\n\t\t}, {\n\t\t\t"lng" : 118.1580448151,\n\t\t\t"lat" : 24.5011295806,\n\t\t\t"count" : 30\n\t\t}, {\n\t\t\t"lng" : 118.1966686249,\n\t\t\t"lat" : 24.4895699680,\n\t\t\t"count" : 200\n\t\t}, {\n\t\t\t"lng" : 118.1835365295,\n\t\t\t"lat" : 24.4943345316,\n\t\t\t"count" : 10\n\t\t}, {\n\t\t\t"lng" : 118.1910896301,\n\t\t\t"lat" : 24.4762126062,\n\t\t\t"count" : 150\n\t\t} ];\n\n\t\tvar map = new AMap.Map("container", {\n\t\t\tresizeEnable : true,\n\t\t\tzoom : 13\n\t\t});\n\t\tif (!isSupportCanvas()) {\n\t\t\talert(\'\xe7\x83\xad\xe5\x8a\x9b\xe5\x9b\xbe\xe4\xbb\x85\xe5\xaf\xb9\xe6\x94\xaf\xe6\x8c\x81canvas\xe7\x9a\x84\xe6\xb5\x8f\xe8\xa7\x88\xe5\x99\xa8\xe9\x80\x82\xe7\x94\xa8,\xe6\x82\xa8\xe6\x89\x80\xe4\xbd\xbf\xe7\x94\xa8\xe7\x9a\x84\xe6\xb5\x8f\xe8\xa7\x88\xe5\x99\xa8\xe4\xb8\x8d\xe8\x83\xbd\xe4\xbd\xbf\xe7\x94\xa8\xe7\x83\xad\xe5\x8a\x9b\xe5\x9b\xbe\xe5\x8a\x9f\xe8\x83\xbd,\xe8\xaf\xb7\xe6\x8d\xa2\xe4\xb8\xaa\xe6\xb5\x8f\xe8\xa7\x88\xe5\x99\xa8\xe8\xaf\x95\xe8\xaf\x95~\')\n\t\t}\n\t\tvar heatmap;\n\t\tmap.plugin([ "AMap.Heatmap" ], function() {\n\t\t\t//\xe5\x88\x9d\xe5\xa7\x8b\xe5\x8c\x96heatmap\xe5\xaf\xb9\xe8\xb1\xa1\n\t\t\theatmap = new AMap.Heatmap(map, {\n\t\t\t\tradius : 25, //\xe7\xbb\x99\xe5\xae\x9a\xe5\x8d\x8a\xe5\xbe\x84\n\t\t\t\topacity : [ 0, 0.8 ]\n\t\t\t});\n\t\t});\n\n\t\theatmap.setDataSet({\n\t\t\tdata : points,\n\t\t\tmax : 200\n\t\t});\n\t\t//\xe5\x88\xa4\xe6\x96\xad\xe6\xb5\x8f\xe8\xa7\x88\xe5\x8c\xba\xe6\x98\xaf\xe5\x90\xa6\xe6\x94\xaf\xe6\x8c\x81canvas\n\t\tfunction isSupportCanvas() {\n\t\t\tvar elem = document.createElement(\'canvas\');\n\t\t\treturn !!(elem.getContext && elem.getContext(\'2d\'));\n\t\t}\n\n\t\tmap.plugin(\'AMap.Geolocation\', function() {\n\t\t\tgeolocation = new AMap.Geolocation({\n\t\t\t\tenableHighAccuracy : true,//\xe6\x98\xaf\xe5\x90\xa6\xe4\xbd\xbf\xe7\x94\xa8\xe9\xab\x98\xe7\xb2\xbe\xe5\xba\xa6\xe5\xae\x9a\xe4\xbd\x8d\xef\xbc\x8c\xe9\xbb\x98\xe8\xae\xa4:true\n\t\t\t\ttimeout : 10000, //\xe8\xb6\x85\xe8\xbf\x8710\xe7\xa7\x92\xe5\x90\x8e\xe5\x81\x9c\xe6\xad\xa2\xe5\xae\x9a\xe4\xbd\x8d\xef\xbc\x8c\xe9\xbb\x98\xe8\xae\xa4\xef\xbc\x9a\xe6\x97\xa0\xe7\xa9\xb7\xe5\xa4\xa7\n\t\t\t\tbuttonOffset : new AMap.Pixel(10, 20),//\xe5\xae\x9a\xe4\xbd\x8d\xe6\x8c\x89\xe9\x92\xae\xe4\xb8\x8e\xe8\xae\xbe\xe7\xbd\xae\xe7\x9a\x84\xe5\x81\x9c\xe9\x9d\xa0\xe4\xbd\x8d\xe7\xbd\xae\xe7\x9a\x84\xe5\x81\x8f\xe7\xa7\xbb\xe9\x87\x8f\xef\xbc\x8c\xe9\xbb\x98\xe8\xae\xa4\xef\xbc\x9aPixel(10, 20)\n\t\t\t\tzoomToAccuracy : false, //\xe5\xae\x9a\xe4\xbd\x8d\xe6\x88\x90\xe5\x8a\x9f\xe5\x90\x8e\xe8\xb0\x83\xe6\x95\xb4\xe5\x9c\xb0\xe5\x9b\xbe\xe8\xa7\x86\xe9\x87\x8e\xe8\x8c\x83\xe5\x9b\xb4\xe4\xbd\xbf\xe5\xae\x9a\xe4\xbd\x8d\xe4\xbd\x8d\xe7\xbd\xae\xe5\x8f\x8a\xe7\xb2\xbe\xe5\xba\xa6\xe8\x8c\x83\xe5\x9b\xb4\xe8\xa7\x86\xe9\x87\x8e\xe5\x86\x85\xe5\x8f\xaf\xe8\xa7\x81\xef\xbc\x8c\xe9\xbb\x98\xe8\xae\xa4\xef\xbc\x9afalse\n\t\t\t\tbuttonPosition : \'RB\'\n\t\t\t});\n\t\t\tmap.addControl(geolocation);\n\t\t\tgeolocation.getCurrentPosition();\n\t\t\tAMap.event.addListener(geolocation, \'complete\', onComplete);//\xe8\xbf\x94\xe5\x9b\x9e\xe5\xae\x9a\xe4\xbd\x8d\xe4\xbf\xa1\xe6\x81\xaf\n\t\t\tAMap.event.addListener(geolocation, \'error\', onError); //\xe8\xbf\x94\xe5\x9b\x9e\xe5\xae\x9a\xe4\xbd\x8d\xe5\x87\xba\xe9\x94\x99\xe4\xbf\xa1\xe6\x81\xaf\n\t\t});\n\t\t//\xe8\xa7\xa3\xe6\x9e\x90\xe5\xae\x9a\xe4\xbd\x8d\xe7\xbb\x93\xe6\x9e\x9c\n\t\tfunction onComplete(data) {\n\t\t//\talert(\'\xe5\xae\x9a\xe4\xbd\x8d\xe6\x88\x90\xe5\x8a\x9f\');\n\t\t\tvar str = [ \'\xe5\xae\x9a\xe4\xbd\x8d\xe6\x88\x90\xe5\x8a\x9f\' ];\n\t\t\tstr.push(\'\xe7\xbb\x8f\xe5\xba\xa6\xef\xbc\x9a\' + data.position.getLng());\n\t\t\tstr.push(\'\xe7\xba\xac\xe5\xba\xa6\xef\xbc\x9a\' + data.position.getLat());\n\n\t\t\t//    alert("\xe7\xbb\x8f\xe5\xba\xa6: " + data.position.getLng() + "  \xe7\xba\xac\xe5\xba\xa6:" + data.position.getLat());\n\t\t\t// \tmap.setCenter(AMap.LngLat(116.418261, 39.921984));\n\t\t    map.setCenter(AMap.LngLat(data.position.getLng(),data.position.getLat()));\n\t\t\tif (data.accuracy) {\n\t\t\t\tstr.push(\'\xe7\xb2\xbe\xe5\xba\xa6\xef\xbc\x9a\' + data.accuracy + \' \xe7\xb1\xb3\');\n\t\t\t}//\xe5\xa6\x82\xe4\xb8\xbaIP\xe7\xb2\xbe\xe7\xa1\xae\xe5\xae\x9a\xe4\xbd\x8d\xe7\xbb\x93\xe6\x9e\x9c\xe5\x88\x99\xe6\xb2\xa1\xe6\x9c\x89\xe7\xb2\xbe\xe5\xba\xa6\xe4\xbf\xa1\xe6\x81\xaf\n\t\t\tstr.push(\'\xe6\x98\xaf\xe5\x90\xa6\xe7\xbb\x8f\xe8\xbf\x87\xe5\x81\x8f\xe7\xa7\xbb\xef\xbc\x9a\' + (data.isConverted ? \'\xe6\x98\xaf\' : \'\xe5\x90\xa6\'));\n\t\t\tdocument.getElementById(\'tip\').innerHTML = str.join(\'<br>\');\n\t\t}\n\t\t//\xe8\xa7\xa3\xe6\x9e\x90\xe5\xae\x9a\xe4\xbd\x8d\xe9\x94\x99\xe8\xaf\xaf\xe4\xbf\xa1\xe6\x81\xaf\n\t\tfunction onError(data) {\n\t\t\talert(\'\xe5\xae\x9a\xe4\xbd\x8d\xe5\xa4\xb1\xe8\xb4\xa5\');\n\t\t\tdocument.getElementById(\'tip\').innerHTML = \'\xe5\xae\x9a\xe4\xbd\x8d\xe5\xa4\xb1\xe8\xb4\xa5\';\n\t\t}\n\t</script>\n</body>\n</html>'

## urllib是python3内置的标准库，文档参考：https://docs.python.org/3/library/urllib.html
## 源码：https://github.com/python/cpython/tree/3.6