function initMap() {
    var polygonDataInput = document.getElementById('id_polygon_data');
    var polygonData = polygonDataInput.value.trim();
  
    var map = new google.maps.Map(document.getElementById('map-canvas'), {
      center: {lat: 22.5731283, lng: 88.4331429},
      zoom: 8
    });
  
    var zoneCoords = [];
    var coords = polygonData.split(',');
    for (var i = 0; i < coords.length; i++) {
      var latlng = coords[i].trim().split(' ');
      zoneCoords.push({lat: parseFloat(latlng[0]), lng: parseFloat(latlng[1])});
    }
  
    var zone = new google.maps.Polygon({
      paths: zoneCoords,
      strokeColor: '#FF0000',
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: '#FF0000',
      fillOpacity: 0.35
    });
  
    zone.setMap(map);
  }
  