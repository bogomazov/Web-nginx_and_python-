<head>
    <title>Category</title>
</head>
<body>


    <h1>Перечень категорий</h1>
    <ul id="category">
	    {% for item in navigation %}
	    	<li>{{item}}</li>
	    {% endfor %}
	</ul>	
</body>
</html>