<?php
	$host = "localhost";
	$user = "root";
	$pass = "sayangku";
	$db = "db_dws";
	mysql_connect($host, $user, $pass);
	mysql_select_db($db);
	$namafile = $argv[1];
	$file = fopen($namafile,"r");
	while(($data = fgetcsv($file)) !== false){
		if (array(null) !== $data) { 
			$now = $data[0];
			$tgl = $data[1];
			$win_dir = substr($data[2],-3);
			$winds_avg = $data[3];
			$winds_max = $data[4];
			$rain_h = $data[5];
			$rain_d = $data[6];
			$suhu = $data[7];
			$kelembaban = $data[8];
			$press = $data[9];

			$qcek = "SELECT * FROM tb_pengamatan WHERE waktu='$now' and location=4";
			$banyak = mysql_num_rows(mysql_query($qcek));
			//echo "$now, $tgl, $win_dir, $winds_avg, $winds_max, $rain_h, $rain_d, $suhu, $kelembaban, $press\n";
			$query = "INSERT INTO tb_pengamatan(waktu, tanggal, location, suhu, kelembaban, tekanan_udara, kecepatan_angin_avg, kecepatan_angin_max, derajat_arah_angin, hujan_jam, hujan_hari) VALUES('$now', '$tgl', 4, $suhu, $kelembaban, $press, $winds_avg, $winds_max, $win_dir, $rain_h, $rain_d);";
			if($banyak >= 1){
				continue;
			} else { mysql_query($query); }
			//echo "<br>";
		} 
	}
	
	
?>
