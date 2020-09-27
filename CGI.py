import cgi
import subprocess
print("context-type: text/html")
print()
print("""
<!DOCTYPE html>
	<html> <head> <title>CGI COMMAND INTERFACE </title> </head>
		<body>
		<center>
			<div class = "form1">
			<form action = '/cgi-bin/CGI.py' >
				<h2 style="color: WHITE">Hello My Name is Rohit Sharma</h2><br><br>
				<h2 style="color: WHITE">Menu Driven Program Using CGI</h2><br><br>
				<h2 style="color: WHITE">Enter your command here</h2>
				<input type = 'text' name = 'z' id = 'num1' placeholder = "Enter Command"/ >
				<input type = 'submit' id = "b2"/>
			</form>
			</div>
			<style type="text/css">
				body
				{
					background-color: black;
				    color: white;
 	     			font-family:Open Sans;
				}
				form1
				{
				    text-align: center;
				    text-decoration-color:green;
				    margin: auto;
				    width: 50vw;
				    height: 50vh;
				    position: absolute;
				    top:1vh;
				    bottom: 1vh;
				    left: 1vw;
				    right: 1vw;
				    margin: auto;
				    padding: 10vh;
   				}
			</style>
		</body>
	</html>
""")
data = cgi.FieldStorage()
u_l = data.getvalue("z")
cmmd = "sudo "+u_l
try:
	output = subprocess.getoutput(cmmd)
	if "command not found" in output or "Error" in output:
		print("\n Sorry oops! something went wrong...")
		print("Please enter valid command")
		print("Try again with correct command")
	else:
		print("\n")
		print("""<h2 style="color: white">Result is: {} </h2>""".format(output))
except:
	print("Error")
