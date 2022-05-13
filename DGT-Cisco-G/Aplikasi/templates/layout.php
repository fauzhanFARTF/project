<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title> Kelompok G Python</title>

    <link href="{{ url_for('static', filename='css/bootstrap.min.css') }}" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link rel="stylesheet" type=text/css href="{{ url_for('static', filename='css/style.css') }}">

</head>
<body id="home">
    
     <nav class="navbar navbar-expand-lg navbar-light bg-customnav"> 
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Kelompok G Python</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#home">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#about">About</a>
                    </li>
                </ul>
            </div>
            <div class="logo">
                <img src="{{ url_for('static', filename='img/digitalentimg.jpeg') }}" alt="" width="10%">
                <img src="{{ url_for('static', filename='img/cisco.png') }}" alt="" width="10%">
            </div>

        </div>
    </nav>

    <div class="content">
        <h4>Peta Persebaran (Toko Modern) Minimarket, Supermarket, Mall dengan Peta Persebaran Kepadatan Penduduk Kabupaten Tangerang</h4>
        <p>Tujuan: <br>
            Menampilkan secara visual kebutuhan Jumlah Toko Modern yang Tersedia dengan Jumlah Kepadatan Penduduk di Kabupaten Tangerang
        </p>
        {% block body %}{% endblock %}
    </div>

    <div id="about">
        <h3>Tentang Kami</h3>
        <h3>Kelompok G Python</h3>
        <ul>
            <li>Fauzan Nurrachman</li>
            <li>Febri Kurnia Rahman</li>
            <li>Fakhrur Rozi</li>
            <li>Faldi Dwi Hastiya</li>
        </ul>
    </div>
    
</body>
</html>