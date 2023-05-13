/**
 * Create a map with a marker.
 * Creating or dragging the marker sets the latitude and longitude values
 * in the input fields.
 */

// var drawingManager = new google.maps.drawing.DrawingManager();
// drawingManager.setMap(map);



function initMap() {
  // const map = new google.maps.Map(document.getElementsByClassName("js-setloc-map"), {
  // const map = new google.maps.Map(document.getElementById("map"), {  
  alert(1234);  
    const map = new google.maps.Map(document.getElementsByClassName("js-setloc-map setloc-map"), {
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

var drawingManager = new google.maps.drawing.DrawingManager({
  drawingMode: google.maps.drawing.OverlayType.POLYGON,
  drawingControl: true,
  drawingControlOptions: {
    position: google.maps.ControlPosition.TOP_CENTER,
    drawingModes: ['polygon'] // Enable only polygons, you can add other shapes if needed
  },
  polygonOptions: {
    editable: true // Allow editing of drawn polygons
  }
});
  // drawingManager.setMap(map);

// Add event listener for polygon complete event
google.maps.event.addListener(drawingManager, 'polygoncomplete', function(polygon) {
  // Store polygon data in JavaScript object
  var polygonData = {
    paths: polygon.getPath().getArray(), // Array of LatLng points
    type: 'polygon' // Type of shape (e.g., polygon, circle, rectangle)
  };
  
  // Send polygon data to server for storing in Django database
  // You can use AJAX or any other method to send the data to your Django view
  // for further processing and storage in the database
  $.post('/store_zone/', polygonData, function(response) {
    // Handle response from server if needed
    console.log(response);
  });
})

;(function($) {
    // We'll insert the map after this element:
    var prev_el_selector = '.form-row.field-longitude';
  
    // The input elements we'll put lat/lon into and use
    // to set the map's initial lat/lon.
    var lat_input_selector = '#id_latitude',
        lon_input_selector = '#id_longitude';
  
    // If we don't have a lat/lon in the input fields,
    // this is where the map will be centered initially.
    var initial_lat = 51.516448,
        initial_lon = -0.130463;
  
    // Initial zoom level for the map.
    var initial_zoom = 6;
  
    // Initial zoom level if input fields have a location.
    var initial_with_loc_zoom = 12;
  
    // Global variables. Nice.
    var map, marker, $lat, $lon;
  
    /**
     * Create HTML elements, display map, set up event listeners.
     */
    function initMap() {
      var $prevEl = $(prev_el_selector);
  
      if ($prevEl.length === 0) {
        // Can't find where to put the map.
        return;
      };
  
      $lat = $(lat_input_selector);
      $lon = $(lon_input_selector);
  
      var has_initial_loc = ($lat.val() && $lon.val());
  
      if (has_initial_loc) {
        // There is lat/lon in the fields, so centre the map on that.
        initial_lat = parseFloat($lat.val());
        initial_lon = parseFloat($lon.val());
        initial_zoom = initial_with_loc_zoom;
      };
  
      $prevEl.after( $('<div class="js-setloc-map setloc-map"></div>') );
      var mapEl = document.getElementsByClassName('js-setloc-map')[0];
  
      map = new google.maps.Map(mapEl, {
        zoom: initial_zoom,
        center: {lat: initial_lat, lng: initial_lon}
      });
  
      // Create but don't position the marker:
      marker = new google.maps.Marker({
        map: map,
        draggable: true,
      });
  
      if (has_initial_loc) {
        // There is lat/lon in the fields, so centre the marker on that.
        setMarkerPosition(initial_lat, initial_lon);
      };
  
      google.maps.event.addListener(map, 'click', function(ev) {
        setMarkerPosition(ev.latLng.lat(), ev.latLng.lng());
      });
      
      google.maps.event.addListener(marker, 'dragend', function() {
        setInputValues(marker.getPosition().lat(), marker.getPosition().lng());
      });
    };
  
    /**
     * Re-position marker and set input values.
     */
    function setMarkerPosition(lat, lon) {
      marker.setPosition({lat: lat, lng: lon});
      setInputValues(lat, lon);
    };
  
    /**
     * Set both lat and lon input values.
     */
    function setInputValues(lat, lon) {
      setInputValue($lat, lat);
      setInputValue($lon, lon);
    };
  
    /**
     * Set the value of $input to val, with the correct decimal places.
     * We work out decimal places using the <input>'s step value, if any.
     */
    function setInputValue($input, val) {
      // step should be like "0.000001".
      var step = $input.prop('step');
      var dec_places = 0;
  
      if (step) {
        if (step.split('.').length == 2) {
          dec_places = step.split('.')[1].length;
        };
  
        val = val.toFixed(dec_places);
      };
  
      $input.val(val);
    };
  
    $(document).ready(function(){
     initMap();
    });
    
  })(django.jQuery);

// // //(django.jQuery);
  
// // function initMap() {
// //   const map = new google.maps.Map(document.getElementById("map"), {
// //     center: { lat: -34.397, lng: 150.644 },
// //     zoom: 8,
// //   });
// //   const drawingManager = new google.maps.drawing.DrawingManager({
// //     drawingMode: google.maps.drawing.OverlayType.MARKER,
// //     drawingControl: true,
// //     drawingControlOptions: {
// //       position: google.maps.ControlPosition.TOP_CENTER,
// //       drawingModes: [
// //         google.maps.drawing.OverlayType.MARKER,
// //         google.maps.drawing.OverlayType.CIRCLE,
// //         google.maps.drawing.OverlayType.POLYGON,
// //         google.maps.drawing.OverlayType.POLYLINE,
// //         google.maps.drawing.OverlayType.RECTANGLE,
// //       ],
// //     },
// //     markerOptions: {
// //       icon: "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png",
// //     },
// //     circleOptions: {
// //       fillColor: "#ffff00",
// //       fillOpacity: 1,
// //       strokeWeight: 5,
// //       clickable: false,
// //       editable: true,
// //       zIndex: 1,
// //     },
// //   });

// //   drawingManager.setMap(map);
// // }

// // window.initMap = initMap;

// const center = { lat: 50.064192, lng: -130.605469 };
// // Create a bounding box with sides ~10km away from the center point
// const defaultBounds = {
//   north: center.lat + 0.1,
//   south: center.lat - 0.1,
//   east: center.lng + 0.1,
//   west: center.lng - 0.1,
// };
// const input = document.getElementById("pac-input");
// const options = {
//   bounds: defaultBounds,
//   componentRestrictions: { country: "us" },
//   fields: ["address_components", "geometry", "icon", "name"],
//   strictBounds: false,
//   types: ["establishment"],
// };
// const autocomplete = new google.maps.places.Autocomplete(input, options);