<!DOCTYPE>
<html>
<head>
    <title>Check</title>
</head>
<body>
	<h1>Hello, {{ user_name }}</h1>
    <ul id="navigation">
    {% for item in navigation %}
        <li><a href="{{ item }}.html">{{ item }}</a></li>
    {% endfor %}
    </ul>
</body>
</html>