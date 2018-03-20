<?php
$file = file_get_contents('.env');
foreach (explode(';', $file) as $line) {
    $data = explode('=', $line);
    $env[$data[0]] = $data[1];
}
// 네이버 로그인 콜백 예제
$client_id = $env['CLIENT_ID'];
$client_secret = $env['CLIENT_SECRET'];
$print = print_r($env, true);
$code = $_GET["code"];
$state = $_GET["state"];
$redirectURI = urlencode("http://localhost:8080/callback.php");
$url = "https://nid.naver.com/oauth2.0/token?grant_type=authorization_code&client_id=" . $client_id . "&client_secret=" . $client_secret . "&redirect_uri=" . $redirectURI . "&code=" . $code . "&state=" . $state;
echo " <pre> {$print} </pre>";
echo " <pre> {$url} </pre>";
$is_post = false;
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, $is_post);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$headers = array();
$response = curl_exec($ch);
$status_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
echo '<pre>';
print_r($response);
echo '</pre>';
echo "status_code:" . $status_code . " ";
curl_close($ch);
if ($status_code == 200) {
    echo $response;
} else {
    echo "Error 내용:" . $response;
}
