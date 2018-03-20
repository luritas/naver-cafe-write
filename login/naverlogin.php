<?php
$file = file_get_contents('.env');
foreach (explode(';', $file) as $line) {
    $data = explode('=', $line);
    $env[$data[0]] = $data[1];
}
// 네이버 로그인 접근토큰 요청 예제
$client_id = $env['CLIENT_ID'];
$redirectURI = urlencode("http://localhost:8080/callback.php");
$state = mt_rand(10000000,90000000);
$apiURL = "https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id=" . $client_id . "&redirect_uri=" . $redirectURI . "&state=" . $state;
echo $apiURL;
?>
<br>
<br>
<br>
<a href="<?php echo $apiURL ?>"><img height="50" src="http://static.nid.naver.com/oauth/small_g_in.PNG"/></a>

