#!/usr/bin/env python3

print("Content-type: text/html")
print()
print("<head>" +
"	<meta charset=\"UTF-8\">" +
"   <title>Route Complexity</title>" +
"   <link rel=\"stylesheet\" type=\"text/css\" href=\"/style.css\" />" +
"   <script src=\"https://api-maps.yandex.ru/2.1/?lang=ru_RU\" type=\"text/javascript\">" +
"    </script>" +
"</head>");

print("<body>" +
"   <header class='header_wrapper'>" +
"   <div class='header'>" +
"       <nav class=\"nav\">" +
"           <ul>" +
"               <li><a href=\"#\">Home</a></li>" +
"               <li><a href=\"#\">About</a></li>" +
"           </ul>" +
"       </nav>" +
"       <span class=\"title\">Route Complexity</span>" +
"   </div>" +
"	</header>");

print("	<div class='main_wrapper'>" +
"    <div class='container'>" +
"      <div class='map_container'>" +
"<!--        <img src=\"res/images/spb-map.jpg\"/> -->" +
"        <div id='map'></div>" +
"      </div>");

print("      <div class='form_wrapper'>" +
"<!--        <h3>Form</h3> -->" +
"        <form class='form' name='data' method='post' action='/res/python/form.py'>" +
"            <div>From</div>" +
"            <input name='from' type='text' size='100'>" +
"            <br>" +
"            <div>To</div>" +
"            <input name='to' type='text' size='100'>" +
"            <br>" +
"            <div>" +
"               <input type='submit'>" +
"               <input type='reset'>" +
"            </div>" +
"       </form>" +
"       <div class='complexity'" +
"       <span>Your route complexity is</span>" + 
"       </div>" +
"      </div>" +
"    </div>" +
"   </div>");

print("<footer class='footer_wrapper'>" +
"       <div class='footer'>" +
"           2017" +
"       </div>" +
"   </footer>" +

"  <script src=\"/res/js/ymap.js\" type=\"text/javascript\">" +
"  </script>" +

"</body>" +
"</html>");
