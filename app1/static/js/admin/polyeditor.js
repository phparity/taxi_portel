(function($) {
    $(document).on('click', '.poly-editor', function(e) {
        e.preventDefault();
        var field = $(this).closest('td').find('input[type="text"]');
        var polygon = field.val();
        var mapOptions = {
            center: { lat: 0, lng: 0 },
            zoom: 2
        };
        var map = new google.maps.Map(document.getElementById('map'), mapOptions);
        var polygon = new google.maps.Polygon({
            map: map,
            paths: google.maps.geometry.encoding.decodePath(polygon),
            editable: true,
            draggable: true
        });
        var infowindow = new google.maps.InfoWindow({
            content: '<div><button id="save-polygon">Save</button></div>'
        });
        infowindow.open(map, polygon);
        google.maps.event.addListener(infowindow, 'domready', function() {
            $('#save-polygon').click(function() {
                field.val(google.maps.geometry.encoding.encodePath(polygon.getPath()));
                infowindow.close();
                map.setMap(null);
            });
        });
    });
})(django.jQuery);
