/* map init */

  var map;
  var markers = [];

  function initialize() {
      sfcenter = new google.maps.LatLng(37.775000, -122.418056)
      var mapOptions = {
        zoom: 13,
        center: sfcenter
      };
      map = new google.maps.Map(document.getElementById('map-canvas'),
          mapOptions);
      google.maps.event.addListener(map, 'click', function() {
         $("#info-wrapper").hide();
      });
      infobox = new InfoBox({
        content: document.getElementById("info-wrapper"),
        disableAutoPan: false,
        maxWidth: 150,
        pixelOffset: new google.maps.Size(-140, 0),
        zIndex: null,
        boxStyle: {
                    background: "url('http://google-maps-utility-library-v3.googlecode.com/svn/trunk/infobox/examples/tipbox.gif') no-repeat",
                    opacity: .9,
                    width: "280px",
            },
        closeBoxMargin: "3px 2px 2px 3px",
        closeBoxURL: "",
        infoBoxClearance: new google.maps.Size(1, 1)
      });
  }

  google.maps.event.addDomListener(window, 'load', initialize);
  var movie_id = -1;

/* autocomplete */
  $(function() {
    $('#welcomeAlert').delay(8000).fadeOut("slow");

    $( "#searchFilm" ).autocomplete({
      source: function( request, response ) {
        $.ajax({
          url: "/cityontheset/api/movies/?",
          dataType: "json",
          data: {
            name: request.term,
            sort: '-release_year',
            limit: 10
          },
          success: function( data ) {
            movie_id = -1;
            response (data);
          }
        });
      },
      minLength: 1,
      focus: function( event, ui ) {
        $( "#searchFilm" ).val( ui.item.name );
        return false;
      },
      select: function( event, ui ) {
        $( "#searchFilm" ).val( ui.item.name + " (" + ui.item.release_year + ")" );
        movie_id = ui.item.id
        return false;
      }
    })
    .autocomplete( "instance" )._renderItem = function( ul, item ) {
      return $( "<li>" )
        .append( "<a>" + item.name + "<br>" + item.release_year + "</a>" )
        .appendTo( ul );
    };
  });

/* search button event handler */
   $(function() {
     $( "#searchBtn" ).click( function() {
        $("#info-wrapper").hide();
        if($("#searchFilm").val() == null || $("#searchFilm").val() == "") {
            $("#navbar-alerts").text("Please enter a film name to search");
            while(markers.length > 0){
              tmp = markers.pop();
              tmp.setMap(null);
            }
            return false;
        }
        $("#navbar-alerts").text("");

        $.ajax({
          url: "/cityontheset/api/cityfilmlocs/?",
          dataType: "json",
          data: {
            movie_id: movie_id
          },
          success: function( data ) {
            while(markers.length > 0){
              tmp = markers.pop();
              tmp.setMap(null);
            }
            if(data.length == 0) {
              $("#navbar-alerts").text("No locations found for this movie");
            }
            else {
              var bounds = new google.maps.LatLngBounds ();

              for(i = 0 ; i < data.length; i++) {
                loc = new google.maps.LatLng(data[i]['location_id']['lat'], data[i]['location_id']['lng']);

                marker = new google.maps.Marker({
                         map:map,
                         draggable:false,
                         animation: google.maps.Animation.DROP,
                         position: loc,
                         data: data[i]
                    });
                markers.push(marker);
                bounds.extend(loc);
                google.maps.event.addListener(marker, 'click', function() {
                    $("div.markerInfo").text('');
                    $("#info-separator1").hide();
                    $("#info-separator2").hide();
                    $("#info-wrapper").show();

                    $("#info-movie").text(this.data['movie_id']['name']);
                    $("#info-location").text(this.data['location_id']['name']);
                    if(this.data['fun_facts'] != null) {
                        $("#info-funFacts").text(this.data['fun_facts']);
                        $("#info-separator1").show();
                    }
                    if(this.data['production_company_id'] != null) {
                        $("#info-prodCompany").text("Produced By: " + this.data['production_company_id']['name']);
                        $("#info-separator2").show();
                    }
                    if(this.data['director_id'] != null) {
                        $("#info-director").text("Directed By: " + this.data['director_id']['name']);
                        $("#info-separator2").show();
                    }

                    if(this.data['actor_1_id'] != null) {
                        $("#info-actor1").text(this.data['actor_1_id']['name']);
                        $("#info-cast").text("Cast:");
                    }
                    if(this.data['actor_2_id'] != null) {
                        $("#info-actor2").text(this.data['actor_2_id']['name']);
                        $("#info-cast").text("Cast:");
                    }
                    if(this.data['actor_3_id'] != null) {
                        $("#info-actor3").text(this.data['actor_3_id']['name']);
                        $("#info-cast").text("Cast:");
                    }

                    if (infobox) {
                        infobox.open(map, this);
                    }
                    map.panTo(loc);
                });
              }
              map.fitBounds(bounds);
            }
          }
        });
       return false;
     });
   });