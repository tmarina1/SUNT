function iniciarMap(){
    var coord = {lat:6.1634733,lng:-75.6049074};
    var map = new google.maps.Map(document.getElementById('mapa'),{
        zoom:10,
        center: coord
    });
    var marker = new google.maps.Marker({
        position:coord,
        map: map
    });
}