#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
&decode;
&header;

$print=&menu();

print <<"EOF";

<center>
<FONT size="1" color=\"#ffff99\">
$print
</center>
<SCRIPT LANGUAGE = "JavaScript">
function keyDownHandler(e) {
    if (e) { // Firefox
                e.preventDefault();
                e.stopPropagation();
    } else { // IE
                window.event.keyCode = 0;
                return false;
    }
}
document.onkeydown = keyDownHandler;
</script>
EOF
exit;
