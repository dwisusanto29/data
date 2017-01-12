<?php
	$host = "202.124.205.201";
	$user = "alvin";
	$pass = "alvin";
	$db = "db_dws";
	$link = mysqli_connect($host, $user, $pass, $db);
	//mysql_connect($host, $user, $pass);
	//mysql_select_db($db);
	$namafile = $argv[1];
	$file = fopen($namafile,"r");
	while(($data = fgetcsv($file)) !== false){
		if (array(null) !== $data) { 
			$now = date("Y-m-d H:i:s", strtotime($data[0]));
			$tgl = date("Y-m-d", strtotime($data[0]));;
			$win_dir = substr($data[1],-3);
			$winds_avg = $data[2];
			$winds_max = $data[3];
			$rain_h = $data[4];
			$rain_d = $data[5];
			$suhu = $data[6];
			$kelembaban = $data[7];
			$press = $data[8];

			$qcek = "SELECT * FROM tb_pengamatan WHERE waktu='$now' and location=4";
			$banyak = mysqli_num_rows(mysqli_query($link, $qcek));
			//$banyak = mysql_num_rows(mysql_query($qcek));
			//echo "$now, $tgl, $win_dir, $winds_avg, $winds_max, $rain_h, $rain_d, $suhu, $kelembaban, $press\n";
			$query = "INSERT INTO tb_pengamatan(waktu, tanggal, location, suhu, kelembaban, tekanan_udara, kecepatan_angin_avg, kecepatan_angin_max, derajat_arah_angin, hujan_jam, hujan_hari) VALUES('$now', '$tgl', 4, $suhu, $kelembaban, $press, $winds_avg, $winds_max, $win_dir, $rain_h, $rain_d);";
			if($banyak >= 1 || $suhu < 10 || $suhu > 45 || $press < 800){
				continue;
			} else { 
				mysqli_query($link,$query);
				//mysql_query($query); 
			}
			//echo "<br>";
		} 
	}
	
	
?>
