// // draw.js
// var drawingManager = new google.maps.drawing.DrawingManager();
// drawingManager.setMap(map);

function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
  const drawingManager = new google.maps.drawing.DrawingManager({
    drawingMode: google.maps.drawing.OverlayType.MARKER,
    drawingControl: true,
    drawingControlOptions: {
      position: google.maps.ControlPosition.TOP_CENTER,
      drawingModes: [
        google.maps.drawing.OverlayType.MARKER,
        google.maps.drawing.OverlayType.CIRCLE,
        google.maps.drawing.OverlayType.POLYGON,
        google.maps.drawing.OverlayType.POLYLINE,
        google.maps.drawing.OverlayType.RECTANGLE,
      ],
    },
    markerOptions: {
      icon: "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png",
    },
    circleOptions: {
      fillColor: "#ffff00",
      fillOpacity: 1,
      strokeWeight: 5,
      clickable: false,
      editable: true,
      zIndex: 1,
    },
  });

  drawingManager.setMap(map);
}

window.initMap = initMap;









// var map;
// var drawingManager;

// function initMap() {
//   map = new google.maps.Map(document.getElementById('map'), {
//     center: {lat: 37.7749, lng: -122.4194},
//     zoom: 12
//   });

//   drawingManager = new google.maps.drawing.DrawingManager({
//     drawingMode: google.maps.drawing.OverlayType.POLYGON,
//     drawingControl: true,
//     drawingControlOptions: {
//       position: google.maps.ControlPosition.TOP_CENTER,
//       drawingModes: [
//         google.maps.drawing.OverlayType.POLYGON,
//         google.maps.drawing.OverlayType.POLYLINE
//       ]
//     },
//     polygonOptions: {
//       editable: true
//     }
//   });

//   drawingManager.setMap(map);

//   google.maps.event.addListener(drawingManager, 'overlaycomplete', function(event) {
//     if (event.type == google.maps.drawing.OverlayType.POLYGON) {
//       var path = event.overlay.getPath().getArray();
//       // send path to server to save drawing data
//     }
//   });
// }

// google.maps.event.addDomListener(window, 'load', initMap);