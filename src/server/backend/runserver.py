from base64 import b64decode
from flask import Flask, request, redirect
from providers.XFLTD import XFLTD

router = Flask(__name__)

@router.route("/xfltd")
def root_xfltd():
    email = request.args.get("email")
    password = b64decode(request.args.get("password")).decode()
    
    with XFLTD() as xfltd:
        xfltd.login(email, password)
        
        subUrl = xfltd.copy()
    
    return redirect(subUrl)

router.run("0.0.0.0", 8080)