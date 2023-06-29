command_script = "$1"

function gm(){
    git add .
    git commit -m "$command_script"
    git push
}

gm