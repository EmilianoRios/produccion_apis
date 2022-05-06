window.onload = function footer(){
    var pathname = window.location.pathname;
    if (pathname == '/login/' || pathname == '/register/' || pathname == '/')
        document.getElementById('sticky-footer').style.position = "absolute";
        document.getElementById("sticky-footer").style.bottom = "0";
        document.getElementById("sticky-footer").style.width = "100%";
}