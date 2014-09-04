<!DOCTYPE>
<html>
<head>
    <title>News</title>
</head>
<body>


    <h1>Сегодняшние новости</h1>
    <ul id="news">
	    {% for item in navigation %}
	    	<li>{{item}}</li>
	    {% endfor %}
	</ul>	
</body>
</html>