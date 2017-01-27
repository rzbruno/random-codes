<?php

if ($_SERVER['REQUEST_METHOD'] == 'GET')
{
    echo "Server up!";
}
else if ($_SERVER['REQUEST_METHOD'] == 'POST')
{
    //payload: {"name":"Bruno"}

    $json = file_get_contents('php://input');
    $obj = json_decode($json, true);

    print_r($obj["name"]);
}