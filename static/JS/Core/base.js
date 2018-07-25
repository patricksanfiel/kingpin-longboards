/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
window.onload = function(){
   document.getElementById('hamburgerIcon').addEventListener("click", function(){
        var x = document.getElementById("myTopNav");
        if (x.className === "topNav row") {
            x.className += " responsive";
        } else {
            x.className = "topNav row";
        }
    });
}
    


