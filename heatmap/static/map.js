// From index.html MapBox template.
// Wrap map in an onload function. Heatlayer will callback to this function.
mapboxgl.accessToken = 'pk.eyJ1IjoiYXJkcmFzYTEiLCJhIjoiY2p0YTYzenJpMDduYTQzcDdvYXh3ZWYzdiJ9.xE_42JTgGbph9pLadldcKw';
    var map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/satellite-streets-v11',
      // Centers on TransLoc :)
      center: [-78.839185, 35.873970],
      zoom: 8
    });
    

          // Adds marker to an awesome place!
        //   var popup = new mapboxgl.Popup()
        //   .setHTML('<h3>TransLoc</h3><p>An awesome place to work!</p>');
          
        // var marker = new mapboxgl.Marker()
        //   .setLngLat([-78.839185, 35.873970])
        //   .setPopup(popup)
        //   .addTo(map);
    
        
//         // Testing example from leaflet-heat with just lat, lng
//         // Needs all of these:
// "layers": [
//   {
//     "id": "water",
//     "source": "mapbox-streets",
//     "source-layer": "water",
//     "type": "fill",
//     "paint": {
//       "fill-color": "#00ffff"
//     }
//   }
// // ]
//         var heat = L.heatLayer([
//           [-78.839185, 35.773980, 0.2], // lat, lng
//           ], 
//           {radius: 25});
//           console.log(map)
//           console.log(heat)
//           map.addLayer(heat);
// })


      

// CODE BELOW is from https://docs.mapbox.com/mapbox-gl-js/example/heatmap-layer/ 
// Pasting here as a guide to be heavily cut and adapted.

 
map.on('load', function() {
// Add a geojson point source.
// Heatmap layers also work with a vector tile source.
  map.addSource('test', {
  "type": "geojson",
  "data": {
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [-78.839185, 35.773980]
    },
    
  }
  // lat, lng, int

  });
  
  map.addLayer({
  "id": "test-heat",
  "type": "heatmap",
  "source": "test",
  "maxzoom": 9,
  "paint": {
  // Increase the heatmap weight based on frequency and property magnitude
  "heatmap-weight": [
  "interpolate",
  ["linear"],
  ["get", "mag"],
  0, 0,
  6, 1
  ],
  // Increase the heatmap color weight weight by zoom level
  // heatmap-intensity is a multiplier on top of heatmap-weight
  "heatmap-intensity": [
  "interpolate",
  ["linear"],
  ["zoom"],
  0, 1,
  9, 3
  ],
  // Color ramp for heatmap.  Domain is 0 (low) to 1 (high).
  // Begin color ramp at 0-stop with a 0-transparancy color
  // to create a blur-like effect.
  "heatmap-color": [
  "interpolate",
  ["linear"],
  ["heatmap-density"],
  0, "rgba(33,102,172,0)",
  0.2, "rgb(103,169,207)",
  0.4, "rgb(209,229,240)",
  0.6, "rgb(253,219,199)",
  0.8, "rgb(239,138,98)",
  1, "rgb(178,24,43)"
  ],
  // Adjust the heatmap radius by zoom level
  "heatmap-radius": [
  "interpolate",
  ["linear"],
  ["zoom"],
  0, 2,
  9, 20
  ],
  // Transition from heatmap to circle layer by zoom level
  "heatmap-opacity": [
  "interpolate",
  ["linear"],
  ["zoom"],
  7, 1,
  9, 0
  ],
  }
}
);
})