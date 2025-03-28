let username;


document.getElementById("confirm").onclick = function(){
    document.getElementById("scan").volume = 0.2;
    document.getElementById("badSound").volume = 0.2;
    document.getElementById("goodSound").volume = 0.2;
    document.getElementById("verification").pause()
    username = document.getElementById("name").value;
    localStorage.setItem("username", username);
    document.getElementById("scan").play();
    document.getElementById("nameboxBottom").style.display = "none";
    document.getElementById("text").textContent = "Scanning...";
    document.getElementById("name").style.display = "none";
    document.getElementById("confirm").style.display = "none";
    document.getElementById("bg2").style.display = "block";
    setTimeout(function (){
        
        if (username == "Adams" || username == "Ādams" || username == "adams" || username == "ādams" || username == "")
        {
            if (localStorage.getItem("secondAttempt"))
            {
                document.getElementById("changename").play();
            }else
            {
                document.getElementById("wentwrong").play();
                localStorage.setItem("secondAttempt", true);
            }
            document.getElementById("badSound").play();
            document.getElementById("text").style.display = "none";
            document.getElementById("bg2").style.display = "none";
            document.getElementById("tryAgain").style.display = "block";
            document.getElementById("bad").style.display = "block";
        }else
        {
            document.getElementById("wentwell").play();
            document.getElementById("goodSound").play();
            document.getElementById("text").style.display = "none";
            document.getElementById("bg2").style.display = "none";
            document.getElementById("continue").style.display = "block";
            document.getElementById("good").style.display = "block";
        }
                  
      }, 4000);
}

function loadhome(){
    localStorage.setItem("secondAttempt", false);
}

function loadmain(){
    username = localStorage.getItem("username")
    document.getElementById("welcome").textContent = "Hello " + username;
}

function loadcreators(){
    document.getElementById("namebox1").addEventListener("mouseenter", () => {
        document.getElementById("creators").pause();
        document.getElementById("nifty").pause();
        document.getElementById("nifty").currentTime = 0;
        document.getElementById("gross").pause();
        document.getElementById("gross").currentTime = 0;
        document.getElementById("nifty").play();
    });
    
    document.getElementById("namebox2").addEventListener("mouseenter", () => {
        document.getElementById("creators").pause();
        document.getElementById("nifty").pause();
        document.getElementById("nifty").currentTime = 0;
        document.getElementById("gross").pause();
        document.getElementById("gross").currentTime = 0;
        document.getElementById("gross").play();
    });
}