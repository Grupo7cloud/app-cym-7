{"changed":true,"filter":false,"title":"server.py","tooltip":"/templates/server.py","value":"from flask import Flask, render_template, request\n\napp = Flask(__name__)\n\n@app.route(\"/\")\ndef home_page():\n    return render_template(\"home.html\")\n    \n@app.route(\"/register_page\")\ndef register_page():\n    return render_template(\"register.html\")\n\n@app.route(\"/register_user\", methods=[\"post\"])\ndef register_user():\n    id = request.form[\"ID\"]\n    Name = request.form[\"Name\"]\n    Last_Name = request.form[\"Last_Name\"]\n    birthday = request.form[\"Birthday\"]\n    print(id, Name, Last_Name, Birthday)\n    return \"Ok\"\n\nif __name__ == \"__main__\":\n    host = '0.0.0.0'\n    port = '8080'\n    app.run(host, port)","undoManager":{"mark":-2,"position":39,"stack":[[{"start":{"row":0,"column":0},"end":{"row":24,"column":23},"action":"insert","lines":["from flask import Flask, render_template, request","","app = Flask(__name__)","","@app.route(\"/\")","def home_page():","    return render_template(\"home.html\")","    ","@app.route(\"/register_page\")","def register_page():","    return render_template(\"register.html\")","","@app.route(\"/register_user\", methods=[\"post\"])","def register_user():","    id = request.form[\"id\"]","    name = request.form[\"name\"]","    lastname = request.form[\"lastname\"]","    birthday = request.form[\"birthday\"]","    print(id, name, lastname, birthday)","    return \"Ok\"","","if __name__ == \"__main__\":","    host = '0.0.0.0'","    port = '8080'","    app.run(host, port)"],"id":36}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"remove","lines":["n"],"id":37}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["n"],"id":38}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"remove","lines":["n"],"id":39}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["N"],"id":40}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"remove","lines":["l"],"id":41}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"insert","lines":["L"],"id":42}],[{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"insert","lines":[" "],"id":43},{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"insert","lines":["0"]}],[{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"remove","lines":["0"],"id":44}],[{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"remove","lines":["n"],"id":45}],[{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"insert","lines":["N"],"id":46}],[{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"remove","lines":[" "],"id":47}],[{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"insert","lines":["-"],"id":48}],[{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"remove","lines":["-"],"id":49},{"start":{"row":16,"column":7},"end":{"row":16,"column":8},"action":"remove","lines":["t"]}],[{"start":{"row":16,"column":7},"end":{"row":16,"column":8},"action":"insert","lines":["t"],"id":50},{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"insert","lines":["_"]}],[{"start":{"row":16,"column":30},"end":{"row":16,"column":31},"action":"remove","lines":["l"],"id":51}],[{"start":{"row":16,"column":30},"end":{"row":16,"column":31},"action":"insert","lines":["L"],"id":52}],[{"start":{"row":16,"column":34},"end":{"row":16,"column":35},"action":"remove","lines":["n"],"id":53}],[{"start":{"row":16,"column":34},"end":{"row":16,"column":35},"action":"insert","lines":["N"],"id":54}],[{"start":{"row":16,"column":34},"end":{"row":16,"column":35},"action":"insert","lines":["_"],"id":55}],[{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"remove","lines":["n"],"id":56}],[{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":["N"],"id":57}],[{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"remove","lines":["b"],"id":58}],[{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"insert","lines":["B"],"id":59}],[{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"remove","lines":["n"],"id":60}],[{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":["N"],"id":61}],[{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"remove","lines":["l"],"id":62}],[{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"insert","lines":["L"],"id":63}],[{"start":{"row":18,"column":24},"end":{"row":18,"column":25},"action":"remove","lines":["n"],"id":64}],[{"start":{"row":18,"column":24},"end":{"row":18,"column":25},"action":"insert","lines":["N"],"id":65},{"start":{"row":18,"column":25},"end":{"row":18,"column":26},"action":"insert","lines":["_"]}],[{"start":{"row":18,"column":25},"end":{"row":18,"column":26},"action":"remove","lines":["_"],"id":66}],[{"start":{"row":18,"column":24},"end":{"row":18,"column":25},"action":"insert","lines":["_"],"id":67}],[{"start":{"row":18,"column":31},"end":{"row":18,"column":32},"action":"remove","lines":["b"],"id":68}],[{"start":{"row":18,"column":31},"end":{"row":18,"column":32},"action":"insert","lines":["B"],"id":69}],[{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"remove","lines":["d"],"id":70},{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"remove","lines":["i"]}],[{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"insert","lines":["I"],"id":71},{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"insert","lines":["D"]}],[{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"remove","lines":["d"],"id":72},{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"remove","lines":["i"]}],[{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"insert","lines":["I"],"id":73},{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"insert","lines":["D"]}],[{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"remove","lines":["D"],"id":74},{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"remove","lines":["I"]}],[{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"insert","lines":["i"],"id":75},{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"insert","lines":["d"]}]]},"ace":{"folds":[],"scrolltop":90,"scrollleft":0,"selection":{"start":{"row":19,"column":15},"end":{"row":19,"column":15},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":5,"state":"start","mode":"ace/mode/python"}},"timestamp":1718226192222}