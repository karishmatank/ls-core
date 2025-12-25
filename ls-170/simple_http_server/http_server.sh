#!/bin/bash

function server() {
    while true
    do
        # #  Below only works for single line input:
        # read method path version

        # Below works for multi line input to account for additional headers:
        message_arr=()
        check=true
        while $check
        do
            read line
            message_arr+=($line)
            if [[ "${#line}" -eq 1 ]]
            then
                check=false
            fi
        done

        method=${message_arr[0]}
        path=${message_arr[1]}

        if [[ $method = "GET" ]]
        then
            if [[ -f ./www/$path ]]
            then
                echo -ne "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: $(wc -c <'./www'$path)\r\n\r\n"; cat ./www/$path; echo -e "\n"
            else
                echo -ne "HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\n\r\n"
            fi
        else
            echo -ne "HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n"
        fi
    done
}

coproc SERVER_PROCESS { server; }

nc -lkv 2345 <&${SERVER_PROCESS[0]} >&${SERVER_PROCESS[1]}

# To start the server, run this in a terminal: /opt/homebrew/bin/bash http_server.sh
# To connect to the port as a client using the terminal, run this: nc -v localhost 2345
# To test using the browser, type: http://localhost:2345/lion.html etc
# The client terminal will show the outputs