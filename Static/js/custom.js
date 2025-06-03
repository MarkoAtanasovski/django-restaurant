// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


// isotope js
$(window).on('load', function () {
    $('.filters_menu li').click(function () {
        $('.filters_menu li').removeClass('active');
        $(this).addClass('active');

        var data = $(this).attr('data-filter');
        $grid.isotope({
            filter: data
        })
    });

    var $grid = $(".grid").isotope({
        itemSelector: ".all",
        percentPosition: false,
        masonry: {
            columnWidth: ".all"
        }
    })
});

// nice select
$(document).ready(function() {
    $('select').niceSelect();
  });

/** google_map js **/
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

// client section owl carousel - UPDATED FIX
$(document).ready(function() {
    var $clientCarousel = $(".client_owl-carousel");
    if ($clientCarousel.length) {
        var totalItems = $clientCarousel.find('.item').length;
        
        $clientCarousel.owlCarousel({
            loop: totalItems > 1,       // Only loop if multiple items
            margin: 20,
            dots: totalItems > 1,       // Only show dots if multiple items
            nav: totalItems > 1,        // Only show nav if multiple items
            autoplay: true,
            autoplayHoverPause: true,
            navText: [
                '<i class="fa fa-angle-left" aria-hidden="true"></i>',
                '<i class="fa fa-angle-right" aria-hidden="true"></i>'
            ],
            responsive: {
                0: { items: 1 },
                768: { items: totalItems > 1 ? 2 : 1 }, // Dynamic item count
                1000: { items: totalItems > 1 ? 2 : 1 }
            }
        });

        // Hide nav completely if only 1 item
        if (totalItems <= 1) {
            $clientCarousel.find('.owl-nav').hide();
        }
    }
});