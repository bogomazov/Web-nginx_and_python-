Studying project.

Basic website, which proccess user GET queries in a few steps:
<pre>
(example of query: "bogomazz.com/news/politics/5/")
</pre>
1. Calling route file, which opens routes.conf in order to check if url corresponds to alowed ones
routes.conf file example:
<pre><code>
   /
   /news/
   /news/[category]/
   /news/[category]/[article]/
   /gallery/
   /gallery/[album]/
</code></pre>
2. While the route was found, application start to use template engine(jinja2) to render the corresponding html template
3. Returns right HTTP Response codes and body.  
  
