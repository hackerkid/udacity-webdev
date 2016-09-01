import webapp2
import jinja2

form="""
<form action="/testform">
	<select name="yo">
		<option value="1">one</option>
		<option>two</option>
		<option>three</option>
	</select>
	<input type="submit">
</form>
"""

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
    	self.response.headers['Content-Type'] = 'text/html'
        self.response.write(form)

class TestHandler(webapp2.RequestHandler):
    def post(self):
    	self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.request)

    def get(self):
    	self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.request)


app = webapp2.WSGIApplication([('/', HelloWebapp2),('/testform', TestHandler)],
 debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()