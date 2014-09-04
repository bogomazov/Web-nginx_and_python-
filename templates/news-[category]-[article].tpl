<!DOCTYPE>
<html>
<head>
    <title>Article</title>
</head>
<body>


    <h1>Your article</h1>
    <ul id="news">
	    {% for item in navigation %}
	    	<li>{{item}}</li>
	    {% endfor %}
	</ul>	
</body>
</html>