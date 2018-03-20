<?php
/**
 * {
 * "access_token":"AAAAQosjWDJieBiQZc3to9YQp6HDLvrmyKC+6+iZ3gq7qrkqf50ljZC+Lgoqrg",
 * "refresh_token":"c8ceMEJisO4Se7uGisHoX0f5JEii7JnipglQipkOn5Zp3tyP7dHQoP0zNKHUq2gY",
 * "token_type":"bearer",
 * "expires_in":"3600"
 * }
 */

use Carbon\Carbon;

require '../vendor/autoload.php';

$file = file_get_contents('.env');
foreach (explode(';', $file) as $line) {
    $data = explode('=', $line);
    $env[$data[0]] = $data[1];
}

$data = [
    'access_token' => $_POST['access_token'],
    'state'        => $_POST['state'],
    'token_type'   => $_POST['token_type'],
    'expires_in'   => $_POST['expires_in'],
];

$mysqli = [
    'host'     => $env['DB_HOST'],
    'username' => $env['DB_USER'],
    'password' => $env['DB_PASSWORD'],
    'db'       => $env['DB_NAME'],
    'port'     => $env['DB_PORT'],
    'prefix'   => '',
    'charset'  => $env['DB_CHARSET'],
];
try {
    $db = new MysqliDb ($mysqli);
} catch (Exception $e) {
    die("DB 접속실패 - {$e->getMessage()}");
}

$data = [
//    'id'            => null,
'token'      => $data['access_token'],
//    'refresh_token' => $data['refresh_token'] ?? null,
'expires_at' => Carbon::now()->addSecond($data['expires_in'])->format('Y-m-d H:i:s'),
'created_at' => Carbon::now()->format('Y-m-d H:i:s'),
//    'updated_at'    => null,
];

try {
    $id = $db->insert('tokens', $data);
} catch (Exception $e) {
    // TODO 에러를 안뱉어서 별로임...
    die("DB 쿼리실패 - {$e->getMessage()}");
}

echo '<pre>';
print_r($data);
echo '</pre>';
echo "생선된 ID: {$id}";



