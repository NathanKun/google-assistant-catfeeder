<?php
header('Content-Type:application/json');

$authHeader = $_SERVER['HTTP_AUTHORIZATION'];

// http POST
$url = 'http://77.205.7.197:5678/feed';
$header =
        "Content-type: application/x-www-form-urlencoded\r\n"
        ."Authorization: $authHeader\r\n"
        ."User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36\r\n"
        ."Accept: */*\r\n"
;
$options = array(
    'http' => array(
        'header'  => $header,
        'method'  => 'POST'
    )
);

$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);

libxml_use_internal_errors(true); //Prevents Warnings, remove if desired

$r = json_decode($result)->result;

// response
$res = array(
        'fulfillmentText' => $r,
        'source' => 'CatProgrammer');

echo json_encode($res);
