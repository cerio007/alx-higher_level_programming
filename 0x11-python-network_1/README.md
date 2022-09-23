# Python Network(1)
Project done during **Full Stack Software Engineering studies** at **ALX School**. It aims to learn about HTTP(Hyper-Text Transfer Protocol)  and its relation to web servers
##Requirements
###General
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file at the root of the repo, containing a description of the repository
* A README.md file, at the root of the folder of this project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* You must use get to access to dictionary value by key (it won't throw an exception if the key doesn't exist in the dictionary)
* A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)
* Your code should not be executed when imported (by using `if __name__ == "__main__":`)

## Files

Filename | Description
--- | ---
`0-body_size.sh` | Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.
`1-body.sh` | Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response(Display only body of a 200 status code response).
`2-delete.sh` | Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.
`3-methods.sh` | Bash script that takes in a URL and displays all HTTP methods the server will accept.
`4-header.sh` | Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response.
`5-post_params.sh` |  Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response, a variable email sent with the value test@gmail.com and a variable subject sent with the value `I will always be here for PLD`.
`6-peak.txt` | text file that contains the time complexity required to run the program.
`6-peak.py` |  function that finds a peak in a list of unsorted integers. * `Prototype: def find_peak(list_of_integers):`
`100-status_code.sh` |  Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
`101-post_json.sh | Bash script that sends a `JSON POST` request to a URL passed as the first argument, displays the body of the response and also sends a `POST` request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request.
`102-catch_me.sh` | Bash script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!`, in the body of the response.
